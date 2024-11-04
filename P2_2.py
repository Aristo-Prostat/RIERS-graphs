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
w1 = 2 * 3.14 / T
wn = w1
N = 5

#----------------------------------------------------------------------------------------------------------------------
# Partial amount

t = np.arange(-20, 1250)
S = np.zeros(len(t))

for t1 in range(0, len(t)):

    STmp = 0
    wn = w1

    for n in range(0, N):
        ReS = (sinc((wn * tau) / 2) / wn) * math.cos((wn * tau) / 2 - (3.14 / 2))
        ImS = (sinc((wn * tau) / 2) / wn) * math.sin((wn * tau) / 2 - (3.14 / 2))    

        amp = (2 / T) * math.sqrt(math.pow(ReS, 2) + math.pow(ImS, 2))
        phase = (3.14 / 2) * (1 - np.sign((1 / wn) * math.sin((wn * tau) / 2) / ((wn * tau) / 2) * math.sin((wn * tau) / 2))) * np.sign(wn) + math.atan(((1 / wn) * math.sin((wn * tau) / 2) / ((wn * tau) / 2) * math.cos((wn * tau) / 2)) / ((1 / wn) * math.sin((wn * tau) / 2) / ((wn * tau) / 2) * math.sin((wn * tau) / 2)))

        STmp = STmp + amp * math.cos(wn * t1 + phase)

        wn += w1

    S[t1] = STmp

plt.plot(t, S)
plt.xlabel("t, мс")
plt.ylabel("SN(t), В")
plt.grid()
plt.show()

#----------------------------------------------------------------------------------------------------------------------