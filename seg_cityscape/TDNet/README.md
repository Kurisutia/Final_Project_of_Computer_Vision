# Segmenting Video Sequences with TDNet

### 1. Prepare Data

Save video frames with their IDs as names. An examplar video is saved in `./test_video`/test.mp4.

### 2.Prepare Model:

Download pretrained models from the :

link：https://pan.baidu.com/s/1HgAmRIWJvaIyya0sQ6oosg?pwd=ilg8 
pwd：ilg8 

### 3.test

```
cd Testing
python make_video.py --choice=V2I
python test.py --model=td4-psp18/td2psp50
python make_video.py  --choice=I2V
```

