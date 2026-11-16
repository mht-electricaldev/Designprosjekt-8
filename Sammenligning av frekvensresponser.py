import numpy as np
import matplotlib.pyplot as plt
import csv

header = []
data = []
filename = 'Faktisk siste målinger\Frekvensspektrum nærbilde uten filter 100 avg.csv'
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
filename1 = 'Faktisk siste målinger\Frekvensrespons nærbilde 100 avg rms.csv'
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
    time1[i] = 10**(-3)*(time1[i])

fig, (nærbilde) = plt.subplots(1,1)
fig.suptitle("Sammenligning av frekvensspektrum", fontsize=14)
nærbilde.plot(time, ch1, label="Frekvensresponsen $S(f)$")
nærbilde.plot(time1, ch11, label="Frekvensresponsen $Y(f)$")
nærbilde.set_yscale('log', base=10)
nærbilde.set_xlabel("Frekvenser [kHz]", fontsize=14)
nærbilde.set_ylabel("Amplitude [$V_{rms}$] i log-skala", fontsize=14)
nærbilde.legend(fontsize=14)
nærbilde.set_xlim([-1, 10.0])
plt.show()