import sys
from PySide2.QtWidgets import QDialog
from PySide2.QtWidgets import QApplication, QWidget, QPushButton
from demoCheckbox1 import *

class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.checkBoxCheese.stateChanged.connect(self.dispAmount)
        self.ui.checkBoxOlives.stateChanged.connect(self.dispAmount)
        self.ui.checkBoxSausage.stateChanged.connect(self.dispAmount)
        self.show()

    def dispAmount(self):
        amount=10
        if self.ui.checkBoxCheese.isChecked():
            amount += 1
        if self.ui.checkBoxOlives.isChecked():
            amount += 1
        if self.ui.checkBoxSausage.isChecked():
            amount += 2
        self.ui.labelAmount.setText(f"Total amount for pizza is ${amount}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())