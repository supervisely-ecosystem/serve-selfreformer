<div align="center" markdown>
<img src="https://user-images.githubusercontent.com/115161827/227239618-52cfebce-8b23-4687-9e36-3c8d37b3a3a5.jpg"/>  

# Serve SelfReformer

<p align="center">
  <a href="#Overview">Overview</a> •
  <a href="#How-To-Run">How To Run</a> 
</p>

[![](https://img.shields.io/badge/supervisely-ecosystem-brightgreen)](https://ecosystem.supervise.ly/apps/supervisely-ecosystem/serve-selfreformer)
[![](https://img.shields.io/badge/slack-chat-green.svg?logo=slack)](https://supervise.ly/slack)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/supervisely-ecosystem/serve-selfreformer)
[![views](https://app.supervise.ly/img/badges/views/supervisely-ecosystem/serve-selfreformer.png)](https://supervise.ly)
[![runs](https://app.supervise.ly/img/badges/runs/supervisely-ecosystem/serve-selfreformer.png)](https://supervise.ly)

</div>


## Overview

This app deploys pretrained **SelfReformer** model as a Supervisely Application for **Salient Instance Segmentation** tasks.

Models under a Salient Instance Segmentation task are usually used for separating foreground from background. They predict a mask for the foreground object. These models are class-agnostic, which means they can't predict a class label for an object.

The app is a serving App that allows you to apply the model to an image inside the Supervisely platform or beyond it (using the [Inference Session API](https://developer.supervise.ly/app-development/neural-network-integration/inference-api-tutorial)).


## Pretrained model

This SelfReformer model is trained on [DUTS-TR](http://saliencydetection.net/duts/) dataset and achieves a good performance on this task (see [authors Readme](https://github.com/BarCodeReader/SelfReformer) and the [paper](https://arxiv.org/abs/2205.11283) for technical details and benchmarks)

### Prediction preview:
![our evaluation](https://raw.githubusercontent.com/supervisely-ecosystem/serve-selfreformer/master/demo_data/image_03_prediction.jpg)

### Authors' comparing with other models:
![prediction previews](https://raw.githubusercontent.com/supervisely-ecosystem/serve-selfreformer/master/SelfReformer/asset/figure1.png)

## How To Run

1. Start the application
2. Open the app in your browser

<img src="https://user-images.githubusercontent.com/31512713/228268903-959167de-1097-437a-a609-c6c514803ff2.png" width="66%"/>

3. Choose the model you want to serve *(there is only one yet)*
4. Click **"SERVE"** button.
5. That's it! Now you can use other apps with your model.

## Related Apps

You can use served model in next Supervisely Applications ⬇️ 

- [Apply NN to Images Project](https://ecosystem.supervise.ly/apps/nn-image-labeling/project-dataset) - app allows to play with different inference options and visualize predictions in real time.  Once you choose inference settings you can apply model to all images in your project to visually analyse predictions and perform automatic data pre-labeling.   
    <img data-key="sly-module-link" data-module-slug="supervisely-ecosystem/nn-image-labeling/project-dataset" src="https://i.imgur.com/M2Tp8lE.png" height="70px" margin-bottom="20px"/>  

- [Apply NN to Videos Project](https://ecosystem.supervise.ly/apps/apply-nn-to-videos-project) - app allows to label your videos using served Supervisely models.  
  <img data-key="sly-module-link" data-module-slug="supervisely-ecosystem/apply-nn-to-videos-project" src="https://imgur.com/LDo8K1A.png" height="70px" margin-bottom="20px" />

- [NN Image Labeling](https://ecosystem.supervise.ly/apps/supervisely-ecosystem%252Fnn-image-labeling%252Fannotation-tool) - integrate any deployed NN to Supervisely Image Labeling UI. Configure inference settings and model output classes. Press `Apply` button (or use hotkey) and detections with their confidences will immediately appear on the image.   
    <img data-key="sly-module-link" data-module-slug="supervisely-ecosystem/nn-image-labeling/annotation-tool" src="https://i.imgur.com/hYEucNt.png" height="70px" margin-bottom="20px"/>



## Acknowledgment

- Based on: [https://github.com/BarCodeReader/SelfReformer](https://github.com/BarCodeReader/SelfReformer)
- Paper: [https://arxiv.org/abs/2205.11283](https://arxiv.org/abs/2205.11283)
