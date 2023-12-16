import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/pravanomprakash/Library/CloudStorage/Box-Box/ZrO_domain/zro_domain_2_0/MACROSCOPIC_AVERAGE.csv")\

zr_position = [0.1379714, 2.669739465, 5.197360127, 7.716472577, 10.23590411, 12.74434547, 15.18132038, 17.62978151, 20.14336376, 22.6645327, 25.18655102, 27.71232836, 30.25420031, 32.91362393]
y = np.ones_like(zr_position)*-12
dist = df["Distance"]
planar = df["planar"] + 12.29
macro = df["Mac average"] + 0.75
polarization = [0.380, 0.455, 0.499, 0.535, 0.602, 0.775, -0.739, -0.585, -0.525, -0.489, -0.448, -0.376, -0.175, 0]
fontsize = 14
# print(len(macro))
# plt.figure(figsize= (8.22, 2.46))
fig, ax1 = plt.subplots(figsize=(8,5))

ax2 = ax1.twinx()
# plt.plot(dist, macro, c = 'orange', linewidth = 3)
ax1.axhline(y = 0, c = 'black', linestyle = '--', linewidth = 0.8)
ax1.plot(dist, planar, c ='#CC6677', linewidth = 1.5)
# ax2.plot(zr_position, polarization, c = 'red', linewidth = 1.5)
ax1.set_ylabel("v(z) (V)", fontsize = fontsize)
# ax2.set_ylabel("Polarization $C/m^2$")
# plt.yticks(fontsize = fontsize)
# plt.xticks(np.linspace(0, 35.5, 14))
# plt.tick_params(labelbottom = False)
plt.show()