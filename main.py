import sys
from PyQt5 import QtWidgets, uic
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

class iniciar:
    def __init__(self):
        app = QtWidgets.QApplication([])
        self.ventana = uic.loadUi("gui_principal.ui")
        self.ventana.show()

        self.ventana.actionSalir_2.triggered.connect(self.click_actionsalir)
        self.ventana.graphicButton.clicked.connect(self.graphics)


        self.graphic_1 = Canvas_grafica()
        self.graphic_2 = Canvas_grafica()
        self.graphic_3 = Canvas_grafica()
        self.graphic_4 = Canvas_grafica()

        self.ventana.graphic_01.addWidget(self.graphic_1)
        self.ventana.graphic_02.addWidget(self.graphic_2)
        self.ventana.graphic_03.addWidget(self.graphic_3)
        self.ventana.graphic_04.addWidget(self.graphic_4)   

        app.exec()

    def graphics(self):

        Wo = self.ventana.inputWo.text()
        Fz = self.ventana.inputFz.text()
        Amp = self.ventana.inputAmp.text()
        K = self.ventana.inputK.text()
        Psi = self.ventana.inputPsi.text()

        if(self.ventana.sineButton.isChecked()):
            plotSignal()
            return
        elif(self.ventana.sawButton.isChecked()):
            plotSignal()
            return
        elif(self.ventana.triangularButton.isChecked()):
            plotSignal()
            return
        elif(self.ventana.pulseButton.isChecked()):
            plotSignal()
            return   

    def click_actionsalir(self):
        sys.exit()



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




#    self.ventana.actionDatos.triggered.connect(self.click_actionDatos)    
  #  def click_actionDatos(self):
     #   self.x01 = uic.loadUi("ventana_x01.ui")
      #  self.x01.show()
      #  self.x01.pb_cancelar.clicked.connect(self.clickcancelar)

  #  def clickcancelar(self):
     #   self.x01.close()
    

def plotSignal():
    return


iniciar()

    