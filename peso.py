#inizio codice
#utilizzo la libreria  numpy e pandas

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn as sk
import pandas as pd



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
#faccio vedere i miei andamenti in palestra 
try:

    giorno1=input("inserisci il nome del giorno: ")
    giorno2=input("inserisci il nome del giorno: ")
    giorno3=input("inserisci il nome del giorno: ")
    tempo1=float(input("inserisci quante ore fai di allenamento: "))
    tempo2=float(input("inserisci quante ore fai di allenamento: "))
    tempo3=float(input("inserisci quante ore fai di allenamento: "))
    x = np.array([giorno1,giorno2,giorno3])
    y = np.array([tempo1,tempo2,tempo3])

    plt.plot(x, y)

    plt.xlabel("giorni")
    plt.ylabel("tempo allenamneto")


    plt.show()
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

#regressione lineare


from sklearn.linear_model import LinearRegression        

x = np.array([1.76,1.69,1.57,1.70,1.78])#peso  
y = np.array([ 72,80,68.8,80,73])#altezza   

lr = LinearRegression()
lr.fit(x.reshape(-1, 1), y)

#Predizione
print(lr.predict([[1.57]]))




#apro un documento excel utilizzando la libreria openpyxl
import openpyxl
excel_document = openpyxl.load_workbook('progressi_palestra.xlsx')
print (type(excel_document))

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["dbmpalestra"]
mycol = mydb["progressi"]

nome=input("inserisci nome: ")
usr=input("inserisci username: ")
abitazione=input("inserisci dove abiti: ")
percorso=float(input("inserisci quanti km vuoi fare: "))
record=float(input("record precedenti: "))

mydict={ 
    "nome": nome, 
    "username" :usr,
    "indirizzo":abitazione,
    "percorso":percorso,
    "record":record
}

x = mycol.insert_one(mydict)

#fine codice


print("****** THE END *********")










