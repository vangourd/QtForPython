import sys
from PySide2.QtWidgets import QDialog, QApplication
from demoStudentClass import *

class Student:
    name = ""
    code = ""
    def __init__(self,code, name):
        self.code = code
        self.name = name
    def getCode(self):
        return self.code
    def printName(self):
        return self.name

class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.ButtonClickMe.clicked.connect(self.dispmessage)
        self.show()

    def dispmessage(self):
        studentObj = Student(self.ui.lineEditName.text(),self.ui.lineEditName_2.text())
        self.ui.labelResponse.setText(f"Hello Code:{studentObj.getCode()} {studentObj.printName()}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())