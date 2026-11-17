import numpy as np
import matplotlib.pyplot as plt

def sinc(x):
    return abs(np.sin(np.pi * x)/(np.pi * x))

frekvenser = np.linspace(-0.01,5,100)
frekvenserNærbilde = np.linspace(0,0.5,100)

# fig,(ax1,ax2) = plt.subplots(1,2 )
# ax1.plot(frekvenser, sinc(frekvenser))
# ax1.set(xlim=[0,5])
# ax1.set_ylabel("Amplitude")
# ax1.set_xlabel("Frekvenser [Hz]")
# ax2.plot(frekvenserNærbilde, sinc(frekvenserNærbilde))
# ax2.plot([0,0.1], [0.99, 0.99])
# ax2.set_xlim([0,0.5])
# ax2.set_xlabel("Frekvenser [Hz]")

plt.plot(frekvenser, sinc(frekvenser),'r-', label="sinc(x)")
plt.ylabel("Amplitude [$V_{rms}$]", fontsize=14)
plt.xlabel("Frekvenser [Hz]", fontsize=14)
plt.title("Eksempel av den normaliserte sinc-funksjon i frekvensplanet med $f=1$ Hz", fontsize=14)
plt.plot([0.1,0.1], [0,0.99], 'p--', label="Grensen til rettlinjet oppførsel")
plt.xlim([-0.01,3])
plt.ylim([0,1.1])
plt.legend(fontsize=14)

plt.show()
