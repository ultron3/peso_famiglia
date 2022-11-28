
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
password=input("inserisci la password: ")
abitazione=input(" dove abiti: ")
palestra=input("inserisci il nome della palestra in cui sei iscritto: ")
allenamento=input("inserisci il tipo di allenamento che vuoi fare")


mydict={ 
    "nome": nome, 
    "username" :usr,
    "pasasword":password,
    "indirizzo":abitazione,
    "palestra": palestra,
    "allenamento":allenamento


   
}

x = mycol.insert_one(mydict)

print("Ciao mi chiamo Movit Ai il tuo personal virtuale,monitora giorno per giorno i passi fatti; ricordati di impostare un obiettivo giornaliero ")

c=input("hai impostato un'obiettivo giornaliero:")
if c =="si":
    print("ok perfetto")
else:
    print("ricordati di farlo")

print("inizio settimana ")

try:
#inserisco i giorni
    giorno1=input("inserisci il giorno:")
    giorno2=input("inserisci il giorno: ")
    giorno3=input("inserisci il giorno: ")
    giorno4=input("inserisci il giorno: ")
    giorno5=input("inserisci il giorno: ")
  #inserisco i km che faccio a piedi
    ps1=float(input("inserisci i passi fatti: "))
    ps2=float(input("inserisci i passi fatti: "))
    ps3=float(input("inserisci i passi fatti: "))
    ps4=float(input("inserisci i passi fatti: "))
    ps5=float(input("inserisci i passi fatti: "))
    
    x = np.array([giorno1,giorno2,giorno3,giorno4,giorno5])
    y = np.array([ps1,ps2,ps3,ps4,ps5])

    plt.plot(x, y)

    plt.xlabel("giorni")
    plt.ylabel("km fatti")


    plt.show()
    media=(ps1+ps2+ps3+ps4+ps5)/5
    print("la media settimanale dei passi  è "+str(media))
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

print("ciao "+str(nome)+str(" questa settimana hai una media di ")+str(media)+str(" km ")+str("hai scelto di fare ")+str(allenamento))

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




print(nome+str(" per un buon andamento monitora il tuo peso giornaliero "))




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


#apro un documento excel utilizzando la libreria openpyxl
import openpyxl
excel_document = openpyxl.load_workbook('progressi_palestra.xlsx')
print (type(excel_document))






