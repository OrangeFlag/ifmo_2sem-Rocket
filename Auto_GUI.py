# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Gui.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import QGridLayout, QLabel, QWidget, QTabWidget, QLayout, QTextEdit, QLineEdit, QSpacerItem, \
    QSizePolicy, QPushButton, QComboBox, QTextBrowser, QStatusBar, QMenuBar, QAction, QMenu
from PyQt5.QtCore import QMetaObject, QCoreApplication, Qt, QSize, QRect

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(809, 868)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Tab = QTabWidget(self.centralwidget)
        self.Tab.setObjectName("Tab")
        self.Conf = QWidget()
        self.Conf.setObjectName("Conf")
        self.gridLayout_5 = QGridLayout(self.Conf)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.Conf_tab = QTabWidget(self.Conf)
        self.Conf_tab.setTabBarAutoHide(True)
        self.Conf_tab.setObjectName("Conf_tab")
        self.Conf_const = QWidget()
        self.Conf_const.setObjectName("Conf_const")
        self.gridLayout_4 = QGridLayout(self.Conf_const)
        self.gridLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.AboutConfig = QTextEdit(self.Conf_const)
        self.AboutConfig.setObjectName("AboutConfig")
        self.gridLayout_4.addWidget(self.AboutConfig, 3, 1, 1, 1)
        spacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem, 5, 0, 1, 2)
        self.Accurancy_edit = QLineEdit(self.Conf_const)
        self.Accurancy_edit.setObjectName("Accurancy_edit")
        self.gridLayout_4.addWidget(self.Accurancy_edit, 1, 1, 1, 1)
        self.Time_label = QLabel(self.Conf_const)
        self.Time_label.setObjectName("Time_label")
        self.gridLayout_4.addWidget(self.Time_label, 0, 0, 1, 1)
        self.Accurancy_label = QLabel(self.Conf_const)
        self.Accurancy_label.setObjectName("Accurancy_label")
        self.gridLayout_4.addWidget(self.Accurancy_label, 1, 0, 1, 1)
        self.G_edit = QLineEdit(self.Conf_const)
        self.G_edit.setObjectName("G_edit")
        self.gridLayout_4.addWidget(self.G_edit, 2, 1, 1, 1)
        self.Time_edit = QLineEdit(self.Conf_const)
        self.Time_edit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.Time_edit.setClearButtonEnabled(False)
        self.Time_edit.setObjectName("Time_edit")
        self.gridLayout_4.addWidget(self.Time_edit, 0, 1, 1, 1)
        self.label = QLabel(self.Conf_const)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 3, 0, 1, 1)
        self.G_label = QLabel(self.Conf_const)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.G_label.sizePolicy().hasHeightForWidth())
        self.G_label.setSizePolicy(sizePolicy)
        self.G_label.setObjectName("G_label")
        self.gridLayout_4.addWidget(self.G_label, 2, 0, 1, 1)
        self.Conf_tab.addTab(self.Conf_const, "")
        self.Conf_rocket = QWidget()
        self.Conf_rocket.setObjectName("Conf_rocket")
        self.gridLayout_7 = QGridLayout(self.Conf_rocket)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.a_rocket_label = QLabel(self.Conf_rocket)
        self.a_rocket_label.setObjectName("a_rocket_label")
        self.gridLayout_7.addWidget(self.a_rocket_label, 15, 0, 1, 1)
        self.u_rocket_edit = QLineEdit(self.Conf_rocket)
        self.u_rocket_edit.setObjectName("u_rocket_edit")
        self.gridLayout_7.addWidget(self.u_rocket_edit, 14, 1, 1, 1)
        self.h_rocket_edit = QLineEdit(self.Conf_rocket)
        self.h_rocket_edit.setObjectName("h_rocket_edit")
        self.gridLayout_7.addWidget(self.h_rocket_edit, 13, 1, 1, 1)
        self.S_rocket_edit = QLineEdit(self.Conf_rocket)
        self.S_rocket_edit.setObjectName("S_rocket_edit")
        self.gridLayout_7.addWidget(self.S_rocket_edit, 3, 1, 1, 1)
        spacerItem1 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem1, 16, 0, 1, 2)
        self.m_rocket_edit = QLineEdit(self.Conf_rocket)
        self.m_rocket_edit.setObjectName("m_rocket_edit")
        self.gridLayout_7.addWidget(self.m_rocket_edit, 2, 1, 1, 1)
        self.c_fuel_label = QLabel(self.Conf_rocket)
        self.c_fuel_label.setObjectName("c_fuel_label")
        self.gridLayout_7.addWidget(self.c_fuel_label, 9, 0, 1, 1)
        self.u_fuel_label = QLabel(self.Conf_rocket)
        self.u_fuel_label.setObjectName("u_fuel_label")
        self.gridLayout_7.addWidget(self.u_fuel_label, 8, 0, 1, 1)
        self.m_fuel_label = QLabel(self.Conf_rocket)
        self.m_fuel_label.setObjectName("m_fuel_label")
        self.gridLayout_7.addWidget(self.m_fuel_label, 7, 0, 1, 1)
        self.c_fuel_edit = QLineEdit(self.Conf_rocket)
        self.c_fuel_edit.setObjectName("c_fuel_edit")
        self.gridLayout_7.addWidget(self.c_fuel_edit, 9, 1, 1, 1)
        self.u_fuel_edit = QLineEdit(self.Conf_rocket)
        self.u_fuel_edit.setObjectName("u_fuel_edit")
        self.gridLayout_7.addWidget(self.u_fuel_edit, 8, 1, 1, 1)
        self.m_fuel_edit = QLineEdit(self.Conf_rocket)
        self.m_fuel_edit.setObjectName("m_fuel_edit")
        self.gridLayout_7.addWidget(self.m_fuel_edit, 7, 1, 1, 1)
        self.m_rocket_label = QLabel(self.Conf_rocket)
        self.m_rocket_label.setObjectName("m_rocket_label")
        self.gridLayout_7.addWidget(self.m_rocket_label, 2, 0, 1, 1)
        self.S_rocket_label = QLabel(self.Conf_rocket)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.S_rocket_label.sizePolicy().hasHeightForWidth())
        self.S_rocket_label.setSizePolicy(sizePolicy)
        self.S_rocket_label.setObjectName("S_rocket_label")
        self.gridLayout_7.addWidget(self.S_rocket_label, 3, 0, 1, 1)
        self.a_rocket_edit = QLineEdit(self.Conf_rocket)
        self.a_rocket_edit.setObjectName("a_rocket_edit")
        self.gridLayout_7.addWidget(self.a_rocket_edit, 15, 1, 1, 1)
        self.h_rocket_label = QLabel(self.Conf_rocket)
        self.h_rocket_label.setObjectName("h_rocket_label")
        self.gridLayout_7.addWidget(self.h_rocket_label, 13, 0, 1, 1)
        self.u_rocket_label = QLabel(self.Conf_rocket)
        self.u_rocket_label.setObjectName("u_rocket_label")
        self.gridLayout_7.addWidget(self.u_rocket_label, 14, 0, 1, 1)
        spacerItem2 = QSpacerItem(40, 5, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem2, 11, 0, 1, 1)
        self.label_2 = QLabel(self.Conf_rocket)
        self.label_2.setObjectName("label_2")
        self.gridLayout_7.addWidget(self.label_2, 12, 0, 1, 1)
        self.Coef_lob_spr_label = QLabel(self.Conf_rocket)
        self.Coef_lob_spr_label.setObjectName("Coef_lob_spr_label")
        self.gridLayout_7.addWidget(self.Coef_lob_spr_label, 10, 0, 1, 1)
        self.Coef_lob_spr_edit = QLineEdit(self.Conf_rocket)
        self.Coef_lob_spr_edit.setObjectName("Coef_lob_spr_edit")
        self.gridLayout_7.addWidget(self.Coef_lob_spr_edit, 10, 1, 1, 1)
        self.Conf_tab.addTab(self.Conf_rocket, "")
        self.Conf_planet = QWidget()
        self.Conf_planet.setObjectName("Conf_planet")
        self.gridLayout_8 = QGridLayout(self.Conf_planet)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.widget = QWidget(self.Conf_planet)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.M_planet_label = QLabel(self.widget)
        self.M_planet_label.setObjectName("M_planet_label")
        self.gridLayout_2.addWidget(self.M_planet_label, 0, 0, 1, 1)
        self.P_atmos_label = QLabel(self.widget)
        self.P_atmos_label.setObjectName("P_atmos_label")
        self.gridLayout_2.addWidget(self.P_atmos_label, 2, 0, 1, 1)
        self.M_planet_edit = QLineEdit(self.widget)
        self.M_planet_edit.setObjectName("M_planet_edit")
        self.gridLayout_2.addWidget(self.M_planet_edit, 0, 1, 1, 1)
        self.P_atmos_edit = QLineEdit(self.widget)
        self.P_atmos_edit.setObjectName("P_atmos_edit")
        self.gridLayout_2.addWidget(self.P_atmos_edit, 2, 1, 1, 1)
        self.R_planet_edit = QLineEdit(self.widget)
        self.R_planet_edit.setObjectName("R_planet_edit")
        self.gridLayout_2.addWidget(self.R_planet_edit, 1, 1, 1, 1)
        self.R_planet_label = QLabel(self.widget)
        self.R_planet_label.setObjectName("R_planet_label")
        self.gridLayout_2.addWidget(self.R_planet_label, 1, 0, 1, 1)
        self.Mol_label = QLabel(self.widget)
        self.Mol_label.setObjectName("Mol_label")
        self.gridLayout_2.addWidget(self.Mol_label, 3, 0, 1, 1)
        self.Temper_label = QLabel(self.widget)
        self.Temper_label.setObjectName("Temper_label")
        self.gridLayout_2.addWidget(self.Temper_label, 4, 0, 1, 1)
        self.Mol_edit = QLineEdit(self.widget)
        self.Mol_edit.setObjectName("Mol_edit")
        self.gridLayout_2.addWidget(self.Mol_edit, 3, 1, 1, 1)
        self.Temper_edit = QLineEdit(self.widget)
        self.Temper_edit.setObjectName("Temper_edit")
        self.gridLayout_2.addWidget(self.Temper_edit, 4, 1, 1, 1)
        self.M_planet_label.raise_()
        self.M_planet_edit.raise_()
        self.R_planet_label.raise_()
        self.R_planet_edit.raise_()
        self.P_atmos_label.raise_()
        self.P_atmos_edit.raise_()
        self.Mol_label.raise_()
        self.Temper_label.raise_()
        self.Mol_edit.raise_()
        self.Temper_edit.raise_()
        self.gridLayout_8.addWidget(self.widget, 5, 0, 1, 2)
        spacerItem3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem3, 6, 0, 1, 2)
        self.Conf_tab.addTab(self.Conf_planet, "")
        self.gridLayout_5.addWidget(self.Conf_tab, 0, 0, 1, 1)
        self.Tab.addTab(self.Conf, "")
        self.Modelir = QWidget()
        self.Modelir.setObjectName("Modelir")
        self.gridLayout_6 = QGridLayout(self.Modelir)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.Fourth_Graph = Graph(self.Modelir)
        self.Fourth_Graph.setObjectName("Fourth_Graph")
        self.gridLayout_6.addWidget(self.Fourth_Graph, 3, 0, 1, 1)
        self.First_Graph = Graph(self.Modelir)
        self.First_Graph.setObjectName("First_Graph")
        self.gridLayout_6.addWidget(self.First_Graph, 0, 0, 1, 1)
        self.Calculate = QPushButton(self.Modelir)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Calculate.sizePolicy().hasHeightForWidth())
        self.Calculate.setSizePolicy(sizePolicy)
        self.Calculate.setObjectName("Calculate")
        self.gridLayout_6.addWidget(self.Calculate, 7, 0, 1, 2)
        self.Sec_Graph = Graph(self.Modelir)
        self.Sec_Graph.setObjectName("Sec_Graph")
        self.gridLayout_6.addWidget(self.Sec_Graph, 0, 1, 1, 1)
        self.Third_Graph = Graph(self.Modelir)
        self.Third_Graph.setObjectName("Third_Graph")
        self.gridLayout_6.addWidget(self.Third_Graph, 3, 1, 1, 1)
        self.Graph_settings = QWidget(self.Modelir)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Graph_settings.sizePolicy().hasHeightForWidth())
        self.Graph_settings.setSizePolicy(sizePolicy)
        self.Graph_settings.setObjectName("Graph_settings")
        self.gridLayout = QGridLayout(self.Graph_settings)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Graph_Help_button = QPushButton(self.Graph_settings)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Graph_Help_button.sizePolicy().hasHeightForWidth())
        self.Graph_Help_button.setSizePolicy(sizePolicy)
        self.Graph_Help_button.setObjectName("Graph_Help_button")
        self.gridLayout.addWidget(self.Graph_Help_button, 0, 2, 1, 1)
        self.Graph_count_label = QLabel(self.Graph_settings)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Graph_count_label.sizePolicy().hasHeightForWidth())
        self.Graph_count_label.setSizePolicy(sizePolicy)
        self.Graph_count_label.setObjectName("Graph_count_label")
        self.gridLayout.addWidget(self.Graph_count_label, 0, 0, 1, 1)
        self.Graph_count = QComboBox(self.Graph_settings)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Graph_count.sizePolicy().hasHeightForWidth())
        self.Graph_count.setSizePolicy(sizePolicy)
        self.Graph_count.setEditable(False)
        self.Graph_count.setObjectName("Graph_count")
        self.Graph_count.addItem("")
        self.Graph_count.addItem("")
        self.Graph_count.addItem("")
        self.gridLayout.addWidget(self.Graph_count, 0, 1, 1, 1)
        self.gridLayout_6.addWidget(self.Graph_settings, 4, 0, 1, 2)
        self.Graph_Help_text = QTextBrowser(self.Modelir)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Graph_Help_text.sizePolicy().hasHeightForWidth())
        self.Graph_Help_text.setSizePolicy(sizePolicy)
        self.Graph_Help_text.setMinimumSize(QSize(0, 350))
        self.Graph_Help_text.setMaximumSize(QSize(16777215, 350))
        self.Graph_Help_text.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.Graph_Help_text.setTabStopWidth(100)
        self.Graph_Help_text.setObjectName("Graph_Help_text")
        self.gridLayout_6.addWidget(self.Graph_Help_text, 5, 0, 1, 2)
        self.Tab.addTab(self.Modelir, "")
        self.gridLayout_3.addWidget(self.Tab, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 809, 22))
        self.menubar.setNativeMenuBar(False)
        self.menubar.setObjectName("menubar")
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.Save_config = QAction(MainWindow)
        self.Save_config.setObjectName("Save_config")
        self.Exit = QAction(MainWindow)
        self.Exit.setObjectName("Exit")
        self.Open_config = QAction(MainWindow)
        self.Open_config.setObjectName("Open_config")
        self.menu.addAction(self.Save_config)
        self.menu.addAction(self.Open_config)
        self.menu.addSeparator()
        self.menu.addAction(self.Exit)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.Tab.setCurrentIndex(1)
        self.Conf_tab.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.Tab, self.Time_edit)
        MainWindow.setTabOrder(self.Time_edit, self.Accurancy_edit)
        MainWindow.setTabOrder(self.Accurancy_edit, self.G_edit)
        MainWindow.setTabOrder(self.G_edit, self.AboutConfig)
        MainWindow.setTabOrder(self.AboutConfig, self.m_rocket_edit)
        MainWindow.setTabOrder(self.m_rocket_edit, self.S_rocket_edit)
        MainWindow.setTabOrder(self.S_rocket_edit, self.m_fuel_edit)
        MainWindow.setTabOrder(self.m_fuel_edit, self.u_fuel_edit)
        MainWindow.setTabOrder(self.u_fuel_edit, self.c_fuel_edit)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.AboutConfig.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Запуск ракетоносителя Falcon 9 с поверхности земли</p></body></html>"))
        self.Accurancy_edit.setText(_translate("MainWindow", "0.1"))
        self.Time_label.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.Time_label.setText(_translate("MainWindow", "t, c"))
        self.Accurancy_label.setText(_translate("MainWindow", "Точность (0.01-10)"))
        self.G_edit.setToolTip(_translate("MainWindow", "<html><head/><body><p>Н*м^2*кг^-2</p></body></html>"))
        self.G_edit.setText(_translate("MainWindow", "6.6740831313131/10^11"))
        self.Time_edit.setToolTip(_translate("MainWindow", "<html><head/><body><p>с</p></body></html>"))
        self.Time_edit.setText(_translate("MainWindow", "Auto"))
        self.label.setText(_translate("MainWindow", "Описание"))
        self.G_label.setText(_translate("MainWindow", "G, Н*м^2/кг^2"))
        self.Conf_tab.setTabText(self.Conf_tab.indexOf(self.Conf_const), _translate("MainWindow", "Общая"))
        self.a_rocket_label.setText(_translate("MainWindow", "Начальное ускорение, м/с^2"))
        self.u_rocket_edit.setToolTip(_translate("MainWindow", "<html><head/><body><p>м/с</p></body></html>"))
        self.u_rocket_edit.setText(_translate("MainWindow", "0"))
        self.h_rocket_edit.setToolTip(_translate("MainWindow", "<html><head/><body><p>м</p></body></html>"))
        self.h_rocket_edit.setText(_translate("MainWindow", "0"))
        self.S_rocket_edit.setToolTip(_translate("MainWindow", "<html><head/><body><p>м^2</p></body></html>"))
        self.S_rocket_edit.setText(_translate("MainWindow", "pi*(3.7/2)^2"))
        self.m_rocket_edit.setToolTip(_translate("MainWindow", "<html><head/><body><p>кг</p></body></html>"))
        self.m_rocket_edit.setText(_translate("MainWindow", "22*10^3"))
        self.c_fuel_label.setText(_translate("MainWindow", "Расход топлива, кг/с"))
        self.u_fuel_label.setText(_translate("MainWindow", "Скорость истечения топлива, м/с"))
        self.m_fuel_label.setText(_translate("MainWindow", "Начальная масса топлива, кг"))
        self.c_fuel_edit.setToolTip(_translate("MainWindow", "<html><head/><body><p>кг/с</p></body></html>"))
        self.c_fuel_edit.setText(_translate("MainWindow", "10^3"))
        self.u_fuel_edit.setToolTip(_translate("MainWindow", "<html><head/><body><p>м/с</p></body></html>"))
        self.u_fuel_edit.setText(_translate("MainWindow", "8000"))
        self.m_fuel_edit.setToolTip(_translate("MainWindow", "<html><head/><body><p>кг</p></body></html>"))
        self.m_fuel_edit.setText(_translate("MainWindow", "500*10^3"))
        self.m_rocket_label.setText(_translate("MainWindow", "Масса, кг"))
        self.S_rocket_label.setText(_translate("MainWindow", "Площадь сечения, м^2"))
        self.a_rocket_edit.setToolTip(_translate("MainWindow", "<html><head/><body><p>м/с^2</p></body></html>"))
        self.a_rocket_edit.setText(_translate("MainWindow", "0"))
        self.h_rocket_label.setText(_translate("MainWindow", "<html><head/><body><p>Начальная высота полета, м</p></body></html>"))
        self.u_rocket_label.setText(_translate("MainWindow", "Начальная скорость, м/с"))
        self.label_2.setText(_translate("MainWindow", "Необязательные параметры:"))
        self.Coef_lob_spr_label.setText(_translate("MainWindow", "Коэффицент лобового сопротивления"))
        self.Coef_lob_spr_edit.setText(_translate("MainWindow", "0.30"))
        self.Conf_tab.setTabText(self.Conf_tab.indexOf(self.Conf_rocket), _translate("MainWindow", "Тело"))
        self.M_planet_label.setToolTip(_translate("MainWindow", "<html><head/><body><p>кг</p></body></html>"))
        self.M_planet_label.setText(_translate("MainWindow", "Масса, кг"))
        self.P_atmos_label.setText(_translate("MainWindow", "Плотность атмосферы на нулевой высоте, кг/м^3"))
        self.M_planet_edit.setToolTip(_translate("MainWindow", "<html><head/><body><p>кг</p></body></html>"))
        self.M_planet_edit.setText(_translate("MainWindow", "5.97*10^24"))
        self.P_atmos_edit.setToolTip(_translate("MainWindow", "<html><head/><body><p>кг/м^3</p></body></html>"))
        self.P_atmos_edit.setText(_translate("MainWindow", "1.1455"))
        self.R_planet_edit.setToolTip(_translate("MainWindow", "<html><head/><body><p>м</p></body></html>"))
        self.R_planet_edit.setText(_translate("MainWindow", "6371*10^3"))
        self.R_planet_label.setText(_translate("MainWindow", "Радиус, м"))
        self.Mol_label.setText(_translate("MainWindow", "Молярная масса газа, моль"))
        self.Temper_label.setText(_translate("MainWindow", "Функция температуры, К"))
        self.Mol_edit.setText(_translate("MainWindow", "29.04"))
        self.Temper_edit.setText(_translate("MainWindow", "280-0.3*h"))
        self.Conf_tab.setTabText(self.Conf_tab.indexOf(self.Conf_planet), _translate("MainWindow", "Планета"))
        self.Tab.setTabText(self.Tab.indexOf(self.Conf), _translate("MainWindow", "Конфигурация"))
        self.Calculate.setText(_translate("MainWindow", "Начать моделирование"))
        self.Graph_Help_button.setText(_translate("MainWindow", "?"))
        self.Graph_count_label.setText(_translate("MainWindow", "Кол-во графиков"))
        self.Graph_count.setItemText(0, _translate("MainWindow", "1"))
        self.Graph_count.setItemText(1, _translate("MainWindow", "2"))
        self.Graph_count.setItemText(2, _translate("MainWindow", "4"))
        self.Graph_Help_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Для ввода функций допустимо использовать следующие операции <span style=\" font-weight:600; color:#ff0000;\">+</span>, <span style=\" font-weight:600; color:#ff0000;\">-</span>, <span style=\" font-weight:600; font-style:italic; color:#ff0000;\">*</span>, <span style=\" font-weight:600; color:#ff0000;\">/</span>, <span style=\" font-weight:600; color:#ff0000;\">^</span>.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Динамические переменные:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#ff0000;\">t</span><span style=\" color:#000000;\"> - время</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#ff0000;\">m_r </span><span style=\" color:#000000;\">- чистая масса ракеты</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#ff0000;\">h</span><span style=\" color:#000000;\"> - расстояние от точки запуска</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#ff0000;\">a_r</span><span style=\" color:#000000;\"> - ускорение ракеты</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#ff0000;\">u_r </span><span style=\" color:#000000;\">- скорость ракеты</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#ff0000;\">m_f </span><span style=\" color:#000000;\">- масса топлива</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#ff0000;\">u_f</span><span style=\" color:#000000;\"> - скорость истечения топлива</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#ff0000;\">c_f </span><span style=\" color:#000000;\">- расход топлива</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#ff0000;\">p_a</span><span style=\" color:#000000;\"> - плотность атмосферы</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#ff0000;\">C_r</span><span style=\" color:#000000;\"> - коэффицент лобового сопротивления</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#ff0000;\">s_r</span><span style=\" color:#000000;\"> - площадь сечения ракеты</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#ef2929;\">Mol_A</span><span style=\" color:#000000;\"> - молярна масса газа</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#ef2929;\">T_A</span><span style=\" color:#000000;\"> - температура атмосферы</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Постоянные:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#ff0000;\">G</span> - гравитационная постоянная</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#ff0000;\">M_P</span> - масса планеты</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#ff0000;\">R_P</span> - радиус планеты</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#ff0000;\">pi</span> - 3,14...</p></body></html>"))
        self.Tab.setTabText(self.Tab.indexOf(self.Modelir), _translate("MainWindow", "Моделирование"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.Save_config.setText(_translate("MainWindow", "Сохранить кофигурацию"))
        self.Exit.setText(_translate("MainWindow", "Выйти"))
        self.Open_config.setText(_translate("MainWindow", "Загрузить конфигурацию"))

from GUI_Graph import Graph