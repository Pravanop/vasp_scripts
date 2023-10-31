import matplotlib.pyplot as plt
import numpy as np
from pymatgen.io.vasp.outputs import Vasprun

distance = [0.18, 0.43, 0.51, 0.56, 0.59,0.66, 0.84, 1.21, -1.21, -0.85, -0.67, -0.59, -0.56, -0.51, -0.43 ]
numbers = [1, 2,3, 4, 5, 6,7, 8, 9, 10, 11, 12, 13, 14, 15]
polarization = [122.31, 297.98, 350.23, 382.46, 404.6, 453.16, 570.67, -577.56, -455.88, -405.51, -382.81, -350.44,
                -298.22]
#
# fig, ax1 = plt.subplots()
# ax2 = ax1.twinx()
# ax2.plot(numbers, polarization, marker = '*', c = '#EE7733', linestyle = '-.', alpha = 0.8, linewidth = 0.8)
# ax1.plot(numbers, distance, marker = '*', c = '#009988', linestyle = '--', alpha = 0.8, linewidth = 0.8)
# ax2.axhline(y = 55, color = '#EE7733', linestyle = '-.', alpha = 0.8, linewidth = 0.8)
# ax1.set_xticks(np.arange(0, 14, 1))
# ax1.tick_params(axis = 'y', colors = '#009988')
# ax2.tick_params(axis = 'y', colors = '#EE7733')
# ax1.set_yticks(np.arange(0, 1, 0.1))
# ax2.set_yticks(np.arange(-600, 600, 100))
# ax1.set_ylabel('O4-O3 distance ($\AA$)', color = '#009988')
# ax2.set_ylabel('Polarization ($\mu C/cm^2$)', color = '#EE7733')
# ax1.set_xlabel('Layers')
# plt.show()

plt.axhline(y = 0, color = 'black', linestyle = '-.', alpha = 0.8, linewidth = 0.8)
plt.axhline(y = 0.55, color = '#EE7733', linestyle = '-.', alpha = 0.8, linewidth = 0.8)
plt.scatter(numbers, distance, marker = 'o', c = 'black')
plt.xticks(np.arange(0, 15, 1))
plt.tick_params(axis = 'y', colors = 'black')
plt.yticks(np.arange(-1.3, 1.3, 0.5))
plt.ylabel('O4-O3 distance ($\AA$)', color = 'black')
plt.xlabel('Layers')
plt.show()
