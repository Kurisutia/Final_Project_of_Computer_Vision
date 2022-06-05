# Segformer

## 1. preparation

### 1.1 requirements

mmcv
torch
torchvision

matplotlib
numpy
terminaltables

codecov
flake8
interrogate
isort==4.3.21
pytest
xdoctest>=0.10.0
yapf

### 1.2 weight

link：https://pan.baidu.com/s/1HgAmRIWJvaIyya0sQ6oosg?pwd=ilg8 
pwd：ilg8 

download weight in the folder named Segformer and put them in the ./checkpoints.

you can see some demos  throught the link.

## 2.test

### 2.1 video_test

put the video in ./test_video,rename it as test.mp4,or change the command.

then run

```
python make_video.py --choice=V2I
python testimg.py  --model=B3/B1
python make_vedio.py  --choice=I2V
```

other parameters

```
python make_video.py  --video_path path to the test video
					  --test_folder   testframes
					  --image_folder  path of outputframes
					  --save_path   path of output video
```

