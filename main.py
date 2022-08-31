import csv
import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import uic
from PyQt6.QtCore import QProcess
from PyQt6.QtWidgets import QFileDialog
import yaml
import subprocess
import os


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # load pyqt6 gui base file
        uic.loadUi("ips_main_gui.ui", self)

    # method to edit dataset yaml
    def editYaml(self, folder_name, value):
        with open("yolov5/yoloconfig.yaml") as f:
            doc = yaml.safe_load(f)
            doc[value] = folder_name
        with open("yolov5/yoloconfig.yaml", "w") as f:
            yaml.dump(doc, f, default_flow_style=False, sort_keys=False)

    # method that lets the user select the directory of the train data on train data button push
    def loadTrainingdata(self):
        folder_name = QFileDialog.getExistingDirectory(self, "select folder with training data")
        self.listWidget.addItem("Loading Training data from: " + str(folder_name))
        self.editYaml(folder_name, "train")

    def loadValidationData(self):
        folder_name = QFileDialog.getExistingDirectory(self, "Select Folder with validation data")
        self.listWidget.addItem("Loading validation data from: " + str(folder_name))
        self.editYaml(folder_name, "val")

    def sloadTestData(self):
        folder_name = QFileDialog.getExistingDirectory(self, "Select Folder with testing data")
        self.listWidget.addItem("Loading Test data from: " + str(folder_name))
        self.editYaml(folder_name, "test")

    def loadResults(self):
        self.listWidget.addItem("loading results")
        # load large csv

        qprocess = QProcess(self)
        qprocess.start('python3', ["visualise.py"])
        qprocess.waitForFinished()
        # webbrowser.open('http://127.0.0.1:8050/')

    def runModel(self):
        self.listWidget.addItem("Installing requirements")
        self.listWidget.addItem("Starting Model")
        qprocess = QProcess(self)
        # command = "cd yolov5 &&python train.py --hyp /home/ryan/PycharmProjects/IPS-Image-processing-system-/yolov5" \
        # "/data/hyps/hyp.scratch-low.yaml --img 640 --batch 5 --epochs 3 --data yoloconfig.yaml --weights " \
        #  "best.pt "
        # qprocess.start("python3", ["python train.py",
        #                            "--hyp /home/ryan/PycharmProjects/IPS-Image-processing-system-/yolov5/data/hyps"
        #                            "/hyp.scratch-low.yaml",
        #                            " --img 640", "--batch 5", "--epochs 3",
        #                            " --data yoloconfig.yaml",
        #                            " --weights best.pt "])

        # subprocess.run(command, shell=True)

    # detection methods
    def loadUnlabeled(self):
        # get the parent directory of the files
        tree_data_location = QFileDialog.getExistingDirectory(self, "Load Unlabeled Tree data")
        tree_data = []
        # tree_results=[]
        # if a folder is selected
        if tree_data_location != "":
            command = "cd yolov5 && python3 detect.py --weights best.pt --source \"" + tree_data_location + "\"" + "--save-txt "
            print(command)
            # run an inference
            subprocess.run(command, shell=True)
            print("fin")
            # for directory in run detect
            label_dir = []
            # for all the runs
            for path, dir, files in os.walk("yolov5/runs/detect"):
                # for each folder in the directory
                for name in dir:
                    # if the folder is a labels folder add it to the list of labels folders
                    if name == "labels":
                        label = os.path.join(path, name)
                        label_dir.append(label)

            # print(label_dir)
            headers = ["capture_id", "latitude", "longitude"]
            capturedata = []
            # for each label directory
            for lab_dir in label_dir:
                # get a list of the labels in the directory
                label_list = os.listdir(lab_dir)
                # get the capture id from the titles and
                for doc in label_list:
                    # skip the existing csv files
                    if doc != "_detectionids.csv":
                        data = doc.split("_")
                        captureid = data[1]
                        lat = data[3]
                        long = data[5]
                        long = long.removesuffix(".txt")
                        capturedata.append([captureid, lat, long])

                # write captureids to document
                csvpath = lab_dir + "/_detectionids.csv"
                with open(csvpath, 'w') as file:
                    writer = csv.writer(file)
                    writer.writerow(headers)
                    writer.writerows(capturedata)








        else:
            self.listWidget.addItem("Canceled Load by User or there is no .png files found")

    def detectTrees(self):
        print("loose")


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
