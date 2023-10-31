import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

mpl.rc('font',family='Helvetica')

fig_path = '/Users/pravanomprakash/Library/CloudStorage/Box-Box/Charge Doping/Figures/Figures_revised/'
save = True

pbcm = np.array([132.25, 125, 118.5, 108.45,98.5,91.25,80,65.25,50.25,37.75,5.5,-13.25,-29.25,-46.5,-60.15, -78.5,
                 -101.75,
                 -121.25,-137,-157.5])
p42nmc = np.array([10,4.25,-0.25,-2.5,-3.75,-7.25,-15.75,-26.5,-31.5,-45.75,-56.25,-71.5,-82.5,-92.75,-102.9,-110.5,
                   -118.75,-127.5, -138.9,-147.25])
pca21 = [0]*len(p42nmc)
pbcm = pbcm.astype(int)
p42nmc = p42nmc.astype(int)
x = [0,0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.11,0.12,0.13,0.14,0.15, 0.16,0.17,0.18,0.19,0.2]
fontsize = 14
colors = ['#332288' , "#0077BB" , "#009988" , "#EE7733" , "#BBBBBB"]
linewidth = 3.5
alpha = 0.3
plt.figure(figsize = (8,8))
plt.rcParams["font.family"] = "sans"
#pca21
plt.scatter(x, pca21, marker = 'o', edgecolor='black', s = 90, facecolor = colors[1])
#p42nmc
plt.scatter(x, p42nmc, marker = 's', edgecolor='black', s = 70, facecolor = colors[3])
#pbcm
plt.scatter(x, pbcm, marker = 'D', edgecolor='black', s = 70, facecolor = colors[2])

plt.plot(x, pca21, linewidth = linewidth, alpha = alpha, c = colors[1])
plt.plot(x, p42nmc, linewidth = linewidth, alpha = alpha, c = colors[3])
plt.plot(x, pbcm, linewidth = linewidth, alpha = alpha, c = colors[2])
plt.legend(['$Pca2_{1}$', '$P4_{2}/nmc$', '$Pbcm$'], fontsize = fontsize, fancybox=True)
#axes labels
plt.ylabel('Energy (meV/f.u.)', fontsize = fontsize)
plt.xlabel('Holes/f.u.', fontsize = fontsize)

#axes
plt.xticks(np.round(np.linspace(0, 0.2, 11),2), fontsize = fontsize, rotation = 30)
plt.yticks(np.linspace(-160, 140, 9).astype(int), fontsize = fontsize)
if save:
	plt.savefig(f"{fig_path}phase_stabilities.png", dpi = 300)
plt.show()
