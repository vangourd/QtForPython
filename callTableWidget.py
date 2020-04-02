import sys
from PySide2.QtWidgets import QDialog, QApplication, QTableWidgetItem
from demoTableWidget import *

class MyForm(QDialog):

    def __init__(self,data):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.importTableData(data)
        self.show()

    def importTableData(self,data):
        row=0
        for tup in data:
            col=0
            for item in tup:
                newTableItem = QTableWidgetItem(item)
                self.ui.tableWidget.setItem(row, col, newTableItem)
                col+=1
            row+=1

data = [
    ("Suite", "40"),
    ("Super Luxury", "30"),
    ("Super Deluxe", "20"),
    ("Ordinary", "10")
]

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm(data)
    w.show()
    sys.exit(app.exec_())