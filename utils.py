import glob 
import cv2 
from PIL import Image
import yaml
def config_yaml_File(yaml_path,train_path,val_path):
  config_file_template = f'''
    train: {train_path}
    val: {val_path}

    nc: 7
    names: ['elbow positive', 'fingers positive', 'forearm fracture', 'humerus fracture', 'humerus', 'shoulder fracture', 'wrist positive']
'''

  with open('data.yaml', 'w') as f:
    f.write(config_file_template)
    print("Yaml file saved.")
  
