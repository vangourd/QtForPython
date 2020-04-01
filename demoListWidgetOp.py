# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'demoListWidgetOp.ui'
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
        Dialog.resize(734, 386)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 60, 111, 21))
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(130, 60, 251, 25))
        self.pushButtonAdd = QPushButton(Dialog)
        self.pushButtonAdd.setObjectName(u"pushButtonAdd")
        self.pushButtonAdd.setGeometry(QRect(210, 100, 88, 27))
        self.listWidget = QListWidget(Dialog)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(440, 40, 256, 192))
        self.pushButtonEdit = QPushButton(Dialog)
        self.pushButtonEdit.setObjectName(u"pushButtonEdit")
        self.pushButtonEdit.setGeometry(QRect(430, 250, 88, 27))
        self.pushButtonDelete = QPushButton(Dialog)
        self.pushButtonDelete.setObjectName(u"pushButtonDelete")
        self.pushButtonDelete.setGeometry(QRect(530, 250, 88, 27))
        self.pushButtonDeleteAll = QPushButton(Dialog)
        self.pushButtonDeleteAll.setObjectName(u"pushButtonDeleteAll")
        self.pushButtonDeleteAll.setGeometry(QRect(630, 250, 88, 27))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Enter an item", None))
        self.pushButtonAdd.setText(QCoreApplication.translate("Dialog", u"Add", None))
        self.pushButtonEdit.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.pushButtonDelete.setText(QCoreApplication.translate("Dialog", u"Delete", None))
        self.pushButtonDeleteAll.setText(QCoreApplication.translate("Dialog", u"Delete All", None))
    # retranslateUi

