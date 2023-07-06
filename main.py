# Importamos pyqt5
import sys

from PyQt5 import QtWidgets
from UI_Principal import Ui_UnitConversor
#instalacion de pyqt5: "pip install pyqt5 pyqt5-tools"


class mainwindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(mainwindow, self).__init__()
        self.ui = Ui_UnitConversor()
        self.ui.setupUi(self)

app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())



