import sys

from PyQt5.QtWidgets import QApplication

from GUI import GUI

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = GUI()
    gui.MainWindow.show()
    sys.exit(app.exec_())




#Допилить систем расчетов