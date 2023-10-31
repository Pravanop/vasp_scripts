import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

mpl.rc('font',family='Helvetica')

fig_path = '/Users/pravanomprakash/Library/CloudStorage/Box-Box/Charge Doping/Figures/Figures_revised/'
save = True

c = [-546.829035199934, -569.4737109642194, -687.1662956510604, -821.3180303227816,-919.2557180997419,
     -318.8107946332184, -329.90817352709365, -496.75081920543926, -595.9222364360685, -724.4312559205096, -876.1435258902513, -1006.582570975464]
c = [-round(i/c[0],2) for i in c]
print(c)
c0 = c[-8:]
x = [0.00, 0.02, 0.04, 0.06, 0.07]
x0 = [0.07, 0.07, 0.08, 0.12, 0.14, 0.16, 0.18, 0.20]
fontsize = 20
colors = ['#332288' , "#0077BB" , "#009988" , "#EE7733" , "#BBBBBB"]
linewidth = 3.5
alpha = 0.3
plt.figure(figsize = (5.079*4/2, 3.6*4/2))
plt.rcParams["font.family"] = "sans"
plt.axvline(x = 0.07, c = 'black', linestyle = '--', linewidth = 0.8, zorder = 1)
plt.scatter(x0, c0, marker = 'D', edgecolor='black', s = 70, facecolor = colors[3], zorder = 2)
plt.scatter(x, c[:5], marker = 'D', edgecolor='black', s = 70, facecolor = colors[2], zorder = 2)

plt.plot(x0, c0, linewidth = linewidth, alpha = alpha, c = colors[3], zorder = 3)
plt.plot(x, c[:5], linewidth = linewidth, alpha = alpha, c = colors[2], zorder = 3)
# plt.legend(['Shift-Inside', 'Shift-Across'], fontsize = fontsize, fancybox=True)
#axes labels
plt.ylabel('max($1/C_{neg}$) (normalized)', fontsize = fontsize)
plt.xlabel('Holes/f.u.', fontsize = fontsize)
plt.ylim(-0.5, -2)
#axes
plt.xticks(np.round(np.linspace(0.0, 0.20, 6),2), fontsize = fontsize, rotation = 30)
plt.yticks(np.linspace(-2, -0.5, 5).astype(int), fontsize = fontsize)

if save:
	plt.savefig(f"{fig_path}neg_capacitance.png", dpi = 300,bbox_inches='tight')
plt.show()
