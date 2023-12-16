import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

mpl.rc('font',family='Helvetica')

fig_path = '/Users/pravanomprakash/Library/CloudStorage/Box-Box/Charge Doping/Figures/Figures_revised/'
save = True
#0	2	3	4	6	7	8	14	18	20
pbcm = np.array([132,122,116,108,98,88,77])
pbcm_1 = np.array([77, 67, 57, 47, 41, 40, 46, 63, 80, 97, 136, 178])
p42nmc = np.array([49,50,50,55,55,69,79])
p42nmc_1 = np.array([79, 89, 99, 110, 121, 133, 140, 146, 154, 160, 170, 181])
pbcm = pbcm.astype(int)
p42nmc = p42nmc.astype(int)
x0 = [0,0.02,0.03,0.04,0.05,0.06,0.07]
x1 = [0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.18, 0.20]
fontsize = 31
colors = ['#332288' , "#0077BB" , "#009988" , "#EE7733" , "#BBBBBB"]
linewidth = 3.5
alpha = 0.3
plt.figure(figsize = (3.39*5, 1.695*5))
plt.rcParams["font.family"] = "sans"
s = 200
plt.scatter(x1, pbcm_1, marker = 'D', edgecolor='black', s = s, facecolor = colors[3], zorder = 3)
plt.scatter(x0, p42nmc, marker = 's', edgecolor='black', s = s, facecolor = colors[2], zorder = 1)
plt.scatter(x1, p42nmc_1, marker = 's', edgecolor='black', s = s, facecolor = colors[2], alpha = alpha + 0.4,
            zorder = 2)
plt.scatter(x0, pbcm, marker = 'D', edgecolor='black', s = s, facecolor = colors[3], alpha = alpha + 0.4, zorder = 2)


plt.plot(x0, p42nmc, linewidth = linewidth, alpha = alpha + 0.4, c = colors[2])
plt.plot(x0, pbcm, linewidth = linewidth, alpha = alpha, c = colors[3])

plt.plot(x1, p42nmc_1, linewidth = linewidth, alpha = alpha, c = colors[2])
plt.plot(x1, pbcm_1, linewidth = linewidth, alpha = alpha + 0.4, c = colors[3])

plt.axvline(x = 0.07, linewidth = 2.2, linestyle = '--', c = 'black', zorder = 0)
plt.legend(['Shift Across', 'Shift Inside'], fontsize = fontsize, fancybox=True)

#axes labels
plt.ylabel('Barrier Energy (meV/f.u.)', fontsize = fontsize)
plt.xlabel('Holes/f.u.', fontsize = fontsize)
#axes
plt.xticks(np.round(np.linspace(0, 0.2, 7),2), fontsize = fontsize)
plt.yticks(np.linspace(20, 181, 9).astype(int), fontsize = fontsize)
if save:
	plt.savefig(f"{fig_path}energy_barrier.png", )
plt.show()
