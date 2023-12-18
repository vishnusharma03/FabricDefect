# Imports
import argparse
import os
import torch
import torch.nn as nn
from torchvision import models
import torchvision.transforms as transforms
from torchvision.models import resnet101
from torchvision.models.detection import FasterRCNN
from torchvision.models.detection.rpn import AnchorGenerator

# Parsers
parser = argparse.ArgumentParser()
parser.add_argument(
    '--epochs',
    default=10,
    help='Number of epochs to train',
    type=int

)
parser.add_argument(
    '--lr',
    default=0.001,
    help='Learning Rate',
    type=float

)
parser.add_argument(
    '--batch',
    default=4,
    help='DataLoader Batch Size',
    type=int

)

args = parser.parse_args()
print(args)

if __name__ == '__main__':
    out_dir = os.path.join('..', 'saved_model')
    # Check why valid_preds is required
    os.makedirs(out_dir, exist_ok=True)

    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

    # Load the pretrained ResNet101 model as the feature extractor
    backbone = resnet101(pretrained=True)

    # Define anchor generator for RPN
    anchor_generator = AnchorGenerator(sizes=((32, 64, 128, 256, 512),),
                                       aspect_ratios=((0.5, 1.0, 2.0),))

    # Define Faster R-CNN model
    model = FasterRCNN(backbone,
                       num_classes=91,  # Number of classes in COCO dataset
                       rpn_anchor_generator=anchor_generator)

    model.to(device)