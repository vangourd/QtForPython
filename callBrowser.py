import sys
from PySide2.QtCore import QUrl
from PySide2.QtWidgets import QDialog, QApplication
from PySide2.QtWebEngineWidgets import QWebEngineView
from demoBrowser import *

class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonGo.clicked.connect(self.dispSite)
        self.show()
    
    def dispSite(self):
        self.ui.widget.load(QUrl(self.ui.lineEditURL.text()))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())