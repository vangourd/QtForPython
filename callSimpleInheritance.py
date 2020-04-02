import sys
from PySide2.QtWidgets import QDialog, QApplication
from demoSimpleInheritance import *

class Student:
    name = ""
    code = ""
    def __init__(self,code,name):
        self.code = code
        self.name = name
    def getCode(self):
        return self.code
    def getName(self):
        return self.name

class Marks(Student):
    historyMarks = 0
    geographyMarks = 0

    def __init__(self,code,name,historyMarks,geographyMarks):
        Student.__init__(self,code,name)
        self.historyMarks = historyMarks
        self.geographyMarks = geographyMarks

    def getHistoryMarks(self):
        return self.historyMarks

    def getGeographyMarks(self):
        return self.geographyMarks
    

class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.ButtonClickMe.clicked.connect(self.dispmessage)
        self.show()
    
    def dispmessage(self):
        marksObj = Marks(self.ui.lineEditCode.text(),
                         self.ui.lineEditName.text(),
                         self.ui.lineEditHistory.text(),
                         self.ui.lineEditGeo.text())
        self.ui.labelResponse.setText(f"Code: {marksObj.getCode()} Name: {marksObj.getCode()} History Marks: {marksObj.getCode()} Geography Marks: {marksObj.getCode()}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())