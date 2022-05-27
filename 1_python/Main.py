from PyQt5.QtWidgets import QApplication
import MyApp
import sys

app = QApplication([])
window = MyApp()
window.show()
sys.exit(app.exec_())