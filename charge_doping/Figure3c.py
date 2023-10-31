import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

mpl.rc('font',family='Helvetica')

fig_path = '/Users/pravanomprakash/Library/CloudStorage/Box-Box/Charge Doping/Figures/Figures_revised/'
save = True

x = np.linspace(-0.5, 0.5, 101)
y = 1/(1 + 2*x)
fontsize = 20
colors = ['#332288' , "#0077BB" , "#009988" , "#EE7733" , "#BBBBBB"]
linewidth = 3.5
alpha = 0.3
plt.figure(figsize = (3.39*2, 3.39*2))
plt.rcParams["font.family"] = "sans"

plt.plot(x, y, linewidth = linewidth, alpha = 0.9, c = colors[0], zorder = 3)
# plt.legend(['Shift-Inside', 'Shift-Across'], fontsize = fontsize, fancybox=True)
#axes labels
plt.ylabel('Amplification', fontsize = fontsize)
plt.xlabel('1/C', fontsize = fontsize)
plt.ylim(0,10)
# plt.xlim(-1/c2 - 1, 1)
#axes
plt.xticks(np.round(np.linspace(-0.5, 0.5, 6),2), fontsize = fontsize)
plt.yticks(np.linspace(0, 10, 6).astype(int), fontsize = fontsize)

if save:
	plt.savefig(f"{fig_path}voltage_amplification.png", dpi = 300,bbox_inches='tight')
plt.show()
