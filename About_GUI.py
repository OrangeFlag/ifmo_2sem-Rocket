# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './About.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5.QtWidgets import QGridLayout, QLabel
from PyQt5.QtCore import QMetaObject, QCoreApplication

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(400, 300)
        self.gridLayout = QGridLayout(About)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QLabel(About)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QLabel(About)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.retranslateUi(About)
        QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        _translate = QCoreApplication.translate
        About.setWindowTitle(_translate("About", "Form"))
        self.label_2.setText(_translate("About", "Make by © IS"))

