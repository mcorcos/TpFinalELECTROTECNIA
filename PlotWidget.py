from PyQt5.QtWidgets import QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvas
import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as pl

class plotWidget():
    def __init__(self, parent = None):

        #QWidget.__init__(self,parent)

        self.fig = pl.figure()
        self.plot = FigureCanvas(self.fig)
        self.ax = self.fig.add_subplot()


    def bodeMod(self,H):

        self.ax.clear()
        w = np.logspace(-4,3,10000)
        ww , mag ,phase = signal.bode(H,w)
        self.ax.plot(ww,mag)
        self.ax.set_xlabel(r'w [$rad/s$] | log')
        self.ax.set_ylabel(r'|H(j$\omega$)| [dB]')
        self.ax.set_xscale('log')
        

        self.plot.draw()


    def bodePhase(self,H):

        self.ax.clear()
        w = np.logspace(-4,3,10000)
        ww , mag ,phase = signal.bode(H,w)
        self.ax.plot(ww,phase)
        self.ax.set_xlabel(r'w [$rad/s$] | log')
        self.ax.set_ylabel(r'H(j$\omega$) phase ')
        self.ax.set_xscale('log')
        
        self.plot.draw()


