import numpy as np
import matplotlib.pyplot as plt
import math

T = 450
tau = 90

t = np.arange(-1000, 1000)
s = []

for i in t:
    if i >= -990 and i <= -900:
        s.append(1 / tau * (i + 900) + 1)
    elif i >= -540 and i <= -450:
        s.append(1 / tau * (i + 450) + 1)
    elif i >= -90 and i <= 0:
        s.append(1 / tau * i + 1)
    elif i >= 450 and i <= 540:
        s.append(1 / tau * (i - 540) + 1)
    elif i >= 900 and i <= 990:
        s.append(1 / tau * (i - 990) + 1)
    else:
        s.append(0)


plt.plot(t, s)
plt.xlabel('t, мс')
plt.ylabel('s(t), В')
plt.grid()
plt.show()