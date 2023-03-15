import os, sys
import torch
import torch.nn.functional as F
import numpy as np
import skimage.io as io
import skimage.color as color

sys.path.append('SelfReformer')
from SelfReformer.augments import Augment
from SelfReformer.option import get_option
from SelfReformer.model.network import Net


def build_model(opt, weights_path, device):
    state_dict = torch.load(weights_path, map_location=device)
    model = Net(opt)
    model.to(device).eval()
    model.load_state_dict(state_dict)
    return model

def load_image(image_path):
    return io.imread(image_path)

def preprocess_image(img, aug):
    if len(img.shape) < 3:
        img = color.gray2rgb(img)
    img = aug.resize(img)
    img = np.ascontiguousarray(img.transpose((2, 0, 1)))
    img = aug.norm(aug.to_tensor(img) / 255.)
    img = img.unsqueeze(0)
    return img

@torch.no_grad()
def predict(inputs, model, device):
    inputs = inputs.to(device)
    b, c, h, w = inputs.shape    
    pred = model(inputs)
    
    pred_sal = F.pixel_shuffle(pred[-1], 4)
    pred_sal = F.interpolate(pred_sal, (h,w), mode='bilinear', align_corners=False)
    pred_sal = torch.sigmoid(pred_sal).squeeze()
    pred_sal = (pred_sal * 255.).detach().cpu().numpy().astype('uint8')
    
    matt_img = pred[0].repeat(1,256,1,1)
    matt_img = F.pixel_shuffle(matt_img, 16)
    matt_img = F.interpolate(matt_img, (h,w), mode='bilinear', align_corners=False)
    matt_img = torch.sigmoid(matt_img)
    matt_img = (matt_img*255.).squeeze().detach().cpu().numpy().astype('uint8')
    return pred, pred_sal, matt_img

def save_pred(opt, pred, pred_sal, matt_img, save_root, NAME, h, w):
    save_path_matt = os.path.join(save_root, "{}_matt.png".format(NAME))
    io.imsave(save_path_matt, matt_img)
    
    if opt.save_all:
        for idx, sal in enumerate(pred[1:]):
            scale=224//(sal.shape[-1])
            sal_img = F.pixel_shuffle(sal,scale)
            sal_img = F.interpolate(sal_img, (h,w), mode='bilinear', align_corners=False)
            sal_img = torch.sigmoid(sal_img)
            sal_path = os.path.join(save_root, "{}_sal_{}.png".format(NAME, idx))
            sal_img = sal_img.squeeze().detach().cpu().numpy()
            sal_img = (sal_img * 255).astype('uint8')
            io.imsave(sal_path, sal_img)
    else:
        # save pred image
        save_path_sal = os.path.join(save_root, "{}_sal.png".format(NAME))
        io.imsave(save_path_sal, pred_sal)

def get_augment(opt):
    return Augment(opt)

def get_opt():
    opt = get_option()
    return opt