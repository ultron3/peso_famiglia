print("Per accedere all'applicazione Movit Ai  inquadrare codice qr")
import pyqrcode
from PIL import Image
link= input ("enter anithing to generate QR: ")
qr_code= pyqrcode.create(link) #https://twitter.com/clcoding
qr_code.png("QRCode.png",scale=5)
Image.open("QRCode.png")


import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
#importo la classe generata da compilatore ui py
#dal file demo1.py importo la classe ui_mainwindow
#ora posso usare ui_mainwindow
import jwt
from ui_movitai import Ui_MainWindow
#creo la classe mainwindow che eredita le caratteristiche della classe  mainwindow
#scrivo la classe 




class MainWindow(QMainWindow):
      #nel costruttore inserisco  tutto il codice  per gestire la finestra e gli oggetti di caricare dentro
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        
        
        self.setWindowTitle("MOVITAI")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()       