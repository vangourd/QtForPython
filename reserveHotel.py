# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reserveHotel.ui'
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
        Dialog.resize(713, 618)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(260, 30, 231, 21))
        font = QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.calendarWidget = QCalendarWidget(Dialog)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(360, 70, 312, 186))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 70, 151, 31))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 270, 151, 31))
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 310, 151, 31))
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(230, 370, 271, 31))
        self.comboBox = QComboBox(Dialog)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(180, 320, 341, 21))
        self.spinBox = QSpinBox(Dialog)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(180, 270, 42, 25))
        self.Enteredinfo = QLabel(Dialog)
        self.Enteredinfo.setObjectName(u"Enteredinfo")
        self.Enteredinfo.setGeometry(QRect(30, 420, 631, 81))
        self.RoomRentInfo = QLabel(Dialog)
        self.RoomRentInfo.setObjectName(u"RoomRentInfo")
        self.RoomRentInfo.setGeometry(QRect(30, 510, 631, 81))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Hotel Room Reservation", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Date of Reservation", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Number of days", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Room type", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Calculate Room Rent", None))
        self.Enteredinfo.setText("")
        self.RoomRentInfo.setText("")
    # retranslateUi

