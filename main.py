import sys
from PyQt5 import QtWidgets, uic

class iniciar:
    def __init__(self):
        app = QtWidgets.QApplication([])
        self.ventana = uic.loadUi("gui_principal.ui")
        self.ventana.show()

        self.ventana.actionSalir_2.triggered.connect(self.click_actionsalir)
    #    self.ventana.actionDatos.triggered.connect(self.click_actionDatos)
        self.ventana.graphicButton.clicked.connect(self.graphics)
        app.exec()

        #sis.exit
    def click_actionsalir(self):
        sys.exit()
    
  #  def click_actionDatos(self):
        self.x01 = uic.loadUi("ventana_x01.ui")
        self.x01.show()
        self.x01.pb_cancelar.clicked.connect(self.clickcancelar)

  #  def clickcancelar(self):
        self.x01.close()
    
    def graphics(self):

        if(self.ventana.sineButton.isChecked()):
            Wo = self.ventana.inputWo.text()
            Fz = self.ventana.inputFz.text()
            Amp = self.ventana.inputAmp.text()
            K = self.ventana.inputK.text()
            plotSignal()
            

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

    