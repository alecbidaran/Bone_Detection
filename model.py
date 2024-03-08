from ultralytics import YOLO
import cv2
def load_model():
  model = YOLO('yolov8n.yaml').load('yolov8n.pt')
  return model

def train_model(model,image_size,epochs):
  model.train(data='data.yaml',epochs=epochs,imgsz=image_size.shape[:2])

def export_model(output_format):
  if output_format is None:
    model.export()  ## Native PyTorch Format
  else:
    model.export(format=output_format) 
  print("The Model is saved!")

def predict(image,model,stream_mode=False,plot=True,save=False):
  if stream_mode:
    res=results=model(image,stream=stream_mode)
  else:
    res=results=model(image,stream=stream_mode)
  if plot:
    res.plot()
  elif save:
    cv2.imwrite("prediction.jpg",res)



  
  
