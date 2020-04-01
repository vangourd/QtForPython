# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'demoComboBox.ui'
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
        Dialog.resize(754, 201)
        self.comboBox = QComboBox(Dialog)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(370, 40, 331, 31))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 50, 211, 21))
        self.labelResult = QLabel(Dialog)
        self.labelResult.setObjectName(u"labelResult")
        self.labelResult.setGeometry(QRect(40, 110, 661, 61))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Saving Account", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"Current Account", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"Recurring Deposit Account", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Dialog", u"Fixed Deposit Account", None))

        self.label.setText(QCoreApplication.translate("Dialog", u"Select your account type", None))
        self.labelResult.setText("")
    # retranslateUi

