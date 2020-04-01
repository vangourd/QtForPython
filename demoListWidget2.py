# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'demoListWidget2.ui'
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
        Dialog.resize(745, 525)
        self.listWidgetDiagnosis = QListWidget(Dialog)
        QListWidgetItem(self.listWidgetDiagnosis)
        QListWidgetItem(self.listWidgetDiagnosis)
        QListWidgetItem(self.listWidgetDiagnosis)
        QListWidgetItem(self.listWidgetDiagnosis)
        QListWidgetItem(self.listWidgetDiagnosis)
        self.listWidgetDiagnosis.setObjectName(u"listWidgetDiagnosis")
        self.listWidgetDiagnosis.setGeometry(QRect(155, 40, 341, 192))
        self.listWidgetDiagnosis.setSelectionMode(QAbstractItemView.MultiSelection)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 50, 121, 19))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 309, 141, 20))
        self.listWidgetSelectedTests = QListWidget(Dialog)
        self.listWidgetSelectedTests.setObjectName(u"listWidgetSelectedTests")
        self.listWidgetSelectedTests.setGeometry(QRect(150, 300, 341, 192))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))

        __sortingEnabled = self.listWidgetDiagnosis.isSortingEnabled()
        self.listWidgetDiagnosis.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidgetDiagnosis.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Dialog", u"Urine Analysis $5", None));
        ___qlistwidgetitem1 = self.listWidgetDiagnosis.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Dialog", u"Chest X Ray $100", None));
        ___qlistwidgetitem2 = self.listWidgetDiagnosis.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("Dialog", u"Sugar Level Test $3", None));
        ___qlistwidgetitem3 = self.listWidgetDiagnosis.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("Dialog", u"Hemoglobin Test $7", None));
        ___qlistwidgetitem4 = self.listWidgetDiagnosis.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("Dialog", u"Thyroid Stimulating Hormone Test $10", None));
        self.listWidgetDiagnosis.setSortingEnabled(__sortingEnabled)

        self.label.setText(QCoreApplication.translate("Dialog", u"Available Tests", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Selected tests are", None))
    # retranslateUi

