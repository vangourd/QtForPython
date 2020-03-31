# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'demoCheckBox2.ui'
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
        Dialog.resize(552, 533)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(300, 20, 68, 19))
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 80, 201, 41))
        self.label_2.setFont(font)
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 280, 201, 41))
        self.label_3.setFont(font)
        self.groupBoxDrinks = QGroupBox(Dialog)
        self.groupBoxDrinks.setObjectName(u"groupBoxDrinks")
        self.groupBoxDrinks.setGeometry(QRect(230, 300, 301, 121))
        self.groupBoxDrinks.setFont(font)
        self.groupBoxDrinks.setCheckable(False)
        self.widget = QWidget(self.groupBoxDrinks)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 20, 281, 95))
        self.widget.setFont(font)
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.checkBoxCoffee = QCheckBox(self.widget)
        self.checkBoxCoffee.setObjectName(u"checkBoxCoffee")
        self.checkBoxCoffee.setFont(font)

        self.verticalLayout.addWidget(self.checkBoxCoffee)

        self.checkBoxSoda = QCheckBox(self.widget)
        self.checkBoxSoda.setObjectName(u"checkBoxSoda")
        self.checkBoxSoda.setFont(font)

        self.verticalLayout.addWidget(self.checkBoxSoda)

        self.checkBoxTea = QCheckBox(self.widget)
        self.checkBoxTea.setObjectName(u"checkBoxTea")
        self.checkBoxTea.setFont(font)

        self.verticalLayout.addWidget(self.checkBoxTea)

        self.groupBoxIceCreams = QGroupBox(Dialog)
        self.groupBoxIceCreams.setObjectName(u"groupBoxIceCreams")
        self.groupBoxIceCreams.setGeometry(QRect(230, 90, 301, 171))
        self.groupBoxIceCreams.setFont(font)
        self.widget1 = QWidget(self.groupBoxIceCreams)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(20, 90, 261, 62))
        self.widget1.setFont(font)
        self.verticalLayout_3 = QVBoxLayout(self.widget1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.checkBoxChocAlmond = QCheckBox(self.widget1)
        self.checkBoxChocAlmond.setObjectName(u"checkBoxChocAlmond")
        self.checkBoxChocAlmond.setFont(font)

        self.verticalLayout_3.addWidget(self.checkBoxChocAlmond)

        self.checkBoxRockyRd = QCheckBox(self.widget1)
        self.checkBoxRockyRd.setObjectName(u"checkBoxRockyRd")
        self.checkBoxRockyRd.setFont(font)

        self.verticalLayout_3.addWidget(self.checkBoxRockyRd)

        self.widget2 = QWidget(self.groupBoxIceCreams)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(20, 30, 261, 62))
        self.widget2.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(self.widget2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.checkBoxMintChips = QCheckBox(self.widget2)
        self.checkBoxMintChips.setObjectName(u"checkBoxMintChips")
        self.checkBoxMintChips.setFont(font)

        self.verticalLayout_2.addWidget(self.checkBoxMintChips)

        self.checkBoxCookieDough = QCheckBox(self.widget2)
        self.checkBoxCookieDough.setObjectName(u"checkBoxCookieDough")
        self.checkBoxCookieDough.setFont(font)

        self.verticalLayout_2.addWidget(self.checkBoxCookieDough)

        self.labelAmount = QLabel(Dialog)
        self.labelAmount.setObjectName(u"labelAmount")
        self.labelAmount.setGeometry(QRect(30, 440, 491, 71))
        self.labelAmount.setFont(font)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Menu", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Select your IceCream", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Select your drink", None))
        self.groupBoxDrinks.setTitle(QCoreApplication.translate("Dialog", u"Drinks", None))
        self.checkBoxCoffee.setText(QCoreApplication.translate("Dialog", u"Coffee $2", None))
        self.checkBoxSoda.setText(QCoreApplication.translate("Dialog", u"Soda $3", None))
        self.checkBoxTea.setText(QCoreApplication.translate("Dialog", u"Tea $1", None))
        self.groupBoxIceCreams.setTitle(QCoreApplication.translate("Dialog", u"IceCream", None))
        self.checkBoxChocAlmond.setText(QCoreApplication.translate("Dialog", u"Chocolate Amond $3", None))
        self.checkBoxRockyRd.setText(QCoreApplication.translate("Dialog", u"Rocky Road $5", None))
        self.checkBoxMintChips.setText(QCoreApplication.translate("Dialog", u"Mint Chocolate Chips $4", None))
        self.checkBoxCookieDough.setText(QCoreApplication.translate("Dialog", u"Cookie Dough $2", None))
        self.labelAmount.setText("")
    # retranslateUi

