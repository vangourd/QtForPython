# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'demoCheckbox1.ui'
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
        Dialog.resize(576, 331)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 40, 151, 20))
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 90, 231, 19))
        self.label_2.setFont(font)
        self.labelAmount = QLabel(Dialog)
        self.labelAmount.setObjectName(u"labelAmount")
        self.labelAmount.setGeometry(QRect(30, 260, 371, 51))
        self.labelAmount.setFont(font)
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(270, 90, 171, 95))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.checkBoxCheese = QCheckBox(self.layoutWidget)
        self.checkBoxCheese.setObjectName(u"checkBoxCheese")
        self.checkBoxCheese.setFont(font)

        self.verticalLayout.addWidget(self.checkBoxCheese)

        self.checkBoxOlives = QCheckBox(self.layoutWidget)
        self.checkBoxOlives.setObjectName(u"checkBoxOlives")
        self.checkBoxOlives.setFont(font)

        self.verticalLayout.addWidget(self.checkBoxOlives)

        self.checkBoxSausage = QCheckBox(self.layoutWidget)
        self.checkBoxSausage.setObjectName(u"checkBoxSausage")
        self.checkBoxSausage.setFont(font)

        self.verticalLayout.addWidget(self.checkBoxSausage)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Regular Pizza $10", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Select your extra toppings", None))
        self.labelAmount.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.checkBoxCheese.setText(QCoreApplication.translate("Dialog", u"Extra Cheese $1", None))
        self.checkBoxOlives.setText(QCoreApplication.translate("Dialog", u"Extra Olives $1", None))
        self.checkBoxSausage.setText(QCoreApplication.translate("Dialog", u"Extra Sausage $2", None))
    # retranslateUi

