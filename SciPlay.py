import numpy as n
import matplotlib.pyplot as plt

#Simple Plot
#x = n.array([1, 2, 3, 4, 5])
#y = x + 3
#plt.plot(x, y, 'rx')
#plt.show()

#Read a file and plot
frequency, mic1, mic2 = n.loadtxt('microphones.txt', unpack=True)
plt.plot(frequency, mic1)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.show()

