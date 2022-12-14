#inizio codice
#utilizzo la libreria  numpy e pandas

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn as sk
import pandas as pd
from tensorflow import _keras_module


#attraverso python  documento i miei progressi in palestra

print(" settimana di ferragosto")
x = np.array(["lunedi","martedi","mercoledi","giovedi","venerdi","sabato","domenica"])
y = np.array([75.6,75.20,75.20,74.85,74.35,74.35,75.20])

plt.plot(x, y)

plt.xlabel("giorni")
plt.ylabel("peso")


plt.show()


print("settimana dopo ferragosto")
x = np.array(["lunedi","martedi","mercoledi","giovedi","venerdi","sabato","domenica"])
y = np.array([74.35,74,74.30,74,74.35,74.32,73.90])

plt.plot(x, y)

plt.xlabel("giorni")
plt.ylabel("peso")


plt.show()

#documento gli ultimi giorni di agosto

print("ultimi giorni di agosto")
x = np.array(["lunedi","martedi","mercoledi"])
y = np.array([74.35,73.9,74.35])

plt.plot(x, y)

plt.xlabel("giorni")
plt.ylabel("peso")


plt.show()


#do il comando di aprire un file in jsonata

print("confronto peso e altezza con i famigliari")

df = pd.read_json('famiglia.json')

print(df.to_string()) 


#modello gaussiano
n=int(input("inserisci un numero: "))
giorni=["lunedi","martedi","mercoledi","giovedi","venerdi","sabato","domenica"]
uscita=["si","no","si","no","si","no","no"]
from sklearn import preprocessing
le = preprocessing.LabelEncoder() # Creo il label encoder (chiamato dunque "le")
giorni_encoded=le.fit_transform(giorni)
uscita_encoded=le.fit_transform(uscita)
from sklearn.naive_bayes import GaussianNB 
model = GaussianNB()
model.fit(giorni_encoded.reshape(-1, 1), uscita_encoded)
predicted=model.predict([[n]])
print("il risultato è:") 
print(predicted.tolist()) 

#regressione lineare tra altezza e peso


from sklearn.linear_model import LinearRegression        

x = np.array([1.57,1.69,1.70,1.76,1.78])#peso  #1.57 1.69 1.70 1.76 1.78
print("altezza:"+str(x))
y = np.array([ 68.8,72,73,75,80])#altezza   #68.8 72 73 75 80
print("peso:"+str(y))
n=float(input("inserisci il valore mediano dell'altezza:"))
lr = LinearRegression()
lr.fit(x.reshape(-1, 1), y)

#Predizione
print(lr.predict([[n]]))

coef = np.polyfit(x,y,1)
poly1d_fn = np.poly1d(coef)

plt.plot(x,y, 'yo', x, poly1d_fn(x), '-k')

plt.xlim(0, 5)
plt.ylim(0, 300)
plt.show()

#da ricontrollare
try:
    peso=float(input("inserisci il peso: "))
    altezza=float(input("inserisci l'altezza: "))
    BMI=peso/(altezza*altezza)
    print(BMI)
except:
    print("dati inseriti non corretti")

#da ricontrollare

dC = pd.read_csv('bmi.csv')

print(dC.to_string())



#apro un documento excel utilizzando la libreria openpyxl
#per capire che il file in excel è aperto il programma scrive class workbook.worbook
#attenzione se si sbaglia a scrivere su una cella il programma non si rompe ma ti dice che c'è un errore in una cella speicifica
import openpyxl
import openpyxl
excel_document = openpyxl.load_workbook('progressi_palestra.xlsx')
print (type(excel_document))

sheet = excel_document.get_sheet_by_name('Foglio1')
print (sheet['D9'].value)

sheet = excel_document.get_sheet_by_name('Foglio1')
print (sheet['E9'].value)

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="telemedicina2123"
)

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM post.dati_famigliari")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)

#inserisco nuovi record
nome=input("inserisci nome: ")
cognome=input("inserisci cogome: ")
peso=input("inserisci peso: ")
altezza=float(input("inserisci l'altezza: "))
mycursor = mydb.cursor()
sql = "INSERT INTO post.dati_famigliari(nome,cognome,peso,altezza)VALUES (%s,%s,%s,%s);" 
val = (nome,cognome,peso,altezza)
mycursor.execute(sql,val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")


#fine codice


print("****** THE END *********")








