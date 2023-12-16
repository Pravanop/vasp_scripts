import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, solve


y = np.linspace(300, 1200, 1000)
ea = np.exp(-1000*(1/y- 1/1000))
eb = np.exp(-800*(1/y- 1/800))
ec = np.exp(-7000/8.314*(1/y- 1/999))

xsb = (1 - ea)/(ec - ea)
xlb = (1- 1/ea)/(1/ec - 1/ea)

plt.plot(xsb, y, c= 'black')
plt.plot(xlb, y, c = 'black')
plt.xlabel("$x_{c}$", fontsize = 14)
plt.ylabel("T (K)", fontsize = 14)
plt.xlim(0, 1)
plt.ylim(700, 1200)
plt.show()
