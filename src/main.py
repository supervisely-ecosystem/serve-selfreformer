import os, sys
import torch
from pathlib import Path
import cv2

import supervisely as sly
from dotenv import load_dotenv
try:
    from typing import Literal
except ImportError:
    # for compatibility with python 3.7
    from typing_extensions import Literal
from typing import List, Any, Dict

from src import selfreformer_api
from src.download_weights import download_selfreformer


load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))
root_source_path = str(Path(__file__).parents[1])
model_data_path = os.path.join(root_source_path, "model", "model_data.json")

device = "cuda" if torch.cuda.is_available() else "cpu"
print("Using device:", device)

class SelfReformerModel(sly.nn.inference.SalientObjectSegmentation):
    def load_on_device(
        self,
        model_dir: str = None,
        device: Literal["cpu", "cuda", "cuda:0", "cuda:1", "cuda:2", "cuda:3"] = "cpu",
    ):
        self.device = device
        self.weights_path = download_selfreformer()
        self.opt = selfreformer_api.get_opt()
        self.model = selfreformer_api.build_model(self.opt, self.weights_path, self.device)
        self.aug = selfreformer_api.get_augment(self.opt)
        self.class_names = ["object_mask"]
        print(f"✅ Model has been successfully loaded on {device.upper()} device")

    def predict(self, image_path: str, settings: Dict[str, Any]) -> List[sly.nn.PredictionMask]:
        threshold_default = self.custom_inference_settings_dict["pixel_confidence_threshold"]
        threshold = settings.get("pixel_confidence_threshold", threshold_default)
        img_np = selfreformer_api.load_image(image_path)
        h,w,c = img_np.shape  # keep for backward resize
        input = selfreformer_api.preprocess_image(img_np, self.aug)
        pred, pred_sal, matt_img = selfreformer_api.predict(input, self.model, self.device)
        pred_sal = cv2.resize(pred_sal, (w, h), interpolation=cv2.INTER_LINEAR)
        mask = self.binarize_mask(pred_sal, threshold)
        return [sly.nn.PredictionMask(class_name=self.class_names[0], mask=mask)]
    
    def get_models(self):
        model_data = sly.json.load_json_file(model_data_path)
        return model_data

    def binarize_mask(self, mask, threshold):
        mask[mask < threshold] = 0
        mask[mask >= threshold] = 1
        return mask

    @property
    def model_meta(self):
        if self._model_meta is None:
            self._model_meta = sly.ProjectMeta(
                [sly.ObjClass(self.class_names[0], sly.Bitmap, [255, 0, 0])]
            )
            self._get_confidence_tag_meta()
        return self._model_meta

    def get_info(self):
        info = super().get_info()
        info["videos_support"] = False
        info["async_video_inference_support"] = False
        return info

    def get_classes(self) -> List[str]:
        return self.class_names


m = SelfReformerModel(
    use_gui=True,
    custom_inference_settings=os.path.join(root_source_path, "custom_settings.yaml"),
)

if sly.is_production():
    m.serve()
else:
    m.load_on_device(m.model_dir, device)
    image_path = "./demo_data/image_01.jpg"
    # rect = sly.Rectangle(360, 542, 474, 700).to_json()
    # ann = m._inference_image_path(image_path=image_path, settings={"rectangle": rect, "bbox_padding":"66%"}, data_to_return={})
    # ann.draw_pretty(sly.image.read(image_path), [255,0,0], 7, output_path="out.png")
    results = m.predict(image_path, settings={})
    vis_path = "./demo_data/image_01_prediction.jpg"
    m.visualize(results, image_path, vis_path, thickness=0)
    print(f"predictions and visualization have been saved: {vis_path}")
