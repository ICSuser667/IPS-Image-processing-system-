import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import uic
from PyQt6.QtWidgets import QFileDialog
import yaml


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # load pyqt6 gui base file
        uic.loadUi("ips_main_gui.ui", self)

    # method to edit dataset yaml
    def editYaml(self,folder_name,value):
        with open("./yolov5/data/dataset.yaml") as f:
            doc = yaml.safe_load(f)
            doc[value] = folder_name
        with open("./yolov5/data/dataset.yaml", "w") as f:
            yaml.dump(doc, f, default_flow_style=False, sort_keys=False)

    # method that lets the user select the directory of the train data on train data button push
    def loadTrainingdata(self):
        folder_name = QFileDialog.getExistingDirectory(self, "select folder with train data")
        print("Loading Training data from: ", folder_name)
        self.editYaml(folder_name, "train")

    def loadValidationData(self):
        folder_name = QFileDialog.getExistingDirectory(self, "select folder with train data")
        print("Loading validation data from: ", folder_name)
        self.editYaml(folder_name, "val")

    def sloadTestData(self):
        folder_name = QFileDialog.getExistingDirectory(self, "select folder with train data")
        print("Loading Test data from: ", folder_name)
        self.editYaml(folder_name, "test")

    def loadResults(self):
        folder_name = QFileDialog.getExistingDirectory(self, "select folder with train data")
        print("Loading Training data from: ", folder_name)
        self.editYaml(folder_name, "train")

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()