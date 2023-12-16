import matplotlib.pyplot as plt
import numpy as np

hole_doping = [0.20, 0.01, 0.05, 0.08, 0.19, 0.35, 0.44, 0.32, 0.14, 0.08, 0.05, 0.06, 0.20, 0.87]
polarization = [0.380, 0.455, 0.499, 0.535, 0.602, 0.775, -0.739, -0.585, -0.525, -0.489, -0.448, -0.376, -0.175, 0]
x = [0.0, 0.08, 0.15, 0.22, 0.29, 0.36, 0.43, 0.50, 0.57, 0.64, 0.71, 0.78, 0.85, 0.93]

fig, ax1 = plt.subplots(figsize=(8,5))

ax2 = ax1.twinx()
ax1.plot(x, hole_doping, c = '#CC6677', marker = 's', ms = 10)
# ax2.scatter(x, hole_doping, c = 'b')

ax1.set_xlabel('Layers')
ax1.set_ylabel('Holes/layer')
# ax2.set_ylabel('Holes/f.u.', color='b')

plt.show()