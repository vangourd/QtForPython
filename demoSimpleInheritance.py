# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'demoSimpleInheritance.ui'
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
        Dialog.resize(400, 300)
        self.ButtonClickMe = QPushButton(Dialog)
        self.ButtonClickMe.setObjectName(u"ButtonClickMe")
        self.ButtonClickMe.setGeometry(QRect(150, 250, 88, 27))
        self.labelResponse = QLabel(Dialog)
        self.labelResponse.setObjectName(u"labelResponse")
        self.labelResponse.setGeometry(QRect(7, 194, 381, 51))
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 20, 341, 161))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEditCode = QLineEdit(self.widget)
        self.lineEditCode.setObjectName(u"lineEditCode")

        self.horizontalLayout.addWidget(self.lineEditCode)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEditName = QLineEdit(self.widget)
        self.lineEditName.setObjectName(u"lineEditName")

        self.horizontalLayout_2.addWidget(self.lineEditName)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.lineEditHistory = QLineEdit(self.widget)
        self.lineEditHistory.setObjectName(u"lineEditHistory")

        self.horizontalLayout_3.addWidget(self.lineEditHistory)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.lineEditGeo = QLineEdit(self.widget)
        self.lineEditGeo.setObjectName(u"lineEditGeo")

        self.horizontalLayout_4.addWidget(self.lineEditGeo)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.ButtonClickMe.setText(QCoreApplication.translate("Dialog", u"Click", None))
        self.labelResponse.setText("")
        self.label.setText(QCoreApplication.translate("Dialog", u"Student Code", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Student Name", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"History Marks", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Geography Marks", None))
    # retranslateUi

