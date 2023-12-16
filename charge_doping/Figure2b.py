import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

mpl.rc('font' , family = 'Helvetica')

fig_path = '/Users/pravanomprakash/Library/CloudStorage/Box-Box/Charge Doping/Figures/Figures_revised/'
save = True

p42nmc_modes = {
'$\Gamma_{4}^{ -}$': [0.419, 0.419, 0.417, 0.416, 0.416, 0.415, 0.415, 0.416, 0.413, 0.413],
		'$\X_{5}^{ +}$': [0.675, 0.674, 0.672, 0.669, 0.668, 0.669, 0.669, 0.673, 0.668, 0.668],
'$\X_{5}^{ -}$': [0.194, 0.194, 0.193, 0.192, 0.191, 0.187, 0.187, 0.186, 0.183, 0.183,]
		}

pbcm_modes = {
		'$\Gamma_{1}^{+}$': [0.403, 0.446, 0.496, 0.520, 0.547, 0.590, 0.607, 0.618, 0.641, 0.652],
        '$\Gamma_{2}^{-}$': [1.335, 1.318, 1.295, 1.281, 1.267, 1.239, 1.229, 1.213, 1.211, 1.200]
		}
x = [0.00, 0.02, 0.04, 0.06, 0.08, 0.12, 0.14, 0.16, 0.18, 0.20]
p42nmc_legend = ['$\Gamma_{4}^{ -}$', '$X_{5}^{ +}$', '$X_{5}^{ -}$', 'Overall']
pbcm_legend = ['$\Gamma_{1}^{ +}$','$\Gamma_{2}^{ -}$' , 'Overall']

fontsize = 14
for key, value in pbcm_modes.items():
	plt.plot(x, value, linewidth = 3, alpha = 0.5, zorder = 2, label='_nolegend_')
	plt.scatter(x, value, marker = 's', s = 100, zorder = 1)

plt.xlabel('Holes/f.u.', fontsize = fontsize)
# plt.ylabel('Normalized Mode Amplitude', fontsize = fontsize)
plt.legend(pbcm_legend[:-1], fontsize = fontsize)
plt.xticks([0, 0.05, 0.1, 0.15, 0.2], fontsize = fontsize)
plt.yticks( fontsize = fontsize)
plt.ylim(0.15, 1.36)

plt.show()
