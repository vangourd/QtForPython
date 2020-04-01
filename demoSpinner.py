# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'demoSpinner.ui'
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
        Dialog.resize(644, 255)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 50, 81, 20))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 110, 81, 20))
        self.lineEditBookPrice = QLineEdit(Dialog)
        self.lineEditBookPrice.setObjectName(u"lineEditBookPrice")
        self.lineEditBookPrice.setGeometry(QRect(120, 50, 113, 25))
        self.lineEditSugarPrice = QLineEdit(Dialog)
        self.lineEditSugarPrice.setObjectName(u"lineEditSugarPrice")
        self.lineEditSugarPrice.setGeometry(QRect(120, 110, 113, 25))
        self.spinBoxBookQty = QSpinBox(Dialog)
        self.spinBoxBookQty.setObjectName(u"spinBoxBookQty")
        self.spinBoxBookQty.setGeometry(QRect(260, 50, 42, 25))
        self.doubleSpinBoxSugarWeight = QDoubleSpinBox(Dialog)
        self.doubleSpinBoxSugarWeight.setObjectName(u"doubleSpinBoxSugarWeight")
        self.doubleSpinBoxSugarWeight.setGeometry(QRect(260, 110, 64, 25))
        self.lineEditBookAmount = QLineEdit(Dialog)
        self.lineEditBookAmount.setObjectName(u"lineEditBookAmount")
        self.lineEditBookAmount.setEnabled(False)
        self.lineEditBookAmount.setGeometry(QRect(340, 50, 113, 25))
        self.lineEditSugarAmount = QLineEdit(Dialog)
        self.lineEditSugarAmount.setObjectName(u"lineEditSugarAmount")
        self.lineEditSugarAmount.setEnabled(False)
        self.lineEditSugarAmount.setGeometry(QRect(340, 110, 113, 25))
        self.labelTotalAmount = QLabel(Dialog)
        self.labelTotalAmount.setObjectName(u"labelTotalAmount")
        self.labelTotalAmount.setGeometry(QRect(290, 190, 151, 31))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Book Price", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Sugar Price", None))
        self.labelTotalAmount.setText("")
    # retranslateUi

