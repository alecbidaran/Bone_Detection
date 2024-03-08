import torch
import os
from ultralytics import YOLO
import glob 
from ./utils import config_yaml_File,get_image_Size
import models
train_path=' ' ## insert your train dataset path
test_path=' ' ## insert your validation dataset path
config_yaml_File()
image_size=get_image_Size(train_path)

model=models.load_model()
print("Training Model \n")
models.train_model(model,image_size,20)
models.export()
