import numpy as np
import matplotlib.pyplot as plt
import csv
header = []
data = []
filename = 'Faktisk siste målinger\Scope uten filter ikke avg.csv'
with open(filename) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    for datapoint in csvreader:
        values = [float(value) for value in datapoint]
        data.append(values)
time = [(p[0]) for p in data]
ch1 = [(p[1]) for p in data]

plt.plot(time, ch1, label="$s(t)$")
plt.xlim([-0.0005,0.0005])
plt.ylabel("Spenning [V]")
plt.xlabel("Tid (ms)")
plt.title("Oscilloskopmåling av $s(t)$")
plt.xticks([-0.0005, 0.0, 0.0005],[-0.5,0.0, 0.5])
plt.legend(fontsize=14)
plt.show()