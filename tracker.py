
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
cognome=input("inserisci cognome: ")
usr=input("inserisci username: ")
password=input("inserisci la password: ")
abitazione=input(" dove abiti: ")
palestra=input("inserisci il nome della palestra in cui sei iscritto: ")
allenamento=input("inserisci il tipo di allenamento che vuoi fare: ")
corporatura=input("inserisci il tuo somatotipo (Endomorfo, mesomorfo ed ectomorfo): ")



mydict={ 
    "nome": nome, 
    "cognome":cognome,
    "username" :usr,
    "pasasword":password,
    "indirizzo":abitazione,
    "palestra": palestra,
    "allenamento":allenamento,
    "somatotipo":corporatura

}

x = mycol.insert_one(mydict)

print("Ciao mi chiamo Movit Ai il tuo personal virtuale,monitora giorno per giorno i passi fatti; ricordati di impostare un obiettivo giornaliero ")


#implementazione di un nuovo algoritmo
#algoritmo reversed
list1=[abitazione,palestra,allenamento]
list2=[abitazione,palestra,allenamento]
print(f"1.)'list1' reversed:"
    f"{list1[::-1]}")
list2.reverse()
print(f"2.)'list2' reversed:"
     f"{list2}")


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

n=int(input("inserisci un numero, tra parentesi sono segnati i possibili risultati  ( 0[lunedi], 1[mercoledi], 2[venerdi]):  "))

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

print(nome+str(" questa settimana hai una media di ")+str(media)+str(" km ")+str("hai scelto di fare ")+str(allenamento))
#aggiunta di un nuovo algoritmo (previsioni)

print("Posso controllare anche le previsioni se oggi ottimo è per allenarsi")
n1=int(input("inserisci un numero: "))
n2=int(input("inserisci un numero: "))
tempo=['Sole','Sole','Pioggia','Pioggia','Nuvoloso','Pioggia','Sole']
temperatura=['Caldo','Caldo','Freddo','Tiepido','Tiepido','Freddo','Freddo']
uscita=['Si','Si','No','Si','Si','No','Si']
le = preprocessing.LabelEncoder() # Creo il label encoder (chiamato dunque "le")
tempo_encoded=le.fit_transform(tempo)
temperatura_encoded=le.fit_transform(temperatura)
uscita_encoded=le.fit_transform(uscita)
model = GaussianNB()
model.fit (list(zip(tempo_encoded, uscita_encoded,strict=True)),temperatura_encoded)
predicted=model.predict([[n1,n2]]) #: 2: Sole, 1=Pioggia, 0: Nuvoloso.
print("le previsioni sono:")
print(predicted.tolist()) 


print(nome+str(" ricordati che per un buon andamento monitora il tuo peso giornaliero "))


n3=int(input("insersci un numero:"))
somatotipo=['endomorfo','mesomorfo','ectomorfo','ectomorfo']
dieta=['carboidrati','proteine','zuccheri','zuccheri']
le = preprocessing.LabelEncoder()
somatotipo_encoded = le.fit_transform(somatotipo)
dieta_encoded=le.fit_transform(dieta)
model=GaussianNB()
model.fit(somatotipo_encoded.reshape(-1, 1), dieta_encoded) 
predicted=model.predict([[n3]])  
print("risultato dieta per il tipo di somatotipo: ")   #da rivedere 
print(predicted.tolist()) 


print("grafico peso giornaliero")
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

print("ciao "+str(nome)+str(" guarda gli altri utenti quali allenamenti hanno  scelto "))

#backup dei dati salvati su mongo db
df = pd.read_json('utenti.json')
print(df.to_string()) 


