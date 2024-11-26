#----------------------------------------------------------------------------------------------------------------------
# Imports

import numpy as np
import matplotlib.pyplot as plt
import math

#----------------------------------------------------------------------------------------------------------------------
# Variables

tau = 60

#----------------------------------------------------------------------------------------------------------------------
# AFR

w = np.arange(-10, 10, 0.1)
H = (1 / 4) * (1 / (np.sqrt(1 + np.pow(w * tau, 2))))

plt.plot(w, H)
plt.grid()
plt.xlabel("w, рад/мс")
plt.ylabel("|H(w)|")
plt.show()

#----------------------------------------------------------------------------------------------------------------------
# PFR

w = np.arange(-10, 10, 0.1)
phase = (-1) * np.atan(w * tau)

plt.plot(w, phase)
plt.grid()
plt.xlabel("w, рад/мс")
plt.ylabel("fiH(w), рад")
plt.show()

#----------------------------------------------------------------------------------------------------------------------
# Impulse response

t = np.arange(0, 120)
h = (1 / (4 * tau)) * np.exp(((-1) * t) / tau)

plt.plot(t, h)
plt.grid()
plt.xlabel("t, мс")
plt.ylabel("h(t), мс^(-1)")
plt.show()

#----------------------------------------------------------------------------------------------------------------------
# Transitional response

t = np.arange(0, 120)
g = (1 / 4) * (1 - np.exp(((-1) * t) / tau))

plt.plot(t, g)
plt.grid()
plt.xlabel("t, мс")
plt.ylabel("g(t)")
plt.show()

#----------------------------------------------------------------------------------------------------------------------
# Linearly increasing effect

t = np.arange(0, 120)
g1 = (1 / 4) * t - (1 / 4) * tau * (1 - np.exp(((-1) * t) / tau))

plt.plot(t, g1)
plt.grid()
plt.xlabel("t, мс")
plt.ylabel("g1(t), мс")
plt.show()

#----------------------------------------------------------------------------------------------------------------------
# Input signal

t = np.arange(0, 150)
u = []

for i in range(len(t)):
    if t[i] <= 90:
        u.append((t[i] / tau))
    else:
        u.append(0)

plt.plot(t, u)
plt.grid()
plt.xlabel("t, мс")
plt.ylabel("uвх, В")
plt.show()

#----------------------------------------------------------------------------------------------------------------------
# Output signal

t = np.arange(0, 250)
u = []

for i in range(len(t)):
    if t[i] <= 90:
        u.append((1 / 4) * t[i] - (1 / 4) * tau * (1 - math.exp(((-1) * t[i]) / tau)))
    elif t[i] <= 180:
        u.append((- 1 / 4) * (t[i] - 90) + (1 / 4) * tau * (1 - math.exp(((-1) * (t[i] - 90)) / tau)) + 11)
    else:
        u.append(0)

plt.plot(t, u)
plt.grid()
plt.xlabel("t, мс")
plt.ylabel("uвых, В")
plt.show()

#----------------------------------------------------------------------------------------------------------------------