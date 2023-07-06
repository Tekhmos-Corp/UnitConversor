# Importamos pyqt5
import sys

from PyQt5 import QtWidgets
from UI_Principal import Ui_UnitConversor
#instalacion de pyqt5: "pip install pyqt5 pyqt5-tools"


# class mainwindow(QtWidgets.QMainWindow):
    
#     def __init__(self):
#         super(mainwindow, self).__init__()
#         self.ui = Ui_UnitConversor()
#         self.ui.setupUi(self)

# Dictionary with key main_dropdown and key dictionaries
global globe_dictionary = {"Distance": {"Kilometers": 1000, "Meters": 1, "Centimeters": 0.01, "Millimeters": 0.001, "Miles": 1609.9, "Yards": 1093.61, "Feet": 3280.84, "Inches": 39370.1},
    "Area": {"Square kilometers": 1000000, "Square meters": 1, "Square centimeters": 0.0001, "Square millimeters": 0.000001, "Square miles": 2590000, "Square yards": 0.836127, "Square feet": 0.092903, "Square inches": 0.00064516, "Hectares": 10000, "Acres": 4046.86},
    "Temperature": {"Celsius": 1, "Fahrenheit": 33.8, "Kelvin": 274.15}, # bogus, luego modificar
    "Volume": {"Liters": 1, "Milliliters": 0.001, "Cubic meters": 1000, "Cubic centimeters": 0.001, "Cubic inches": 0.0163871, "Cubic feet": 28.3168, "Gallons": 3.78541}, # bogus, luego modificar
    "Mass": {"Kilograms": 1, "Grams": 0.001, "Milligrams": 0.000001, "Pounds": 0.453592, "Ounces": 0.0283495},
    "Time": {"Seconds": 1, "Minutes": 60, "Hours": 3600, "Days": 86400, "Weeks": 604800, "Years": 31536000},
    "Speed": {"Meters per second": 1, "Kilometers per hour": 3.6, "Miles per hour": 2.23694, "Knots": 1.94384},
    #"Frequency": {"Hertz": 1, "Kilohertz": 1000, "Megahertz": 1000000, "Gigahertz": 1000000000},
    "Data": {"Bits": 1, "Bytes": 8, "Kilobits": 1000, "Kilobytes": 8000, "Megabits": 1000000, "Megabytes": 8000000, "Gigabits": 1000000000, "Gigabytes": 8000000000, "Terabits": 1000000000000, "Terabytes": 8000000000000},
    "Energy": {"Joules": 1, "Kilojoules": 1000, "Calories": 4.184, "Kilocalories": 4184, "Kilowatt-hours": 3600000, "Watt-hours": 3600, "Foot-pounds": 1.35582, "BTUs": 1055.06},
    "Power": {"Watts": 1, "Kilowatts": 1000, "Megawatts": 1000000, "Gigawatts": 1000000000, "Horsepower": 745.7},
    "Pressure": {"Pascals": 1, "Hectopascals": 100, "Kilopascals": 1000, "Megapascals": 1000000, "Bars": 100000, "PSI": 6894.76, "Atmospheres": 101325, "Millimeters of mercury": 133.322, "Inches of mercury": 3386.39},
    "Angle": {"Degrees": 1, "Radians": 57.2958, "Gradians": 0.9, "Revolutions": 360}
    #"Fuel Economy": {"Miles per gallon": 1, "Liters per 100 kilometers": 235.215, "Miles per gallon (UK)": 1.20095}
    #"Cooking": {"Teaspoons": 1, "Tablespoons": 3, "Cups": 48, "Quarts": 192, "Gallons": 768, "Cubic feet": 5745.04, "Cubic meters": 202884.14}
}

class MainWindow(Ui_UnitConversor):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        self.setupUi(parent)
        self.main_dropdown.currentIndexChanged.connect(self.update_selection)
        # Modificar el QComboBox

    def update_selection(self, parent=None):
        self.from_dropbox.clear()
        self.to_dropbox.clear()
        selection = self.main_dropdown.currentText() 
        for key in globe_dictionary[selection]:
            self.from_dropbox.addItem(key)
            self.to_dropbox.addItem(key)


            

# app = QtWidgets.QApplication([])
# application = MainWindow()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = MainWindow(window)
    window.show()
    sys.exit(app.exec_())


