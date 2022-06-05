---
# Faster R-CNN


## 1. results
| Model                | Train dataset      | Test dataset  | mAP   |        
| -------------------- | ------------------ | ------------- | ----- | 
|random init | VOC 2007 trainval | VOC 2007 test | 29.60 |  
| ImageNet pretrain  | VOC 2007 trainval  | VOC 2007 test | 74.72| 
|COCO pretrain| VOC 2007 trainval | VOC 2007 test | 77.37 |                                           
|COCO pretrain (freeze)| VOC 2007 trainval | VOC 2007 test | 76.51| 

## 2. preparation
### 2.1 environment
 - pytorch 1.10
 - CUDA 11.0
 - python 3.8
 - RTX 3060
  ### 2.2 dataset
 1.Download the training, validation, test data and VOCdevkit
 
``` javascript
wget http://host.robots.ox.ac.uk/pascal/VOC/voc2007/VOCtrainval_06-Nov-2007.tar
wget http://host.robots.ox.ac.uk/pascal/VOC/voc2007/VOCtest_06-Nov-2007.tar
```

2.Extract all of these tars into one directory named ***VOCdevikit***
```
tar xvf VOCtrainval_06-Nov-2007.tar
tar xvf VOCtest_06-Nov-2007.tar
```

3.run `voc_annotion.py` to generate `2007_trainval.txt` and `2007_val.txt`
### 2.3 weight
download weigh from：https://pan.baidu.com/s/1ZxUAaHj5r2-brNdRYmDwig 
提取码：3tpo
## 3.train

1. modify `Freeze_Train`, `pretrain`,`model_path` in `train.py`
- random init: set `Freeze_Train=False`, `pretrain=False`, `model_path=''`
- imagenet pretrain: set `Freeze_Train=True`, `pretrain=True`, `model_path=''`
- coco pretrain: set `Freeze_Train=True`, `pretrain=False`, `model_path='/path/to/coco weight/'`
2. run `train.py`
3. visualization： loss and map curves are saved in `/plot`.
```
cd plot
tensorboard --logdir=./
```

## 4.test
1. modify `model_path` in `frcnn`
2. run`get_map.py`
 
##  5. inference
1. modify `model_path` in `frcnn`
2. modify `dir_origin_path` in `predict.py` as the directory of images
3. run `predict.py`
- option
	- `mode='predict'` to predict signal image
	- `mode='video'` to prdict video
     
 