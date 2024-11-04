#----------------------------------------------------------------------------------------------------------------------
# Imports

import numpy as np
import matplotlib.pyplot as plt
import math

#----------------------------------------------------------------------------------------------------------------------
# Functions

def sinc(x):
    if x == 0:
        return 1
    else:
        return (math.sin(x) / x)
    
#----------------------------------------------------------------------------------------------------------------------
# Variables

tau = 90
T = 1200

#----------------------------------------------------------------------------------------------------------------------
# Signal

t = np.arange(-200, 101)

s = []
for i in t:
    if (i < -90 or i > 0):
        s.append(0)
    else:
        s.append(1 / tau * i + 1)

numPeriods = 5 
sPeriodic = np.concatenate([s] * numPeriods)  
tPeriodic = np.linspace(0, numPeriods * T, len(sPeriodic))  

plt.plot(tPeriodic, sPeriodic)
plt.xlabel('t, мс')
plt.ylabel('s(t), В')
plt.grid()
plt.xlim(0, numPeriods * T)
plt.show()  

#----------------------------------------------------------------------------------------------------------------------
# Amplitude spectrum

w = np.arange(0, 3, 0.05) 
amp = np.zeros(len(w))

for i in range(0, len(w)):
    if w[i] == 0:
        amp[i] = 1
    else:
        ReS = (sinc((w[i] * tau) / 2) / w[i]) * math.cos((w[i] * tau) / 2 - (3.14 / 2))
        ImS = (sinc((w[i] * tau) / 2) / w[i]) * math.sin((w[i] * tau) / 2 - (3.14 / 2))
        if math.sqrt(math.pow(ReS, 2) + math.pow(ImS, 2)) <= 100:
            amp[i] = (2 / T) * math.sqrt(math.pow(ReS, 2) + math.pow(ImS, 2))
        else: 
            amp[i] = 100

for i in range(len(w)):
    plt.plot([w[i], w[i]], [0, amp[i]], 'b', linewidth=1) 

plt.xlabel('w, рад/мс')
plt.ylabel('|s(w)|, В')
plt.grid()
plt.yscale('log') 
plt.show()

#----------------------------------------------------------------------------------------------------------------------
# Phase spectrum
    
w = np.arange(-10, 10, 0.1)
w[100] = 1

phase = (3.14 / 2) * (1 - np.sign((1 / w) * np.sin((w * tau) / 2) / ((w * tau) / 2) * np.sin((w * tau) / 2))) * np.sign(w) + np.atan(((1 / w) * np.sin((w * tau) / 2) / ((w * tau) / 2) * np.cos((w * tau) / 2)) / ((1 / w) * np.sin((w * tau) / 2) / ((w * tau) / 2) * np.sin((w * tau) / 2)))

plt.plot(w, phase, 'o', markersize=4) 

for i in range(len(w)):
    plt.plot([w[i], w[i]], [0, phase[i]], 'b', linewidth=1)  

plt.xlabel('w, рад/мс')
plt.ylabel('fi(w), рад')
plt.grid()
plt.show()

#----------------------------------------------------------------------------------------------------------------------