# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'demoStudentClass.ui'
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
        Dialog.resize(548, 323)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 60, 161, 31))
        self.lineEditName = QLineEdit(Dialog)
        self.lineEditName.setObjectName(u"lineEditName")
        self.lineEditName.setGeometry(QRect(220, 60, 291, 25))
        self.labelResponse = QLabel(Dialog)
        self.labelResponse.setObjectName(u"labelResponse")
        self.labelResponse.setGeometry(QRect(30, 120, 161, 31))
        self.ButtonClickMe = QPushButton(Dialog)
        self.ButtonClickMe.setObjectName(u"ButtonClickMe")
        self.ButtonClickMe.setGeometry(QRect(260, 190, 88, 27))
        self.lineEditName_2 = QLineEdit(Dialog)
        self.lineEditName_2.setObjectName(u"lineEditName_2")
        self.lineEditName_2.setGeometry(QRect(220, 120, 291, 25))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Student Code", None))
        self.labelResponse.setText(QCoreApplication.translate("Dialog", u"Student Name", None))
        self.ButtonClickMe.setText(QCoreApplication.translate("Dialog", u"Click", None))
    # retranslateUi

