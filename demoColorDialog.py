# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'demoColorDialog.ui'
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
        Dialog.resize(601, 292)
        self.pushButtonColor = QPushButton(Dialog)
        self.pushButtonColor.setObjectName(u"pushButtonColor")
        self.pushButtonColor.setGeometry(QRect(70, 150, 211, 31))
        self.frameColor = QFrame(Dialog)
        self.frameColor.setObjectName(u"frameColor")
        self.frameColor.setGeometry(QRect(320, 90, 211, 151))
        self.frameColor.setFrameShape(QFrame.StyledPanel)
        self.frameColor.setFrameShadow(QFrame.Raised)
        self.labelColor = QLabel(Dialog)
        self.labelColor.setObjectName(u"labelColor")
        self.labelColor.setGeometry(QRect(360, 250, 121, 21))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButtonColor.setText(QCoreApplication.translate("Dialog", u"Choose color", None))
        self.labelColor.setText("")
    # retranslateUi

