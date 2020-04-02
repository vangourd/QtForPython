# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'demoMultiLevelInheritance.ui'
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
        Dialog.resize(404, 340)
        self.ButtonClickMe = QPushButton(Dialog)
        self.ButtonClickMe.setObjectName(u"ButtonClickMe")
        self.ButtonClickMe.setGeometry(QRect(150, 290, 88, 27))
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(24, 23, 361, 241))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEditCode = QLineEdit(self.layoutWidget)
        self.lineEditCode.setObjectName(u"lineEditCode")

        self.horizontalLayout.addWidget(self.lineEditCode)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEditName = QLineEdit(self.layoutWidget)
        self.lineEditName.setObjectName(u"lineEditName")

        self.horizontalLayout_2.addWidget(self.lineEditName)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.lineEditHistory = QLineEdit(self.layoutWidget)
        self.lineEditHistory.setObjectName(u"lineEditHistory")

        self.horizontalLayout_3.addWidget(self.lineEditHistory)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.lineEditGeographyMarks = QLineEdit(self.layoutWidget)
        self.lineEditGeographyMarks.setObjectName(u"lineEditGeographyMarks")

        self.horizontalLayout_4.addWidget(self.lineEditGeographyMarks)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.lineEditTotal = QLineEdit(self.layoutWidget)
        self.lineEditTotal.setObjectName(u"lineEditTotal")
        self.lineEditTotal.setEnabled(False)

        self.horizontalLayout_6.addWidget(self.lineEditTotal)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.lineEditPercentage = QLineEdit(self.layoutWidget)
        self.lineEditPercentage.setObjectName(u"lineEditPercentage")
        self.lineEditPercentage.setEnabled(False)

        self.horizontalLayout_5.addWidget(self.lineEditPercentage)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.ButtonClickMe.setText(QCoreApplication.translate("Dialog", u"Click", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Student Code", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Student Name", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"History Marks", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Geography Marks", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Total", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Percentage", None))
    # retranslateUi

