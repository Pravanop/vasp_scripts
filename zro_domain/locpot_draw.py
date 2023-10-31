import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/pravanomprakash/Downloads/zro_domain_2_0/MACROSCOPIC_AVERAGE.csv")\

zr_position = [0.1379714, 2.669739465, 5.197360127, 7.716472577, 10.23590411, 12.74434547, 15.18132038, 17.62978151, 20.14336376, 22.6645327, 25.18655102, 27.71232836, 30.25420031, 32.91362393]
y = np.ones_like(zr_position)*-12
dist = df["Distance"]
macro = df["planar"]
planar = df["Mac average"]
polarization = [0.380, 0.455, 0.499, 0.535, 0.602, 0.775, -0.739, -0.585, -0.525, -0.489, -0.448, -0.376, -0.175, 0]
fontsize = 14

plt.figure(figsize= (8.22, 2.46))

plt.plot(dist, macro, c = 'orange', linewidth = 3)
plt.plot(dist, planar, c ='blue', linewidth = 1.5)
# plt.plot(zr_position, polarization, c = "blue", linewidth = 3, marker = "D")
# plt.axhline(y = 0.5, linestyle = "--", linewidth = 2, c = "black")
plt.scatter(zr_position, y, c = 'black', alpha = 0.5)
plt.ylabel("v(z) (eV)", fontsize = fontsize)
plt.yticks(fontsize = fontsize)
plt.xticks(np.linspace(0, 35.5, 14))
plt.tick_params(labelbottom = False)
plt.show()