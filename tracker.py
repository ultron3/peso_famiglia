
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

print("Per l'auteticazione registrare la propria voce ")
#registro la voce per l'autenticazione
import sounddevice #la libreia si chiama souddevice
from scipy.io.wavfile import write
fs=44100 #sample_rate
second=5 #enter your required time..
print("Recording....\n")
record_voice=sounddevice.rec(int(second * fs),samplerate=fs,channels=2)
sounddevice.wait()
write("out.wav",fs,record_voice)
print("Finished...\nPlease Check it...")



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
    plt.ylabel("passi fatti")


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



print(nome+str(" ricordati che per un buon andamento monitora il tuo peso giornaliero  "))
print(nome+str(" posso controllare la tua dieta per il tuo tipo di corpo "))
#aggiunto algoritmo che diagnostica la dieta in base al somatotipo
n3=int(input("insersci un numero:"))
somatotipo=['endomorfo','mesomorfo','ectomorfo','ectomorfo']
dieta=['carboidrati','proteine','zuccheri','zuccheri']
le = preprocessing.LabelEncoder()
somatotipo_encoded = le.fit_transform(somatotipo)
dieta_encoded=le.fit_transform(dieta)
model=GaussianNB()
model.fit(somatotipo_encoded.reshape(-1, 1), dieta_encoded) 
predicted=model.predict([[n3]])  
print("risultato dieta per il tipo di somatotipo  ( 0[carboidrati], 1[proteine], 2[zuccheri/grassi])  : ")   #da rivedere 
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

#aggiungo la possibilità di inviare le notifiche

#da aggiornare dopo aver aggiornato a python3.11
import win10toast
toaster = win10toast.ToastNotifier()
toaster.show_toast("Contalla l'app! Hai una nuova notifica", duration=10)

