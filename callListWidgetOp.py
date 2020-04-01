import sys
from PySide2.QtWidgets import QDialog, QApplication, QInputDialog, QListWidgetItem
from demoListWidgetOp import *

itemList = [ 
    "Ice Cream",
    "Soda",
    "Coffee",
    "Chocolate"
]

class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        for item in itemList:
            self.ui.listWidget.addItem(item)
        self.ui.pushButtonAdd.clicked.connect(self.addItem)
        self.ui.pushButtonEdit.clicked.connect(self.editItem)
        self.ui.pushButtonDelete.clicked.connect(self.delItem)
        self.ui.pushButtonDeleteAll.clicked.connect(self.deleteAll)
        self.show()
    
    def addItem(self):
        self.ui.listWidget.addItem(self.ui.lineEdit.text())
        self.ui.lineEdit.setText('')
        self.ui.lineEdit.setFocus()

    def editItem(self):
        row=self.ui.listWidget.currentRow()
        newtext, ok=QInputDialog.getText(self, "Enter new text", "Enter new text")
        if ok and (len(newtext) != 0):
            self.ui.listWidget.takeItem(self.ui.listWidget.currentRow())
            self.ui.listWidget.insertItem(row, QListWidgetItem(newtext))

    def delItem(self):
        self.ui.listWidget.takeItem(self.ui.listWidget.currentRow())
    
    def deleteAll(self):
        self.ui.listWidget.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
