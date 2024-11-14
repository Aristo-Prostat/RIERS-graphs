#----------------------------------------------------------------------------------------------------------------------
# Imports

import numpy as np
import matplotlib.pyplot as plt
import math

#----------------------------------------------------------------------------------------------------------------------
# ACF of video signal

tau = np.arange(-100, 100)
R = np.zeros(len(tau))

for i in range(len(tau)):
  if tau[i] >= -90 and tau[i] <= 0:
    R[i] = (math.pow(tau[i], 3) / -48600) + 2.5 * tau[i] + 210
  elif tau[i] >= 0 and tau[i] <= 90:
    R[i] = (math.pow(tau[i], 3) / 48600) - 2.5 * tau[i] + 210

plt.plot(tau, R)
plt.grid()
plt.xlabel("tau, мс")
plt.ylabel("R(tau), (В^2)*мс")
plt.show()

#----------------------------------------------------------------------------------------------------------------------
# ACF of radio signal

tau = np.arange(-100, 100)
R = np.zeros(len(tau))

for i in range(len(tau)):
  if tau[i] >= -90 and tau[i] <= 0:
    R[i] = ((math.pow(tau[i], 3) / -48600) + 2.5 * tau[i] + 210) * math.cos(7 * tau[i]) * (1 / 2)
  elif tau[i] >= 0 and tau[i] <= 90:
    R[i] = ((math.pow(tau[i], 3) / 48600) - 2.5 * tau[i] + 210) * math.cos(7 * tau[i]) * (1 / 2)

plt.plot(tau, R)
plt.grid()
plt.xlabel("tau, мс")
plt.ylabel("R(tau), (В^2)*мс")  
plt.show()

#----------------------------------------------------------------------------------------------------------------------