import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import uic
from PyQt6.QtWidgets import QFileDialog
import yaml
import subprocess

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # load pyqt6 gui base file
        uic.loadUi("ips_main_gui.ui", self)

    # method to edit dataset yaml
    def editYaml(self,folder_name,value):
        with open("yolov5/yoloconfig.yaml") as f:
            doc = yaml.safe_load(f)
            doc[value] = folder_name
        with open("yolov5/yoloconfig.yaml", "w") as f:
            yaml.dump(doc, f, default_flow_style=False, sort_keys=False)

    # method that lets the user select the directory of the train data on train data button push
    def loadTrainingdata(self):
        folder_name = QFileDialog.getExistingDirectory(self, "select folder with training data")
        self.listWidget.addItem("Loading Training data from: ", folder_name)
        self.editYaml(folder_name, "train")

    def loadValidationData(self):
        folder_name = QFileDialog.getExistingDirectory(self, "select folder with validation data")
        self.listWidget.addItem("Loading validation data from: ", folder_name)
        self.editYaml(folder_name, "val")

    def sloadTestData(self):
        folder_name = QFileDialog.getExistingDirectory(self, "select folder with testing data")
        self.listWidget.addItem("Loading Test data from: ", folder_name)
        self.editYaml(folder_name, "test")

    def loadResults(self):
        folder_name = QFileDialog.getExistingDirectory(self, "select folder with train data")
        self.listWidget.addItem("Loading Training data from: ", folder_name)
        self.editYaml(folder_name, "train")
    def runModel(self):
        self.listWidget.addItem("Starting Model")
        command = "cd yolov5 && pip3 install -r requirements.txt &&python train.py --hyp /home/ryanscodingden/PycharmProjects/IPS-Image-processing-system-/yolov5/data/hyps/hyp.scratch-low.yaml --img 640 --batch 16 --epochs 3 --data yoloconfig.yaml --weights yolov516.pt"
        subprocess.run(command, shell=True)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()