import numpy as np
import matplotlib.pyplot as plt
import csv

header = []
data = []
filename = 'Faktisk siste målinger\Frekvensrespons nærbilde 100 avg rms.csv'
with open(filename) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    for datapoint in csvreader:
        values = [float(value) for value in datapoint]
        data.append(values)
time = [(p[0]) for p in data]
ch1 = [(p[1]) for p in data] # Nærbilde

header1 = []
data1 = []
filename1 = 'Faktisk siste målinger\Frekvensrespons oversiktsbilde 1000 avg rms.csv'
with open(filename1) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    for datapoint in csvreader:
        values = [float(value) for value in datapoint]
        data1.append(values)
time1 = [(p[0]) for p in data1]
ch11 = [(p[1]) for p in data1] # oversiktsbilde

for i in range(len(time)):
    time[i] = 10**(-3)*(time[i])

for i in range(len(time1)):
    time1[i] = 10**(-6)*(time1[i])


fig, (nærbilde,oversiktsbilde) = plt.subplots(1,2)
fig.suptitle("Frekvensspektrum hele systemet", fontsize=14)
nærbilde.plot(time, ch1, label="Frekvensresponsen $Y(f)$", color='C1')
nærbilde.set_title("Nærbilde", fontsize=14)
nærbilde.set_xlabel("Frekvenser [kHz]", fontsize=14)
nærbilde.set_ylabel("Amplitude [$V_{rms}$]", fontsize=14)
nærbilde.legend(fontsize=14)
oversiktsbilde.plot(time1, ch11, label="Frekvensresponsen $Y(f)$", color='C1')
oversiktsbilde.set_yscale('log', base=10)
oversiktsbilde.set_title("Oversiktsbilde", fontsize=14)
oversiktsbilde.set_xlabel("Frekvenser [MHz]", fontsize=14)
oversiktsbilde.set_ylabel("Amplitude [$V_{rms}$] i log-skala", fontsize=14)
oversiktsbilde.legend(fontsize=14)
plt.show()
