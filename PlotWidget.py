from ctypes import resize
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
        return


    def bodePhase(self,H):

        self.ax.clear()
        w = np.logspace(-4,3,10000)
        ww , mag ,phase = signal.bode(H,w)
        self.ax.plot(ww,phase)
        self.ax.set_xlabel(r'w [$rad/s$] | log')
        self.ax.set_ylabel(r'H(j$\omega$) phase ')
        self.ax.set_xscale('log')
        
        self.plot.draw()
        return



    def plotFilteredSignal(self,H,u,t,):


        self.ax.clear()
        if(H):
            response = signal.lsim( H.tf , U = u , T = t)
            self.ax.plot(response[0],response[1])
        else:
            self.ax.plot(t,u)


        self.plot.draw()

        return

    def plotResponse(self,H):


        self.ax.clear()
        self.ax.plot(H[0],H[1])
        self.plot.draw()

        return


    def plotZP(self, H):

        self.ax.clear()
        if(H):
            Z= H.zeros
            P = H.poles
            reZ = np.real(Z)
            imgZ = np.imag(Z)
            reP = np.real(P)
            imgP = np.imag(P)

            self.ax.scatter(reZ, imgZ , c="r", marker="o")
            self.ax.scatter(reP, imgP , c="g", marker="X")
            self.ax.set_ylabel(r'$|jw|$')
            self.ax.set_xlabel(r'$\sigma$')
            self.ax.set_title('Polos y Ceros')

        self.ax.grid(True)
        self.plot.draw()