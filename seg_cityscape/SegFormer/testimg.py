# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 19:29:16 2022

@author: MECHREVO
"""
from mmseg.apis import init_segmentor, inference_segmentor
from mmseg.core.evaluation import get_palette
import mmcv
import matplotlib.pyplot as plt
import argparse
import torch
import glob
import time

parser = argparse.ArgumentParser(description="Params")
parser.add_argument("--model",type=str,default='B1',help="test model",)
parser.add_argument("--test_folder",type=str,default='test_frame',help="test frame",)
parser.add_argument("--out_folder",type=str,default='out_frame',help="out frame",)
args = parser.parse_args()

if args.model=='B1':
    config_file = './local_configs/segformer/B1/segformer.b1.1024x1024.city.160k.py'
    checkpoint_file = './checkpoints/segformer.b1.1024x1024.city.160k.pth'
else:
    config_file = './local_configs/segformer/B3/segformer.b3.1024x1024.city.160k.py'
    checkpoint_file = './checkpoints/segformer.b3.1024x1024.city.160k.pth'


model = init_segmentor(config_file, checkpoint_file, device='cuda:0')

def seg_img(path):
    start = time.time()    
    result = inference_segmentor(model, path)
    img = model.show_result(path, result, palette=get_palette('cityscapes'), show=False)
    end_time = (time.time() - start)
    print(end_time)
    img_show=mmcv.bgr2rgb(img)
    save_path=path.replace(args.test_folder,args.out_folder)
    plt.imsave(save_path, img_show)
    return end_time
    

with torch.no_grad():
    filePath = args.test_folder
    test_list= glob.glob(filePath+"/*")
    runtime=0.0
    for img in test_list:
        runtime+=seg_img(img)
        torch.cuda.empty_cache()
    count=len(test_list)
    print("average runtime:")
    rt=runtime/count
    print(rt)