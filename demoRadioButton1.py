# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'demoRadioButton1.ui'
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
        Dialog.resize(400, 217)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 171, 31))
        self.labelFare = QLabel(Dialog)
        self.labelFare.setObjectName(u"labelFare")
        self.labelFare.setGeometry(QRect(20, 180, 351, 21))
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 70, 172, 83))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.radioButtonFirstClass = QRadioButton(self.widget)
        self.radioButtonFirstClass.setObjectName(u"radioButtonFirstClass")

        self.verticalLayout.addWidget(self.radioButtonFirstClass)

        self.radioButtonBusinessClass = QRadioButton(self.widget)
        self.radioButtonBusinessClass.setObjectName(u"radioButtonBusinessClass")

        self.verticalLayout.addWidget(self.radioButtonBusinessClass)

        self.radioButtonEconomyClass = QRadioButton(self.widget)
        self.radioButtonEconomyClass.setObjectName(u"radioButtonEconomyClass")

        self.verticalLayout.addWidget(self.radioButtonEconomyClass)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Choose the flight type", None))
        self.labelFare.setText("")
        self.radioButtonFirstClass.setText(QCoreApplication.translate("Dialog", u"First Class $150", None))
        self.radioButtonBusinessClass.setText(QCoreApplication.translate("Dialog", u"Business Class $125", None))
        self.radioButtonEconomyClass.setText(QCoreApplication.translate("Dialog", u"Economy Class $100", None))
    # retranslateUi

