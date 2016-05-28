# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from PyQt4 import QtGui
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar


class BarChart(QtGui.QDialog):
    """
        Implements mechanism for plotting of a bar chart for given data.
    """
    def __init__(self, bar_chart_name, ordinate_name, data_for_plotting, parent=None):
        """Make a instance of BarChart class.
        Args:
            bar_chart_name (str): It is a name of a bar chart.
            ordinate_name (str): It is a ordinate name of a bar chart.
            data_for_plotting (list): It is a data for plotting of a bar chart.
        """
        super(BarChart, self).__init__(parent)
        self.data = data_for_plotting
        self.graph_name = bar_chart_name
        self.ordinate_name = ordinate_name

        # a figure instance to plot on
        self.figure = plt.figure()

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)

        # set the layout
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)

        self.setLayout(layout)
        self.plot()

    def plot(self):
        """Plot a bar chart on the window's frame."""
        # create an axis
        ax = self.figure.add_subplot(111)

        # discards the old graph
        ax.hold(False)
        # del data[0]

        number = len(self.data)
        x = np.arange(1, number+1)
        y = [num for (s, num) in self.data]

        # labels = [ s for (s, num) in data ]
        width = 0.9
        self.figure = plt.bar(x, y, width, color="m")
        plt.title(self.graph_name)
        plt.ylabel(self.ordinate_name)
        plt.xlabel("Package emitting date")
        labels = [s for (s, num) in self.data]
        print self.data
        plt.xticks(x + width/2.0, labels)

        # refresh canvas
        self.canvas.draw()
