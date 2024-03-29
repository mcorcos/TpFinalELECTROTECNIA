import sys

from PyQt5 import QtWidgets, uic
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy import signal
from scipy.fft import ifft
from PlotWidget import plotWidget



def convertToFloat(x):
    last = x[-1]
    multiplier = 1.0
    if(last.isalpha()):
        x = x[0:-1] #saco la letra del multiplo
        if last == 'p':
            multiplier *= 1e-12
        if last == 'n':
            multiplier *= 1e-9
        if last == 'u':
            multiplier *= 1e-6
        if last == 'm':
            multiplier *= 1e-3
        if last == 'k':
            multiplier *= 1e3
        if last == 'M':
            multiplier *= 1e6
        if last == 'G':
            multiplier *= 1e9
        if last == 'T':
            multiplier *= 1e12
    
    res = np.nan
    try:
        res = float(x) * multiplier
    except ValueError:
        print("Error: parámetros especificados incorrectamente")
    
    return res
    
        
class iniciar:

    def __init__(self):
        app = QtWidgets.QApplication([])
        self.ventana = uic.loadUi("gui_principal.ui")
        self.ventana.show()

        self.ventana.actionSalir_2.triggered.connect(self.click_actionsalir)
        self.ventana.graphicButton.clicked.connect(self.graphics)
        self.ventana.graphicRLC_Button.clicked.connect(self.graphicsRLC)

        self.graphic_bode_mod = plotWidget()
        self.graphic_bode_phase = plotWidget()
        self.graphic_output = plotWidget()
        self.graphic_ZP = plotWidget()
        self.graphic_bode_mod_RLC = plotWidget()
        self.graphic_bode_phase_RLC = plotWidget()

        self.ventana.graphic_bode_mod.addWidget(self.graphic_bode_mod.plot)
        self.ventana.graphic_bode_phase.addWidget(self.graphic_bode_phase.plot)
        self.ventana.graphic_output.addWidget(self.graphic_output.plot)
        self.ventana.graphic_ZP.addWidget(self.graphic_ZP.plot)
        self.ventana.graphic_bode_mod_RLC.addWidget(self.graphic_bode_mod_RLC.plot)
        self.ventana.graphic_bode_phase_RLC.addWidget(self.graphic_bode_phase_RLC.plot)
      # self.ventana.graphic_img.addWidget('RLC.png')
  
        app.exec()





    def selectFilter(self,order,filter,wo,k,psi):
        
        if(order == 1):
            if(filter==0):
                obj = pasaBajos(wo,k)
                return obj
            elif(filter==1):
                obj = pasaAltos(wo,k)
                return obj
            elif(filter==2):
                obj = pasaTodo(wo,k)
                return obj
        elif(order==2):
            if(filter==0):
                obj = pasaBajos_2(wo,k,psi)
                return obj
            elif(filter==1):
                obj = pasaAltos_2(wo,k,psi)
                return obj
            elif(filter==2):
                obj = pasaTodo_2(wo,k,psi)
                return obj
            if(filter==3):
                obj = pasaBanda(wo,k,psi)
                return obj
            elif(filter==4):
                obj = notch(wo,k,psi)
                return obj


                

    def plotSignal(self,fz,amplitud,wo,k,psi):

        filter = 0

        if(self.ventana.PrimerOrdenButton.isChecked()):
            order = 1
            filter = self.ventana.selectFilter_01.currentIndex() ## los filtros se manejan por numero de index
            filter = (self.selectFilter(order,filter,wo,k,psi))

        elif(self.ventana.SegundoOrdenButton.isChecked()):
            order = 2
            filter=self.ventana.selectFilter_2.currentIndex()
            filter = (self.selectFilter(order,filter,wo,k,psi))
 
        if(not filter.k):
            return

        t = np.linspace(0, 1, 500)

        if(self.ventana.sineButton.isChecked()):
            self.graphic_output.plotFilteredSignal(filter,np.sin(2*np.pi*int(fz)*t),t)
        elif(self.ventana.sawButton.isChecked()):
            self.graphic_output.plotFilteredSignal(filter,signal.sawtooth(2*np.pi*int(fz)*t),t)
            return
        elif(self.ventana.squareButton.isChecked()):
            self.graphic_output.plotFilteredSignal(filter,signal.square(2*np.pi*int(fz)*t),t)
            return
        elif(self.ventana.pulseButton.isChecked()):
            self.graphic_output.plotResponse(signal.impulse(filter.tf))
            return  
        elif(self.ventana.stepButton.isChecked()):
            self.graphic_output.plotResponse(signal.step(filter.tf))
            return  
        return


    def plotFilter(self,order,filter,wo,k,psi):

        filter = (self.selectFilter(order,filter,wo,k,psi))

        if(filter.k):
            self.graphic_bode_mod.bodeMod(filter.tf)
            self.graphic_bode_phase.bodePhase(filter.tf)
            self.graphic_ZP.plotZP(filter.tf)



        return



    def graphics(self):

        wo = convertToFloat(self.ventana.inputWo.text())
        fz = convertToFloat(self.ventana.inputFz.text())
        amp = convertToFloat(self.ventana.inputAmp.text())
        k = convertToFloat(self.ventana.inputK.text())
        psi = convertToFloat(self.ventana.inputPsi.text())

        if(np.isnan(wo) or np.isnan(fz) or np.isnan(amp) or np.isnan(k) or np.isnan(psi)):
            return

        if(self.ventana.PrimerOrdenButton.isChecked()):
            order = 1
            filter = self.ventana.selectFilter_01.currentIndex() ## los filtros se manejan por numero de index
        elif(self.ventana.SegundoOrdenButton.isChecked()):
            order = 2
            filter=self.ventana.selectFilter_2.currentIndex()
            
        self.plotFilter(order,filter,wo,k,psi)
        self.plotSignal(fz,amp,wo,k,psi)

        return 


    def click_actionsalir(self):
        sys.exit()


    def graphicsRLC(self):

        R = convertToFloat(self.ventana.inputR.text())
        L = convertToFloat(self.ventana.inputL.text())
        C = convertToFloat(self.ventana.inputC.text())

        if(np.isnan(R) or np.isnan(L) or np.isnan(C)):
            return
        
        if(self.ventana.button_1_4.isChecked()):
            filter = ft_1_4(R,L,C)
            self.graphic_bode_mod_RLC.bodeMod(filter.tf)
            self.graphic_bode_phase_RLC.bodePhase(filter.tf)
            return

        elif(self.ventana.button_1_3.isChecked()):
            filter = ft_1_3(R,L,C)
            self.graphic_bode_mod_RLC.bodeMod(filter.tf)
            self.graphic_bode_phase_RLC.bodePhase(filter.tf)
            return

        elif(self.ventana.button_1_2.isChecked()):
            filter = ft_1_2(R,L,C)
            self.graphic_bode_mod_RLC.bodeMod(filter.tf)
            self.graphic_bode_phase_RLC.bodePhase(filter.tf)
            return
        elif(self.ventana.button_2_4.isChecked()):
            filter = ft_2_4(R,L,C)
            self.graphic_bode_mod_RLC.bodeMod(filter.tf)
            self.graphic_bode_phase_RLC.bodePhase(filter.tf)
            return
        elif(self.ventana.button_2_3.isChecked()):
            filter = ft_2_3(R,L,C)
            self.graphic_bode_mod_RLC.bodeMod(filter.tf)
            self.graphic_bode_phase_RLC.bodePhase(filter.tf)
            return
        elif(self.ventana.button_3_4.isChecked()):
            filter = ft_3_4(R,L,C)
            self.graphic_bode_mod_RLC.bodeMod(filter.tf)
            self.graphic_bode_phase_RLC.bodePhase(filter.tf)
            return


class pasaBajos():
    def __init__(self,wo,k, parent=None): 
        self.wo = wo
        self.k = k
        num = np.array([1])
        num = np.polymul(num,self.k)
        den = np.array([1/(self.wo),1])

        self.tf = signal.TransferFunction(num,den)

class pasaAltos():
    def __init__(self,wo,k, parent=None):
        self.wo = wo
        self.k = k
        num = np.array([1,0])
        num = np.polymul(num,self.k)
        den = np.array([1/(self.wo),1])

        self.tf = signal.TransferFunction(num,den)

class pasaTodo():
    def __init__(self,wo,k, parent=None):
        self.wo = wo
        self.k = k
        num = np.array([1/(self.wo),-1])
        num = np.polymul(num,self.k)
        den = np.array([1/(self.wo),1])

        self.tf = signal.TransferFunction(num,den)
         
    ## 2 orden 
class pasaBajos_2():
    def __init__(self,wo,k,psi, parent=None): 
        self.wo = wo
        self.k = k
        self.psi = psi
        num = np.array([self.k])
        den = np.array([1/((self.wo)*(self.wo)),(2*self.psi)/(self.wo),1])
        self.tf = signal.TransferFunction(num,den)

class pasaAltos_2():
    def __init__(self,wo,k,psi, parent=None):
        self.wo = wo
        self.k = k
        self.psi = psi
        num = np.array([k,0,0])
        den = np.array([1/((self.wo)*(self.wo)),(2*self.psi)/(self.wo),1])
        self.tf = signal.TransferFunction(num,den)

class pasaTodo_2():
    def __init__(self,wo,k,psi, parent=None):
        self.wo = wo
        self.k = k
        self.psi = psi
        num = np.array([1/((self.wo)*(self.wo)),((-2)*self.psi)/(self.wo),1])
        num = np.polymul(num,self.k)
        den = np.array([1/((self.wo)*(self.wo)),(2*self.psi)/(self.wo),1])
        self.tf = signal.TransferFunction(num,den)
class pasaBanda():
    def __init__(self,wo,k,psi, parent=None):
        self.wo = wo
        self.k = k
        self.psi = psi
        num = np.array([1,0])
        num = np.polymul(num,self.k)
        den = np.array([1/((self.wo)*(self.wo)),(2*self.psi)/(self.wo),1])
        self.tf = signal.TransferFunction(num,den)

class notch():
    def __init__(self,wo,k,psi, parent=None):
        self.wo = wo
        self.k =  k
        self.psi = psi
        num = np.array([1/((self.wo)*(self.wo)),0,1])
        num = np.polymul(num,[self.k])
        den = np.array([1/((self.wo)*(self.wo)),(2*self.psi)/(self.wo),1])
        self.tf = signal.TransferFunction(num,den)
class lowPassNotch():
    def __init__(self,wo,k, parent=None):
        return
class highPassNotch():
    def __init__(self,wo,k, parent=None):
        return

class Canvas_grafica(FigureCanvas):
    def __init__(self, parent=None):     
        self.fig , self.ax = plt.subplots(1, dpi=100, figsize=(5, 5), 
            sharey=True, facecolor='white')
        super().__init__(self.fig) 

        nombres = ['15', '25', '30', '35','40']
        colores = ['red','red','red','red', 'red']
        tamaño = [10, 15, 20, 25, 30]

        self.ax.bar(nombres, tamaño, color = colores)
        self.fig.suptitle('Grafica de Barras',size=9)




class ft_1_4():
    def __init__(self,R,L,C, parent=None):
        self.R = R
        self.L = L
        self.C = C
        num = np.array([1])
        den = np.array([1])
        self.tf = signal.TransferFunction(num,den)

class ft_1_3():
    def __init__(self,R,L,C, parent=None):
        self.R = R
        self.L = L
        self.C = C
        num = np.array([(self.L)*(self.C),(self.R)*(self.C),0])
        den = np.array([(self.L)*(self.R),(self.R)*(self.C),1])
        self.tf = signal.TransferFunction(num,den)

class ft_1_2():
    def __init__(self,R,L,C, parent=None):
        self.R = R
        self.L = L
        self.C = C
        num = np.array([self.R*self.C,0])
        den = np.array([self.L*self.C,self.C*self.R,1])
        self.tf = signal.TransferFunction(num,den)

class ft_2_4():
    def __init__(self,R,L,C, parent=None):
        self.R = R
        self.L = L
        self.C = C
        num = np.array([self.L*self.C,0,1])
        den = np.array([self.L*self.C,self.C*self.R,1])
        self.tf = signal.TransferFunction(num,den)

class ft_2_3():
    def __init__(self,R,L,C, parent=None):
        self.R = R
        self.L = L
        self.C = C
        num = np.array([self.L*self.C,0,0])
        den = np.array([self.L*self.C,self.C*self.R,1])
        self.tf = signal.TransferFunction(num,den)

class ft_3_4():
    def __init__(self,R,L,C, parent=None):
        self.R = R
        self.L = L
        self.C = C
        num = np.array([1])
        den = np.array([self.L*self.C,self.C*self.R,1])
        self.tf = signal.TransferFunction(num,den)


#    self.ventana.actionDatos.triggered.connect(self.click_actionDatos)    
  #  def click_actionDatos(self):
     #   self.x01 = uic.loadUi("ventana_x01.ui")
      #  self.x01.show()
      #  self.x01.pb_cancelar.clicked.connect(self.clickcancelar)

  #  def clickcancelar(self):
     #   self.x01.close()
    


iniciar()

    