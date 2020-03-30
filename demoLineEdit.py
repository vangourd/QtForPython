# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'demoLineEdit.ui'
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


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.labelResponse = QLabel(Dialog)
        self.labelResponse.setObjectName(u"labelResponse")
        self.labelResponse.setGeometry(QRect(70, 80, 101, 31))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(66, 152, 71, 21))
        self.lineEditName = QLineEdit(Dialog)
        self.lineEditName.setObjectName(u"lineEditName")
        self.lineEditName.setGeometry(QRect(70, 120, 113, 20))
        self.ButtonClickMe = QPushButton(Dialog)
        self.ButtonClickMe.setObjectName(u"ButtonClickMe")
        self.ButtonClickMe.setGeometry(QRect(70, 180, 75, 23))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.labelResponse.setText(QCoreApplication.translate("Dialog", u"Enter your name", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.lineEditName.setText("")
        self.ButtonClickMe.setText(QCoreApplication.translate("Dialog", u"Click", None))
    # retranslateUi

