import sys
from PySide2.QtWidgets import QDialog, QApplication
from demoCalculator import *

class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonPlus.clicked.connect(self.addTwoNum)
        self.ui.pushButtonSubtract.clicked.connect(self.subtractTwoNum)
        self.ui.pushButtonMultiply.clicked.connect(self.multiplyTwoNum)
        self.ui.pushButtonDivide.clicked.connect(self.divideTwoNum)
        self.show()
    
    def addTwoNum(self):
        if len(self.ui.lineEditFirstNumber.text())!=0:
            a=int(self.ui.lineEditFirstNumber.text())
        else:
            a = 0
        if len(self.ui.lineEditSecondNumber.text())!=0:
            b=int(self.ui.lineEditSecondNumber.text())
        else:
            b = 0
        
        sum = a + b
        self.ui.labelResult.setText(f"Addition: {str(sum)}")

    def subtractTwoNum(self):
        if len(self.ui.lineEditFirstNumber.text())!=0:
            a = int(self.ui.lineEditFirstNumber.text())
        else:
            a = 0
        if len(self.ui.lineEditSecondNumber.text())!=0:
            b = int(self.ui.lineEditSecondNumber.text())
        else:
            b = 0
        
        diff = a - b
        self.ui.labelResult.setText(f"Subtraction: {str(diff)}")

    def divideTwoNum(self):
        if len(self.ui.lineEditFirstNumber.text())!=0:
            a = int(self.ui.lineEditFirstNumber.text())
        else:
            a = 0
        if len(self.ui.lineEditSecondNumber.text())!=0:
            b = int(self.ui.lineEditSecondNumber.text())
        else:
            b = 0
        
        division = a/b
        self.ui.labelResult.setText(f"Division: {str(round(division,2))}")

    def multiplyTwoNum(self):
        if len(self.ui.lineEditFirstNumber.text())!=0:
            a = int(self.ui.lineEditFirstNumber.text())
        else:
            a = 0
        if len(self.ui.lineEditSecondNumber.text())!=0:
            b = int(self.ui.lineEditSecondNumber.text())
        else:
            b = 0
        
        multiply = a * b
        self.ui.labelResult.setText(f"Multiply: {str(multiply)}")


if __name__ == "__main__":
        app = QApplication(sys.argv)
        w = MyForm()
        w.show()
        sys.exit(app.exec_())