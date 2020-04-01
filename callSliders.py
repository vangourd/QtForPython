import sys
from PySide2.QtWidgets import QDialog, QApplication
from demoSliders import *

class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.horizontalScrollBarSugarlevel.valueChanged.connect(self.scrollHorizontal)
        self.ui.horizontalSliderBloodPressure.valueChanged.connect(self.sliderHorizontal)
        self.ui.verticalScrollBarPulseRate.valueChanged.connect(self.scrollVertical)
        self.ui.verticalSliderCholesterolLvl.valueChanged.connect(self.sliderVertical)
        self.show()

    def scrollHorizontal(self, value):
        self.ui.lineEditResult.setText(f"Sugar Level: {str(value)}")

    def scrollVertical(self, value):
        self.ui.lineEditResult.setText(f"Pulse Rate: {str(value)}")

    def sliderHorizontal(self, value):
        self.ui.lineEditResult.setText(f"Blood Pressure: {str(value)}")

    def sliderVertical(self, value):
        self.ui.lineEditResult.setText(f"Cholesterol Lvl: {str(value)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())