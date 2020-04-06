# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'demoBrowser.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

from PySide2.QtWebEngineWidgets import QWebEngineView


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(599, 601)
        self.lineEditURL = QLineEdit(Dialog)
        self.lineEditURL.setObjectName(u"lineEditURL")
        self.lineEditURL.setGeometry(QRect(80, 20, 371, 20))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 51, 20))
        self.pushButtonGo = QPushButton(Dialog)
        self.pushButtonGo.setObjectName(u"pushButtonGo")
        self.pushButtonGo.setGeometry(QRect(470, 20, 75, 23))
        self.widget = QWebEngineView(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 60, 521, 511))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Enter URL", None))
        self.pushButtonGo.setText(QCoreApplication.translate("Dialog", u"Go", None))
    # retranslateUi

