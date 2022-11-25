
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn as sk
import pandas as pd
from tensorflow import keras
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["dbmpalestra"]
mycol = mydb["progressi"]

nome=input("inserisci nome: ")
usr=input("inserisci username: ")
abitazione=input(" dove abiti: ")
percorso=float(input("inserisci quanti km vuoi fare: "))
giorno=input("inserisci il giorno: ")
media_settimanale=float(input("media km precedenti: "))

mydict={ 
    "nome": nome, 
    "username" :usr,
    "indirizzo":abitazione,
    "percorso":percorso,
    "giorno":giorno,
    "record":media_settimanale
}

x = mycol.insert_one(mydict)

print("Ciao mi chiamo Movit Ai il tuo personal virtuale")


print("inizio settimana ")

try:
#inserisco i giorni
    giorno1=input("inserisci il giorno:")
    giorno2=input("inserisci il giorno: ")
    giorno3=input("inserisci il giorno: ")
    giorno4=input("inserisci il giorno: ")
    giorno5=input("inserisci il giorno: ")
  #inserisco i km che faccio a piedi
    km1=float(input("inserisci i km fatti: "))
    km2=float(input("inserisci i km fatti: "))
    km3=float(input("inserisci i km fatti: "))
    km4=float(input("inserisci i km fatti: "))
    km5=float(input("inserisci i km fatti: "))
    
    x = np.array([giorno1,giorno2,giorno3,giorno4,giorno5])
    y = np.array([km1,km2,km3,km4,km5])

    plt.plot(x, y)

    plt.xlabel("giorni")
    plt.ylabel("km fatti")


    plt.show()
    media=(km1+km2+km3+km4+km5)/5
    print("la media settimanale è "+str(media))
except:
    print("dati inseriti non corretti")

#utilizzo modello gaussiano

n=int(input("inserisci un numero (deve essere 0[lunedi], 1[mercoledi], 2[venerdi]):  "))

giorni_allenamento=["lunedi","martedi","mercoledi","giovedi","venerdi","sabato"]
uscita=["si","no","si","no","si","si"]

from sklearn import preprocessing
le = preprocessing.LabelEncoder() # Creo il label encoder (chiamato dunque "le")
giorni_encoded=le.fit_transform(giorni_allenamento)
uscita_encoded=le.fit_transform(uscita)
from sklearn.naive_bayes import GaussianNB 
model = GaussianNB()
model.fit(giorni_encoded.reshape(-1, 1), uscita_encoded) 
predicted=model.predict([[n]])
print("giorno in cui potrei allenarmi: ") 
print(predicted.tolist()) 

print(nome+str(" questa settimana hai una media di ")+str(media)+str(" km "))
try:
    giorno1=input("inserisci il giorno:")
    giorno2=input("inserisci il giorno: ")
    giorno3=input("inserisci il giorno: ")
    giorno4=input("inserisci il giorno: ")
    giorno5=input("inserisci il giorno: ")
    peso1=float(input("inserisci il peso: "))
    peso2=float(input("inserisci il peso: "))
    peso3=float(input("inserisci il peso: "))
    peso4=float(input("inserisci il peso: "))
    peso5=float(input("inserisci il peso: "))
    z = np.array([giorno1,giorno2,giorno3,giorno4,giorno5])
    v = np.array([peso1,peso2,peso3,peso4,peso5])

    plt.plot(z,v)

    plt.xlabel("giorni")
    plt.ylabel("peso")
    plt.show()

    media=(peso1+peso2+peso3+peso4+peso5)/5
    print("la media settimanale è "+str(media))

    
except:
    print("dati inserti non corretti")

