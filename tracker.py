
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn as sk
import pandas as pd

from tensorflow import _keras_module



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
except:
    print("dati inseriti non corretti")

#utilizzo modello gaussiano

n=int(input("inserisci un numero (deve essere 0, 1, 2):  "))

giorni_allenamento=["lunedi","mercoledi","venerdi","sabato"]
uscita=["si","no","si","si"]
from sklearn import preprocessing
le = preprocessing.LabelEncoder() # Creo il label encoder (chiamato dunque "le")
giorni_encoded=le.fit_transform(giorni_allenamento)
uscita_encoded=le.fit_transform(uscita)
from sklearn.naive_bayes import GaussianNB 
model = GaussianNB()
model.fit(giorni_encoded.reshape(-1, 1), uscita_encoded) #: 2: lunedi, 1=mercoledi, 0: venerdi.
predicted=model.predict([[n]])
print("il risultato è:") 
print(predicted.tolist()) 