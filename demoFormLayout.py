# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'demoFormLayout.ui'
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
        Dialog.resize(400, 195)
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(90, 32, 216, 141))
        self.formLayout = QFormLayout(self.widget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label)

        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_2)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMaximumSize(QSize(120, 16777215))

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.pushButton_2)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(120, 16777215))

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.pushButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(1, QFormLayout.FieldRole, self.verticalSpacer)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(3, QFormLayout.FieldRole, self.verticalSpacer_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Name", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Email Address", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Submit", None))
    # retranslateUi

