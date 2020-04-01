# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'demoSliders.ui'
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
        Dialog.resize(706, 552)
        self.horizontalSliderBloodPressure = QSlider(Dialog)
        self.horizontalSliderBloodPressure.setObjectName(u"horizontalSliderBloodPressure")
        self.horizontalSliderBloodPressure.setGeometry(QRect(240, 80, 160, 22))
        self.horizontalSliderBloodPressure.setOrientation(Qt.Horizontal)
        self.verticalSliderCholesterolLvl = QSlider(Dialog)
        self.verticalSliderCholesterolLvl.setObjectName(u"verticalSliderCholesterolLvl")
        self.verticalSliderCholesterolLvl.setGeometry(QRect(430, 120, 22, 160))
        self.verticalSliderCholesterolLvl.setOrientation(Qt.Vertical)
        self.verticalScrollBarPulseRate = QScrollBar(Dialog)
        self.verticalScrollBarPulseRate.setObjectName(u"verticalScrollBarPulseRate")
        self.verticalScrollBarPulseRate.setGeometry(QRect(200, 120, 16, 160))
        self.verticalScrollBarPulseRate.setOrientation(Qt.Vertical)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 130, 81, 19))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(80, 80, 131, 19))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(80, 40, 131, 19))
        self.horizontalScrollBarSugarlevel = QScrollBar(Dialog)
        self.horizontalScrollBarSugarlevel.setObjectName(u"horizontalScrollBarSugarlevel")
        self.horizontalScrollBarSugarlevel.setGeometry(QRect(220, 40, 321, 20))
        self.horizontalScrollBarSugarlevel.setOrientation(Qt.Horizontal)
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(280, 130, 111, 20))
        self.lineEditResult = QLineEdit(Dialog)
        self.lineEditResult.setObjectName(u"lineEditResult")
        self.lineEditResult.setGeometry(QRect(90, 370, 501, 81))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Pulse rate", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Blood Pressure", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Sugar Level", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Cholesterol Lvl", None))
    # retranslateUi

