import os

from PyQt5.QtWidgets import QDialog, QMessageBox, QFileDialog

from ui.fart import Ui_FartDialog


class fartForm(QDialog,Ui_FartDialog):
    def __init__(self, parent=None):
        super(fartForm, self).__init__(parent)
        self.setupUi(self)
        self.setWindowOpacity(0.93)
        self.btnSubmitFart.clicked.connect(self.submitFart)
        self.btnSubmitFartClass.clicked.connect(self.submitFartClass)
        self.btnSelectClasses.clicked.connect(self.selectClasses)
        self.examplePath = os.getcwd() + "/example/"

    def selectClasses(self):
        fileName_choose, filetype = QFileDialog.getOpenFileName(self,
                                                                "选取文件",
                                                                self.examplePath,
                                                                "Text Files (*.txt);;All Files (*)")
        if fileName_choose == "":
            return
        self.txtClassesPath.setText(fileName_choose)
        with open(self.txtClassesPath,"r") as classesFile:
            data=classesFile.read()
            self.txtClasses.setPlainText(data)


    def submitFartClass(self):
        classes=self.txtClasses.toPlainText()
        if len(classes)<=0:
            QMessageBox().information(self, "提示", "未填写类名")
            return
        self.classes=classes
        self.done(1)

    def submitFart(self):
        self.done(2)