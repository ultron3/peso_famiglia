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


