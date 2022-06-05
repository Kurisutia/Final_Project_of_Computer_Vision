import math
import torch
import torch.nn as nn
from torch.hub import load_state_dict_from_url
import pickle
import numpy as np

from nets.frcnn import FasterRCNN



def resnet50(pretrained=False):
    # model = ResNet(Bottleneck, [3, 4, 6, 3])
    if pretrained:
        # state_dict = torch.load('./resnet50_caffe-788b5fa3.pth')
        # for key, val in state_dict['state_dict'].items():
        #     # if 'backbone' in key:
        #     print(key)
        state_dict = torch.load('./model_data/voc_weights_resnet.pth')
        for key, val in state_dict.items():

            print(key,val.shape)
        # print(model)
        # model.load_state_dict(state_dict['state_dict'])
    # ----------------------------------------------------------------------------#
    #   获取特征提取部分，从conv1到model.layer3，最终获得一个38,38,1024的特征层
    # ----------------------------------------------------------------------------#
    features = list([model.conv1, model.bn1, model.relu, model.maxpool, model.layer1, model.layer2, model.layer3])
    # ----------------------------------------------------------------------------#
    #   获取分类部分，从model.layer4到model.avgpool
    # ----------------------------------------------------------------------------#
    classifier = list([model.layer4, model.avgpool])

    features = nn.Sequential(*features)
    classifier = nn.Sequential(*classifier)
    return features, classifier

if __name__ == "__main__":
    model = FasterRCNN(20, backbone='resnet50')
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model_dict = model.state_dict()
    pretrained_dict = torch.load('./model_data/voc_weights_resnet.pth', map_location=device)
    load_key, no_load_key, temp_dict = [], [], {}
    for k, v in pretrained_dict.items():
        if k in model_dict.keys() and np.shape(model_dict[k]) == np.shape(v) and 'extractor' in k:
            temp_dict[k] = v
            load_key.append(k)
        elif 'extractor' in k:
            no_load_key.append(k)
    model_dict.update(temp_dict)
    model.load_state_dict(model_dict)

    model_dict = model.state_dict()
    # for key, val in model_dict.items():
    #     print(key)
    # resnet50(True)
    # with open('./model_final_4f86c3.pkl','rb') as f:
    #     la = pickle.load(f)
    # for key, val in la['model'].items():
    #     print(key, val.shape)
