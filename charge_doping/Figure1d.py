import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

mpl.rc('font',family='Helvetica')

fig_path = '/Users/pravanomprakash/Library/CloudStorage/Box-Box/Charge Doping/Figures/Figures_revised/'
save = True
x = np.linspace(-1.5, 1.5, 129)
p42nmc = 193*x**2 - 492*x**4  + 345*x**6 + -66*x**8  + 22
pbcm = -255.53*x**2 + 106*x**4  + 22.22*x**6 + -6.7*x**8 + 134
fontsize = 32
colors = ['#332288' , "#0077BB" , "#009988" , "#EE7733" , "#BBBBBB"]
linewidth = 6.5
alpha = 1
plt.figure(figsize = (3.39*5, 1.695*5))
plt.rcParams["font.family"] = "sans"
plt.plot(x, p42nmc, linewidth = linewidth, alpha = alpha, c = colors[2])
plt.plot(x, pbcm, linewidth = linewidth, alpha = alpha, c = colors[3])
# plt.legend(['Shift-Inside', 'Shift-Across'], fontsize = fontsize, fancybox=True)
#axes labels
plt.ylim([0,160])
plt.xlim([-1.25, 1.25])
plt.ylabel('E', fontsize = fontsize)
plt.xlabel('P', fontsize = fontsize)

#axes
plt.tick_params(
    axis='both',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,
		left = False,# ticks along the top edge are off
    labelbottom=False,
		labelleft = False)
if save:
	plt.savefig(f"{fig_path}energy_barrier_schematic.png", dpi = 300,bbox_inches='tight')
plt.show()
