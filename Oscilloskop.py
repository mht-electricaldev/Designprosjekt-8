import numpy as np
import matplotlib.pyplot as plt
import csv

header = []
data = []
filename = 'Faktisk siste målinger\Scope nærbilde ikke avg.csv'
with open(filename) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    for datapoint in csvreader:
        values = [float(value) for value in datapoint]
        data.append(values)
time = [(p[0]) for p in data]
ch1 = [(p[1]) for p in data]

header1 = []
data1 = []
filename1 = 'Faktisk siste målinger\Scope uten filter ikke avg.csv'
with open(filename1) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    for datapoint in csvreader:
        values = [float(value) for value in datapoint]
        data1.append(values)
time1 = [(p[0]) for p in data1]
ch11 = [(p[1]) for p in data1] 

plt.plot(time1, ch11, label="$s(t)$")
plt.plot(time,ch1, label="$y(t)$")
plt.ylabel("Spenning [V]")
plt.xlabel("Tid [ms]")
plt.title("Sammenligning mellom oscilloskopet til $y(t)$ og $s(t)$")
plt.xlim([-0.0005,0.0005])
plt.legend()
plt.show()