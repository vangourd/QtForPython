import sys
from PySide2.QtWidgets import QDialog, QApplication
from demoCalendar import *

class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.calendarWidget.selectionChanged.connect(self.dispDate)

        self.show()
    
    def dispDate(self):
        self.ui.dateEdit.setDisplayFormat('MMM d yyyy')
        self.ui.dateEdit.setDate(self.ui.calendarWidget.selectedDate())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())