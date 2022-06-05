# Swin Transformer and SL-Swin for CIFAR-100

此次实验使用代码主要来源于Vision Transformer for Small-Size Datasets论文官方代码，官方GitHub：https://github.com/aanna0701/SPT_LSA_ViT  

## Environment
- pytorch 1.10
- CUDA 11.0
- python 3.8  

## Dataset
- CIFAR-100 

## How to train models
### Pure Swin with ra=1
```bash
python main.py --model swin --ra=1
```
### SL-Swin with ra=3
```bash
python main.py --model swin --is_LSA --is_SPT --ra=3
```  

## How to test your models
### Pure Swin
```bash
python test.py --model swin --resume /path/to/your/xxx.pth
```
### SL-Swin
```bash
python test.py --model swin --is_LSA --is_SPT --resume /path/to/your/xxx.pth
```  

### Model Performance
| Model      | Params | CIFAR100-Top1 err |
|-----------|---------:|--------:|
|Swin+ra=1| 8.1M  | 29.53%  |
|SL-Swin+ra=1| 8.6M  | 25.73%  |
|SL-Swin+ra=3| 8.6M  | 21.15%  |
|SL-Swin+ra=6| 8.6M  | 19.75%  |

### Models We Trained
百度网盘链接：https://pan.baidu.com/s/14KZlYkQloY-VGBMkSe_klg 
提取码：va2v


