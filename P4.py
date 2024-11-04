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
T = 450
w0 = 10

#----------------------------------------------------------------------------------------------------------------------
# Signal

t = np.arange(-1000, 1000)
s = []

for i in t:
    if i >= -990 and i <= -900:
        s.append((1 / tau * (i + 900) + 1) * math.cos(w0 * i))
    elif i >= -540 and i <= -450:
        s.append((1 / tau * (i + 450) + 1) * math.cos(w0 * i))
    elif i >= -90 and i <= 0:
        s.append((1 / tau * i + 1) * math.cos(w0 * i))
    elif i >= 450 and i <= 540:
        s.append((1 / tau * (i - 540) + 1) * math.cos(w0 * i))
    elif i >= 900 and i <= 990:
        s.append((1 / tau * (i - 990) + 1) * math.cos(w0 * i))
    else:
        s.append(0)

plt.plot(t, s)
plt.xlabel('t, мс')
plt.ylabel('s(t), В')
plt.grid()
plt.show()

#----------------------------------------------------------------------------------------------------------------------
# Amplitude spectrum in the negative region

w = np.arange(-2 - w0, 2 - w0, 0.1) 
amp = np.zeros(len(w))

for i in range(0, len(w)):
    if w[i] == 0:
        amp[i] = 1
    else:
        ReS = (sinc(((w[i] + w0) * tau) / 2) / (w[i] + w0)) * math.cos(((w[i] + w0) * tau) / 2 - (3.14 / 2))
        ImS = (sinc(((w[i] + w0) * tau) / 2) / (w[i] + w0)) * math.sin(((w[i] + w0) * tau) / 2 - (3.14 / 2))
        if math.sqrt(math.pow(ReS, 2) + math.pow(ImS, 2)) <= 100:
            amp[i] = math.sqrt(math.pow(ReS, 2) + math.pow(ImS, 2))
        else: 
            amp[i] = 100

plt.figure(figsize=(8, 6))
plt.plot(w, amp, 'o', markersize=4) 
for i in range(len(w)):
    plt.plot([w[i], w[i]], [0, amp[i]], 'b', linewidth=1) 

plt.xlabel('w, рад/мс')
plt.ylabel('|s(w)|, В')
plt.grid()
plt.yscale('log')  
plt.show()

#----------------------------------------------------------------------------------------------------------------------
# Amplitude spectrum in the positive region

w = np.arange(-2 + w0, 2 + w0, 0.1) 
amp = np.zeros(len(w))

for i in range(0, len(w)):
    if w[i] == 0:
        amp[i] = 1
    else:
        ReS = (sinc(((w[i] - w0) * tau) / 2) / (w[i] - w0)) * math.cos(((w[i] - w0) * tau) / 2 - (3.14 / 2))
        ImS = (sinc(((w[i] - w0) * tau) / 2) / (w[i] - w0)) * math.sin(((w[i] - w0) * tau) / 2 - (3.14 / 2))
        if math.sqrt(math.pow(ReS, 2) + math.pow(ImS, 2)) <= 100:
            amp[i] = math.sqrt(math.pow(ReS, 2) + math.pow(ImS, 2))
        else: 
            amp[i] = 100

plt.figure(figsize=(8, 6))
plt.plot(w, amp, 'o', markersize=4) 
for i in range(len(w)):
    plt.plot([w[i], w[i]], [0, amp[i]], 'b', linewidth=1) 

plt.xlabel('w, рад/мс')
plt.ylabel('|s(w)|, В')
plt.grid()
plt.yscale('log')  
plt.show()

#----------------------------------------------------------------------------------------------------------------------
# Phase spectrum in the negative region

w = np.arange(-5 - w0, 5 - w0, 0.1)
wNormal = np.arange(-5, 5, 0.1)
wNormal[50] = 1

phase = (3.14 / 2) * (1 - np.sign((1 / wNormal) * np.sin((wNormal * tau) / 2) / ((wNormal * tau) / 2) * np.sin((wNormal * tau) / 2))) * np.sign(wNormal) + np.atan(((1 / wNormal) * np.sin((wNormal * tau) / 2) / ((wNormal * tau) / 2) * np.cos((wNormal * tau) / 2)) / ((1 / wNormal) * np.sin((wNormal * tau) / 2) / ((wNormal * tau) / 2) * np.sin((wNormal * tau) / 2)))

plt.figure(figsize=(8, 6))
plt.plot(w, phase, 'o', markersize=4) 
for i in range(len(w)):
    plt.plot([w[i], w[i]], [0, phase[i]], 'b', linewidth=1) 

plt.xlabel('w, рад/мс')
plt.ylabel('fi(w), рад')
plt.grid()
plt.show()

#----------------------------------------------------------------------------------------------------------------------
# Phase spectrum in the positive region

w = np.arange(-5 + w0, 5 + w0, 0.1)
wNormal = np.arange(-5, 5, 0.1)
wNormal[50] = 1

phase = (3.14 / 2) * (1 - np.sign((1 / wNormal) * np.sin((wNormal * tau) / 2) / ((wNormal * tau) / 2) * np.sin((wNormal * tau) / 2))) * np.sign(wNormal) + np.atan(((1 / wNormal) * np.sin((wNormal * tau) / 2) / ((wNormal * tau) / 2) * np.cos((wNormal * tau) / 2)) / ((1 / wNormal) * np.sin((wNormal * tau) / 2) / ((wNormal * tau) / 2) * np.sin((wNormal * tau) / 2)))

plt.figure(figsize=(8, 6))
plt.plot(w, phase, 'o', markersize=4) 
for i in range(len(w)):
    plt.plot([w[i], w[i]], [0, phase[i]], 'b', linewidth=1) 

plt.xlabel('w, рад/мс')
plt.ylabel('fi(w), рад')
plt.grid()
plt.show()

#----------------------------------------------------------------------------------------------------------------------