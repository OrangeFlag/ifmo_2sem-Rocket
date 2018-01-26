from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QMainWindow, QFileDialog, QAction, QWidget)
from Auto_GUI import Ui_MainWindow
from Parsers import Parse_Data_edit, Parse_Graph_edit
from Config import Config
import About_GUI
import Help_GUI


class GUI(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.MainWindow = QMainWindow()
        self.setupUi(self.MainWindow)
        self.Add()
    def Add(self):

        _translate = QCoreApplication.translate
        self.MainWindow.setWindowTitle("Rocket")
        self.Calculate.clicked.connect(self.Start_Modeling)
        self.Graph_count.activated[int].connect(self.Visible_graps)

        self.Graph_count.setCurrentIndex(0)
        self.First_Graph.setVisible(True)
        self.Sec_Graph.setVisible(False)
        self.Third_Graph.setVisible(False)
        self.Fourth_Graph.setVisible(False)
        self.Tab.setCurrentIndex(0)
        self.Conf_tab.setCurrentIndex(0)
        self.Graph_Help_text.setVisible(False)
        self.Graph_Help_button.clicked.connect(self.Visible_help)
        self.Graph_Help_button.setCheckable(True)

        self.Exit.triggered.connect(QCoreApplication.instance().quit)
        self.Save_config.triggered.connect(self.Save_conf)
        self.Save_config.setShortcut('Ctrl+s')
        self.Save_config.setShortcut('Ctrl+S')
        self.Save_config.setStatusTip('Save Config')
        self.Open_config.triggered.connect(self.Open_conf)
        self.Open_config.setShortcut('Ctrl+o')
        self.Open_config.setShortcut('Ctrl+O')
        self.Open_config.setStatusTip('Open Config')
        self.MainWindow.setWindowIcon(QIcon("./Roc_icon.png"))
        self.Save_config.setIcon(QIcon("./Save.png"))
        self.Open_config.setIcon(QIcon("./Open.png"))

        self.About = QAction(self.MainWindow)
        self.About.setObjectName("About")
        self.menubar.addAction(self.About)
        self.About.setText(_translate("MainWindow", "О программе"))
        self.About.triggered.connect(self.Show_About)


        self.menuHelp = QAction(self.MainWindow)
        self.menuHelp.setObjectName("menuHelp")
        self.menubar.addAction(self.menuHelp)
        self.menuHelp.setText(_translate("MainWindow", "&Help"))
        self.menuHelp.triggered.connect(self.Show_Help)
    def Show_Help(self):
        help = Help_GUI.Ui_Help()
        self.window_help = QWidget()
        help.setupUi(self.window_help)
        self.window_help.show()

    def Show_About(self):
        about = About_GUI.Ui_About()
        self.window_about = QWidget()
        about.setupUi(self.window_about)
        self.window_about.show()

    def Visible_help(self):
        self.Graph_Help_text.setVisible(not self.Graph_Help_text.isVisible())
    def Show_Percent(self, fl):
        self.statusbar.showMessage("Расчет " + str(round(fl*100)) + "%")



    def Visible_graps(self, int):
        if int == 0:
            self.First_Graph.setVisible(True)
            self.Sec_Graph.setVisible(False)
            self.Third_Graph.setVisible(False)
            self.Fourth_Graph.setVisible(False)
        elif int == 1:
            self.First_Graph.setVisible(True)
            self.Sec_Graph.setVisible(True)
            self.Third_Graph.setVisible(False)
            self.Fourth_Graph.setVisible(False)
        elif int == 2:
            self.First_Graph.setVisible(True)
            self.Sec_Graph.setVisible(True)
            self.Third_Graph.setVisible(True)
            self.Fourth_Graph.setVisible(True)

    def Start_Modeling(self):
        self.Graph_Help_text.setVisible(False)
        self.Graph_Help_button.setCheckable(False)
        self.Graph_Help_button.setCheckable(True)
        # заполнение конфига
        self.statusbar.showMessage("Распознавание данных")
        self.Make_config()
        self.statusbar.showMessage("Нормализация данных")
        self.Conf.Normalization_config()
        self.statusbar.showMessage("Расчет")
        try:
            self.Conf.Calculate()
        except BaseException:
            self.statusbar.showMessage("Ошибка при расчете")
            return
        else:
            self.statusbar.clearMessage()

        Graphs = [self.First_Graph, self.Sec_Graph, self.Third_Graph, self.Fourth_Graph]
        # парсинг переменных для каждого массива и вывод массивов
        for Graph in Graphs:
            line = str(Graph.edit.text()).replace(" ", '')
            if not line:
                continue
            try:
                x, y = Parse_Graph_edit(line, self.Conf)
            except BaseException:
                self.statusbar.showMessage("Ошибка в поле " + line)
                break
            Graph.plot(x, y, line.split(";")[0], line.split(";")[1]);
    def Make_config(self):
        self.Conf = Config()
        List_edit = [(self.Conf.t_mas, self.Time_edit, False), (self.Conf.Accuracy, self.Accurancy_edit, False),
                     (self.Conf.G, self.G_edit, False),
                     (self.Conf.m_rocket, self.m_rocket_edit, True),
                     (self.Conf.S_rocket, self.S_rocket_edit, True),
                     (self.Conf.distance, self.h_rocket_edit, False), (self.Conf.a_rocket, self.a_rocket_edit, False),
                     (self.Conf.u_rocket, self.u_rocket_edit, False),
                     (self.Conf.m_fuel, self.m_fuel_edit, True), (self.Conf.u_fuel, self.u_fuel_edit, True),
                     (self.Conf.c_fuel, self.c_fuel_edit, True), (self.Conf.M_planet, self.M_planet_edit, False),
                     (self.Conf.R_planet, self.R_planet_edit, False),
                     (self.Conf.Atmospher_density, self.P_atmos_edit, True),
                     (self.Conf.Coefficient_resistance, self.Coef_lob_spr_edit, True),
                     (self.Conf.Mol_gas, self.Mol_edit, True)]
        error_title = ""
        try:
            for var, edit, is_mas in List_edit:
                global error_title
                error_title = str(edit.text())
                edit = str(edit.text())
                if (edit == "Auto" or edit == "auto"):
                    var.clear()
                    var.append(1000)
                else:
                    Temp = Parse_Data_edit(edit, self.Conf, is_mas)
                    var.clear()
                    for x in Temp:
                        var.append(x)
            error_title = str(self.Temper_edit.text())
            self.Conf.Temperature.clear()
            self.Conf.Temperature.append(str(self.Temper_edit.text()).split(';')[0])
        except BaseException:
            self.statusbar.showMessage("Ошибка в поле " + error_title)
        else:
            self.statusbar.clearMessage()

    def Save_conf(self):
        fname = QFileDialog.getSaveFileName(self.MainWindow, 'Save file', '*.mdr')[0]
        f = open(fname, 'w')
        List_edit = [self.Time_edit, self.Accurancy_edit,
                     self.G_edit,
                     self.m_rocket_edit,
                     self.S_rocket_edit,
                     self.h_rocket_edit, self.a_rocket_edit,
                     self.u_rocket_edit,
                     self.m_fuel_edit, self.u_fuel_edit,
                     self.c_fuel_edit, self.M_planet_edit,
                     self.R_planet_edit,
                     self.P_atmos_edit,
                     self.Coef_lob_spr_edit,
                     self.Mol_edit,
                     self.Temper_edit]
        for edit in List_edit:
            f.write(str(edit.objectName())+ " " +str(edit.text()) + '\n')
        f.write(str(self.AboutConfig.toPlainText()))
        f.close()


    def Open_conf(self):
        fname = QFileDialog.getOpenFileName(self.MainWindow, 'Open file', '.mdr')[0]
        f = open(fname, 'r')
        List_edit = [self.Time_edit, self.Accurancy_edit,
                     self.G_edit,
                     self.m_rocket_edit,
                     self.S_rocket_edit,
                     self.h_rocket_edit, self.a_rocket_edit,
                     self.u_rocket_edit,
                     self.m_fuel_edit, self.u_fuel_edit,
                     self.c_fuel_edit, self.M_planet_edit,
                     self.R_planet_edit,
                     self.P_atmos_edit,
                     self.Coef_lob_spr_edit,
                     self.Mol_edit,
                     self.Temper_edit]
        for edit in List_edit:
            line = f.readline()
            line = line.replace("\n", '')
            line = line.split(' ')
            edit.setText(line[1])
        about = f.read()
        self.AboutConfig.setText(about)
        f.close()

