import numpy as np
import matplotlib.pyplot as plt
import math

def sinc(x):
    if x == 0:
        return 1
    else:
        return (math.sin(x) / x)
    
tau = 90

w = np.arange(-5, 5, 0.1)
ReS = np.zeros(len(w))
ImS = np.zeros(len(w))

for i in range(0, len(w)):
    if w[i] == 0:
        ReS[i] = 1
        ImS[i] = 1
    else:
        ReS[i] = (sinc((w[i] * tau) / 2) / w[i]) * math.cos((w[i] * tau) / 2 - (3.14 / 2))
        ImS[i] = (sinc((w[i] * tau) / 2) / w[i]) * math.sin((w[i] * tau) / 2 - (3.14 / 2))

s = (np.pi / 2) * (1 - np.sign(ReS)) * np.sign(w) + np.atan(ImS / ReS)

plt.figure(figsize=(8, 6))
plt.plot(w, s)
plt.grid()
plt.show()