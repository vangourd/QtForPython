# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'demoRadioButton2.ui'
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
        Dialog.resize(452, 352)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 221, 41))
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.labelSelected = QLabel(Dialog)
        self.labelSelected.setObjectName(u"labelSelected")
        self.labelSelected.setGeometry(QRect(20, 280, 401, 61))
        self.labelSelected.setFont(font)
        self.labelSelected.setWordWrap(True)
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 160, 281, 31))
        self.label_3.setFont(font)
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 190, 148, 83))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.radioButtonCard = QRadioButton(self.layoutWidget)
        self.radioButtonCard.setObjectName(u"radioButtonCard")

        self.verticalLayout_2.addWidget(self.radioButtonCard)

        self.radioButtonPayPal = QRadioButton(self.layoutWidget)
        self.radioButtonPayPal.setObjectName(u"radioButtonPayPal")

        self.verticalLayout_2.addWidget(self.radioButtonPayPal)

        self.radioButtonCashOnDelivery = QRadioButton(self.layoutWidget)
        self.radioButtonCashOnDelivery.setObjectName(u"radioButtonCashOnDelivery")

        self.verticalLayout_2.addWidget(self.radioButtonCashOnDelivery)

        self.layoutWidget1 = QWidget(Dialog)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 50, 111, 112))
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.radioButtonMedium = QRadioButton(self.layoutWidget1)
        self.radioButtonMedium.setObjectName(u"radioButtonMedium")

        self.verticalLayout.addWidget(self.radioButtonMedium)

        self.radioButtonLarge = QRadioButton(self.layoutWidget1)
        self.radioButtonLarge.setObjectName(u"radioButtonLarge")

        self.verticalLayout.addWidget(self.radioButtonLarge)

        self.radioButtonXL = QRadioButton(self.layoutWidget1)
        self.radioButtonXL.setObjectName(u"radioButtonXL")

        self.verticalLayout.addWidget(self.radioButtonXL)

        self.radioButtonXXL = QRadioButton(self.layoutWidget1)
        self.radioButtonXXL.setObjectName(u"radioButtonXXL")

        self.verticalLayout.addWidget(self.radioButtonXXL)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Choose your Shirt Size", None))
        self.labelSelected.setText("")
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Choose your payment method", None))
        self.radioButtonCard.setText(QCoreApplication.translate("Dialog", u"Debit/Credit Card", None))
        self.radioButtonPayPal.setText(QCoreApplication.translate("Dialog", u"PayPal", None))
        self.radioButtonCashOnDelivery.setText(QCoreApplication.translate("Dialog", u"Cash On Delivery", None))
        self.radioButtonMedium.setText(QCoreApplication.translate("Dialog", u"M", None))
        self.radioButtonLarge.setText(QCoreApplication.translate("Dialog", u"L", None))
        self.radioButtonXL.setText(QCoreApplication.translate("Dialog", u"XL", None))
        self.radioButtonXXL.setText(QCoreApplication.translate("Dialog", u"XXL", None))
    # retranslateUi

