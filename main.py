import sys
from PyQt5 import QtWidgets, uic

class iniciar:
    def __init__(self):
        app = QtWidgets.QApplication([])
        self.ventana = uic.loadUi("gui_principal.ui")
        self.ventana.show()

        self.ventana.actionSalir_2.triggered.connect(self.click_actionsalir)
        self.ventana.actionDatos.triggered.connect(self.click_actionDatos)
        app.exec()

        #sis.exit
    def click_actionsalir(self):
        sys.exit()
    
    def click_actionDatos(self):
        self.x01 = uic.loadUi("ventana_x01.ui")
        self.x01.show()
        self.x01.pb_cancelar.clicked.connect(self.clickcancelar)

    def clickcancelar(self):
        self.x01.close()




iniciar()

    