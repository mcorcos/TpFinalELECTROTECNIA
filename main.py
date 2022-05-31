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


        self.ventana.grafica_01 = Canvas_grafica1()
        self.ventana.grafica_02 = Canvas_grafica2()
        self.ventana.grafica_03 = Canvas_grafica3()
        self.ventana.grafica_04 = Canvas_grafica4()

        self.ventana.grafica_uno.addWidget(self.grafica_01)
        self.ventana.grafica_dos.addWidget(self.grafica_02)
        self.ventana.grafica_tres.addWidget(self.grafica_03)
        self.ventana.grafica_cuatro.addWidget(self.grafica_04)   




        app.exec()

    def click_actionsalir(self):
        sys.exit()

#    self.ventana.actionDatos.triggered.connect(self.click_actionDatos)    
  #  def click_actionDatos(self):
        self.x01 = uic.loadUi("ventana_x01.ui")
        self.x01.show()
        self.x01.pb_cancelar.clicked.connect(self.clickcancelar)

  #  def clickcancelar(self):
        self.x01.close()
    

         self.grafica = Canvas_grafica()







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

def plotSignal():
    return



iniciar()

    