
from PyQt5.QtWidgets import QWidget, QLineEdit, QVBoxLayout

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt


class Graph(QWidget):
    def __init__(self, parent=None):
        super(Graph, self).__init__(parent)

        # a figure instance to plot on
        self.Plt = plt
        self.figure = self.Plt.figure()

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)

        # Just some button connected to `plot` method
        self.edit = QLineEdit()

        # set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        layout.addWidget(self.edit)
        self.setLayout(layout)

    def plot(self, x, y, x_label, y_label):
        ''' plot some random stuff '''
        # random data

        # instead of ax.hold(False)
        self.figure.clear()

        # create an axis
        ax = self.figure.add_subplot(111)
        ax.grid(True)
        ax.plot(x, y, label=x_label + ' / ' + y_label)
        ax.legend(loc='best')
        # discards the old graph
        # ax.hold(False) # deprecated, see above

        # refresh canvas
        self.canvas.draw()