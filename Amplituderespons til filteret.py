import numpy as np
import matplotlib.pyplot as plt
import csv

header = []
data = []
filename = 'Ferdige målinger\ANettverksanalyse nærbilde.csv'
with open(filename) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    for datapoint in csvreader:
        values = [float(value) for value in datapoint]
        data.append(values)
time = [(p[0]) for p in data]
ch1 = [(p[1]) for p in data] # Nærbilde

senterfrekvens = np.max(ch1)
print(senterfrekvens)
cutOffFrekvenser = []

for i in range(len(ch1)):
    if ch1[i] >= 4.65:
        cutOffFrekvenser.append(time[i])
    if ch1[i] == 7.651374348456399:
        print(time[i])

nedreCO = cutOffFrekvenser[0]
øvreCO = cutOffFrekvenser[-1]

print(nedreCO, øvreCO)

header1 = []
data1 = []
filename1 = 'Ferdige målinger\ANettverksanalyse oversikt.csv'
with open(filename1) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    for datapoint in csvreader:
        values = [float(value) for value in datapoint]
        data1.append(values)
time1 = [(p[0]) for p in data1]
ch11 = [(p[1]) for p in data1] # oversiktsbilde

fig, (nærbilde,oversiktsbilde) = plt.subplots(1,2)
fig.suptitle("Amplituderesponsen til Deliyannis-friend-båndpassfilteret", fontsize=14)
nærbilde.plot(time, ch1, color='C1',label="amplituderespons")
nærbilde.plot([3112, 3112], [-10,10], 'r--',label="$f_{c,min}$")
nærbilde.plot([3358, 3358], [-10,10], 'r--',label="$f_{c,max}$")
nærbilde.plot([3120,3120], [-10,10], 'g--',label="$Teoretisk $f_0$")
nærbilde.plot([3221,3221], [7.65,7.65], 'bo',label="Realisert $f_0")

print("Q-faktor", (3221)/(3360-3120))

nærbilde.set_title("Nærbilde", fontsize=14)
nærbilde.set_xlabel("Frekvenser [kHz]", fontsize=14)
nærbilde.set_ylabel("Amplitude [$V_{rms}$]", fontsize=14)
nærbilde.set_xlim([2800,3800])
nærbilde.set_ylim([-10,10])
nærbilde.legend(fontsize=14,loc='upper right')

oversiktsbilde.plot(time1, ch11, color='C1', label="Amplituderesponsen")
oversiktsbilde.set_title("Oversiktsbilde", fontsize=14)
oversiktsbilde.set_xlabel("Frekvenser [Hz]", fontsize=14)
oversiktsbilde.set_ylabel("Amplitude [dB]", fontsize=14)
oversiktsbilde.legend(fontsize=14,loc='upper right')
plt.show()

