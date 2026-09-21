import sys

from PyQt5.QtWidgets import QApplication

from calculatrice import Calculatrice
app = QApplication(sys.argv)
fenetre = Calculatrice()
fenetre.show()
sys.exit(app.exec_())
