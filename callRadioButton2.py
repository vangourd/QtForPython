import sys
from PySide2.QtWidgets import QDialog, QApplication
from demoRadioButton2 import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.radioButtonMedium.toggled.connect(self.dispSelected)
        self.ui.radioButtonLarge.toggled.connect(self.dispSelected)
        self.ui.radioButtonXL.toggled.connect(self.dispSelected)
        self.ui.radioButtonXXL.toggled.connect(self.dispSelected)
        self.ui.radioButtonCard.toggled.connect(self.dispSelected)
        self.ui.radioButtonPayPal.toggled.connect(self.dispSelected)
        self.ui.radioButtonCashOnDelivery.toggled.connect(self.dispSelected)
        self.show()

    def dispSelected(self):
        shirtsize="";
        paymentmethod="";
        if self.ui.radioButtonMedium.isChecked() is True:
            shirtsize = "Medium"
        if self.ui.radioButtonLarge.isChecked() is True:
            shirtsize = "Large"
        if self.ui.radioButtonXL.isChecked() is True:
            shirtsize = "XL"
        if self.ui.radioButtonXXL.isChecked() is True:
            shirtsize = "XXL"
        if self.ui.radioButtonCard.isChecked() is True:
            paymentmethod = "Debit/Credit Card"
        if self.ui.radioButtonCashOnDelivery.isChecked() is True:
            paymentmethod = "Cash on Delivery"
        if self.ui.radioButtonPayPal.isChecked() is True:
            paymentmethod = "PayPal"
        if shirtsize and paymentmethod:
            
            self.ui.labelSelected.setText(f"Chosen shirt size is {shirtsize} and payment method as {paymentmethod}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())