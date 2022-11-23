#inizio codice
#utilizzo la libreria  numpy e pandas

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn as sk
import pandas as pd

from tensorflow import keras

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

#calcolo medie carico esercizi
try:

    esercizio=input("inserisci il nome  dell'esercizio: ")
    print(esercizio)

    serie=int(input("inserisci quante serie fai: "))
    
    kg1=float(input("inserisci i kili: "))
    kg2=float(input("inserisci i kili: "))
    kg3=float(input("inserisci i kili: "))
    
    if serie == 2:
        
        media=(kg1+kg2)/2
        print("la media dell'esercizio "+str(media))
    elif serie > 2:
        media=(kg1+kg2+kg3)/3
        print("la media è"+str(media))
    else:
        print("dati inseriti non corretti")


except:
    print("dati inseriti non corretti")



try:
    bike=float(input("inserisci quanti kilometri fai con la bici: "))
    ciclette=float(input("inserisci quanti km fai con la cyclette: "))
    tappeto=float(input("inserisci quanti km fai con il tappeto: "))
    media=(bike+ciclette+tappeto)/3
    print("la media dei km è:"+str(media))
except:
    print("dati inseriti non corretti")

#do il comando di aprire un file in jsonata

print("confronto peso e altezza con i famigliari")

df = pd.read_json('famiglia.json')

print(df.to_string()) 


#modello gaussiano

giorni=["lunedi","martedi","mercoledi","giovedi","venerdi","sabato","domenica"]
uscita=["si","no","si","no","si","no","no"]
from sklearn import preprocessing
le = preprocessing.LabelEncoder() # Creo il label encoder (chiamato dunque "le")
giorni_encoded=le.fit_transform(giorni)
uscita_encoded=le.fit_transform(uscita)
from sklearn.naive_bayes import GaussianNB 
model = GaussianNB()
model.fit(giorni_encoded.reshape(-1, 1), uscita_encoded)
predicted=model.predict([[2]])
print("il risultato è:") 
print(predicted.tolist()) 

#regressione lineare tra altezza e peso


from sklearn.linear_model import LinearRegression        

x = np.array([1.57,1.69,1.70,1.76,1.78])#peso  #1.57 1.69 1.70 1.76 1.78
y = np.array([ 68.8,72,73,75,80])#altezza   #68.8 72 73 75 80

lr = LinearRegression()
lr.fit(x.reshape(-1, 1), y)

#Predizione
print(lr.predict([[1.70]]))





#apro un documento excel utilizzando la libreria openpyxl
import openpyxl
excel_document = openpyxl.load_workbook('progressi_palestra.xlsx')
print (type(excel_document))

sheet = excel_document.get_sheet_by_name('Foglio1')
print (sheet['D9'].value)

sheet = excel_document.get_sheet_by_name('Foglio1')
print (sheet['E9'].value)

#collegamento a mongodb

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["dbmpalestra"]
mycol = mydb["progressi"]

nome=input("inserisci nome: ")
usr=input("inserisci username: ")
abitazione=input("inserisci dove abiti: ")
percorso=float(input("inserisci quanti km vuoi fare: "))
giorno=input("inserisci il giorno: ")
record=float(input("record precedenti: "))

mydict={ 
    "nome": nome, 
    "username" :usr,
    "indirizzo":abitazione,
    "percorso":percorso,
    "giorno":giorno,
    "record":record
}

x = mycol.insert_one(mydict)



#fine codice


print("****** THE END *********")








