<div align="center" markdown>
<img src="https://user-images.githubusercontent.com/115161827/227239618-52cfebce-8b23-4687-9e36-3c8d37b3a3a5.jpg"/>  

# Serve SelfReformer

<p align="center">
  <a href="#Overview">Overview</a> •
  <a href="#Pretrained-Model">Pretrained Model</a> •
  <a href="#How-To-Run">How To Run</a> •
  <a href="#Inference-Settings">Inference Settings</a> •
  <a href="#Related-apps">Related Apps</a> •
  <a href="#Acknowledgment">Acknowledgment</a>
</p>

[![](https://img.shields.io/badge/supervisely-ecosystem-brightgreen)](../../../../supervisely-ecosystem/serve-selfreformer)
[![](https://img.shields.io/badge/slack-chat-green.svg?logo=slack)](https://supervisely.com/slack)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/supervisely-ecosystem/serve-selfreformer)
[![views](https://app.supervisely.com/img/badges/views/supervisely-ecosystem/serve-selfreformer.png)](https://supervisely.com)
[![runs](https://app.supervisely.com/img/badges/runs/supervisely-ecosystem/serve-selfreformer.png)](https://supervisely.com)

</div>


## Overview

This app deploys pretrained **SelfReformer** model as a Supervisely Application for **Salient Instance Segmentation** tasks.

Models under a Salient Instance Segmentation task are usually used for separating foreground from background. They predict a mask for the foreground object. These models are class-agnostic, which means they can't predict a class label for an object.

The app is a serving App that allows you to apply the model to an image inside the Supervisely platform or beyond it (using the [Inference Session API](https://developer.supervisely.com/app-development/neural-network-integration/inference-api-tutorial)).


## Pretrained model

This SelfReformer model is trained on [DUTS-TR](http://saliencydetection.net/duts/) dataset and achieves a good performance on this task (see [authors Readme](https://github.com/BarCodeReader/SelfReformer) and the [paper](https://arxiv.org/abs/2205.11283) for technical details and benchmarks)

### Prediction preview:
| Input    | Prediction   |
| -------- | ------------ |
| ![bird](https://user-images.githubusercontent.com/31512713/229129414-b9fd8acf-11f0-467b-8e5e-5226d5f51426.jpg) | ![selfreformer](https://user-images.githubusercontent.com/31512713/229128975-e5802e8e-ed29-4227-87c5-5cc8b9843d0d.jpg) |





### Authors' comparing with other models:
![prediction previews](https://raw.githubusercontent.com/supervisely-ecosystem/serve-selfreformer/master/SelfReformer/asset/figure1.png)

## How To Run

1. Start the application from Ecosystem
2. Open the app in your browser

<img src="https://user-images.githubusercontent.com/31512713/228268903-959167de-1097-437a-a609-c6c514803ff2.png" width="80%"/>

3. Select the model you want to deploy *(there is only one yet)*
4. Click **"SERVE"** button.
5. ✅ That's it! Now you can use other apps with your model.


## Inference Settings

- `bbox_padding`: (default `66%`) when applying the model to a crop of an image (ROI), this bbox_padding will expand the crop at the boundaries, getting more image context to the model (may lead to more accurate preditctions). The value can be measured either in pixels (e.g. `100px`) or in percentages (e.g. `10%`)
- `pixel_confidence_threshold`: (default `150`). The model predicts a "soft" masks, i.e. the mask values are in range 0-255, but the mask in Supervisely is a Bitmap and has only two values: 0-1 (one bit). With this threshold we will treat the pixels in the mask as **0** if they are below the **threshold** and as **1** if above.


## Related Apps

You can use deployed model in the following Supervisely Applications ⬇️ 

- [Apply Object Segmentor to Images Project](../../../../supervisely-ecosystem/apply-object-segmentor-to-images-project) - apply a salient segmentation model to labeled rectangles (bbox). A padding can be added to extend the boundaries.
    <img data-key="sly-module-link" data-module-slug="supervisely-ecosystem/apply-object-segmentor-to-images-project" src="https://user-images.githubusercontent.com/115161827/229510088-dfe8413f-ec09-4cca-988e-596aab4dd7d2.jpg" height="70px" margin-bottom="20px"/>

- [Apply NN to Images Project](../../../../../supervisely-ecosystem/nn-image-labeling/project-dataset) - app allows to play with different inference options and visualize predictions in real time.  Once you choose inference settings you can apply model to all images in your project to visually analyse predictions and perform automatic data pre-labeling. 
    <img data-key="sly-module-link" data-module-slug="supervisely-ecosystem/nn-image-labeling/project-dataset" src="https://i.imgur.com/M2Tp8lE.png" height="70px" margin-bottom="20px" />

- [Apply NN to Videos Project](../../../../supervisely-ecosystem/apply-nn-to-videos-project) - app allows to label your videos using served Supervisely models.  
  <img data-key="sly-module-link" data-module-slug="supervisely-ecosystem/apply-nn-to-videos-project" src="https://imgur.com/LDo8K1A.png" height="70px" margin-bottom="20px" />

- [NN Image Labeling](../../../../supervisely-ecosystem/supervisely-ecosystem%252Fnn-image-labeling%252Fannotation-tool) - integrate any deployed NN to Supervisely Image Labeling UI. Configure inference settings and model output classes. Press `Apply` button (or use hotkey) and detections with their confidences will immediately appear on the image.   
    <img data-key="sly-module-link" data-module-slug="supervisely-ecosystem/nn-image-labeling/annotation-tool" src="https://i.imgur.com/hYEucNt.png" height="70px" margin-bottom="20px"/>

## Acknowledgment

- Based on: [https://github.com/BarCodeReader/SelfReformer](https://github.com/BarCodeReader/SelfReformer) ![GitHub Org's stars](https://img.shields.io/github/stars/BarCodeReader/SelfReformer?style=social). Code in this repository is distributed under the BSD 3-Clause license.
- Paper: [https://arxiv.org/abs/2205.11283](https://arxiv.org/abs/2205.11283)
