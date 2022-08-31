
It is suggested that anyone who aims to train models on this system at least reads the yolov5 documentation as it will 
provide valuable insight to the user documentation can be found here https://github.com/ultralytics/yolov5 

# IPS-Image-processing-system-
This is the second half of my honors project the Image processing system. The system can currently be used to train a model to detect trees and tree groups.
The IPS can also display the detections using a dash application as an interactive map. The model used for detection is 
a custom model based on yolov5 

# Usage Training 
To train a model use the load buttons to select folders that contain the images and once you have gone through all three
click the run model button. Run results are saved as yolov5/runs/train/exp<run number>. Model weights are located at yolov5/best.pt
Note the model is yolov5 based so expects the labels to in the same parent directory as the 
images ie /home/Train/Images (image location), /home/Train/Labels (Label for images)


# Usage inferencing (prediction)
To run inferencing on set of captured images simply hit the run inference button and select the folder the images are in,
runs are stored in yolov5/runs/detect/exp<run number>. also note that the labels are saved as runs/detect/exp<runnumber>/labels.
labels are only saved for postive detections 
