# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'demoCalculator.ui'
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
        Dialog.resize(422, 279)
        self.labelFirstNumber = QLabel(Dialog)
        self.labelFirstNumber.setObjectName(u"labelFirstNumber")
        self.labelFirstNumber.setGeometry(QRect(10, 20, 151, 31))
        self.labelSecondNumber = QLabel(Dialog)
        self.labelSecondNumber.setObjectName(u"labelSecondNumber")
        self.labelSecondNumber.setGeometry(QRect(10, 60, 181, 41))
        self.labelResult = QLabel(Dialog)
        self.labelResult.setObjectName(u"labelResult")
        self.labelResult.setGeometry(QRect(10, 220, 391, 51))
        self.lineEditFirstNumber = QLineEdit(Dialog)
        self.lineEditFirstNumber.setObjectName(u"lineEditFirstNumber")
        self.lineEditFirstNumber.setGeometry(QRect(200, 30, 181, 25))
        self.lineEditSecondNumber = QLineEdit(Dialog)
        self.lineEditSecondNumber.setObjectName(u"lineEditSecondNumber")
        self.lineEditSecondNumber.setGeometry(QRect(200, 70, 181, 25))
        self.pushButtonPlus = QPushButton(Dialog)
        self.pushButtonPlus.setObjectName(u"pushButtonPlus")
        self.pushButtonPlus.setGeometry(QRect(40, 130, 171, 27))
        self.pushButtonSubtract = QPushButton(Dialog)
        self.pushButtonSubtract.setObjectName(u"pushButtonSubtract")
        self.pushButtonSubtract.setGeometry(QRect(40, 170, 171, 27))
        self.pushButtonMultiply = QPushButton(Dialog)
        self.pushButtonMultiply.setObjectName(u"pushButtonMultiply")
        self.pushButtonMultiply.setGeometry(QRect(223, 130, 171, 27))
        self.pushButtonDivide = QPushButton(Dialog)
        self.pushButtonDivide.setObjectName(u"pushButtonDivide")
        self.pushButtonDivide.setGeometry(QRect(223, 170, 171, 27))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.labelFirstNumber.setText(QCoreApplication.translate("Dialog", u"Enter First Number", None))
        self.labelSecondNumber.setText(QCoreApplication.translate("Dialog", u"Enter Second Number", None))
        self.labelResult.setText("")
        self.pushButtonPlus.setText(QCoreApplication.translate("Dialog", u"+", None))
        self.pushButtonSubtract.setText(QCoreApplication.translate("Dialog", u"-", None))
        self.pushButtonMultiply.setText(QCoreApplication.translate("Dialog", u"*", None))
        self.pushButtonDivide.setText(QCoreApplication.translate("Dialog", u"/", None))
    # retranslateUi

