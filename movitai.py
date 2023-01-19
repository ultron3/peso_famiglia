#utilizzo la libreria pyprcode, pypng, langdetect

from langdetect import detect

text = input("enter any text in any language: ")

print( detect(text))
if text == "italiano":
      

  print("Per accedere all'applicazione Movit Ai  inquadrare codice qr")
  link= input ("link per generare QRcode: ")
  print("Ricordati che devi impostare una password")
  passlen= int(input("inserisci un numero per la generazione della password:"))
else:
   print("Scan the qr code to access the Movit Ai application")
   link=input("generate link for QRcode: ")
   print("Remember that you need to set a password")
   passlen= int(input("enter the lenght of password:"))   


import pyqrcode
from PIL import Image


qr_code= pyqrcode.create(link) #https://twitter.com/clcoding
qr_code.png("QRCode.png",scale=5)
Image.open("QRCode.png")

#genero una password per l'applicazione


import random

s="abcdefghijklmnopqrstuvwxyz1234567890?#*&%$"
p="".join(random.sample(s,passlen))
print(p)

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