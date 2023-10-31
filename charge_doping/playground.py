import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import pandas as pd
path = [[174 , 64 , 6 , -10 , 2 , 23 , 39 , 36 , 16 , 0 , 16 , 36 , 39 , 23 , 2 , -10 , 6 , 64 , 174],
        [197 , 79 , 18 , 3 , 15 , 37 , 51 , 44 , 18 , 0 , 18 , 44 , 51 , 37 , 15 , 3 , 18 , 79 , 197],
        [138 ,33 ,-25 ,-41 ,-28 ,-4 ,11 ,13 ,6 ,0 ,6 ,13 ,11 ,-4 ,-28 ,-41 ,-25 ,33 ,138],
        [240 ,121 ,56 ,39 ,52 ,67 ,63 ,41 ,14 ,0 ,14 ,41 ,63 ,67 ,52 ,39 ,56 ,121 ,240],
        [384 ,239 ,160 ,139 ,152 ,159 ,134 ,81 ,25 ,0 ,25 ,81 ,134 ,159 ,152 ,139 ,160 ,239 ,384]]


doping = [0, 0.05, 0.1, 0.15, 0.2]

factor = 66
x = np.linspace(-1.5*factor, 1.5*factor, 19)
def func(x, a, b ,c , d):
    return (a/2)*(x**2) + (b/4)*(x**4) + (c/6)*(x**6) + (d/8)*(x**8)
    # return (a/2)*((1-s)**2)*(x**2) + (b/4)*((1-s)**4)*(x**4) + (c/6)*(x**6) + (e/8)*(x**8)
popt_list = []
for i in range(len(doping)):
    popt, pcov = curve_fit(func, x, path[i])
    popt_list.append(popt)
    print(f"{doping[i]}:{popt}")

popt_list = np.array(popt_list)

def electric_func(x, a, b, c, d):
    return a*x + b*x**3 + c*x**5 + d*x**7

def capacitance_func(x, a, b, c, d):
    return a + 3*b*x**2 + 5*c*x**4
    # return a + 3*b*x**2 + 5*c*x**4
size = 40
marker = 'D'
linewidth = 3.5
alpha = 0.3
colors = ['#F57634' , "#E94C1F" ,"#92C5DE" , "#4393C3", "#2166AC"]
x = np.linspace(-1, 1, 19)
fig, ax = plt.subplots(nrows = 2, ncols = 1)
for i in range(len(doping)) :
    ax[0].scatter(x,electric_func(x*factor , *popt_list[i]), marker = marker , edgecolor = 'black' , s = size ,
                  facecolor =
    colors[i])
    ax[1].scatter(
        x , capacitance_func(x*factor , *popt_list[i]) , marker = marker , edgecolor = 'black' , s = size , facecolor =
        colors[i]
        )
    print(min(capacitance_func(x , *popt_list[i])))
for i in range(len(doping)):
    ax[0].plot(x , electric_func(x*factor , *popt_list[i]) , linewidth = linewidth , alpha = alpha , c = colors[i])
    ax[1].plot(x , capacitance_func(x*factor , *popt_list[i]) , linewidth = linewidth , alpha = alpha , c = colors[i])
    ax[1].set_ylim(-1, 1)
    # ax[1].set_xticks(np.linspace(-1, 1, 19))
# ax[0].set_ylabel('G')
ax[0].set_ylabel('E')
ax[1].set_ylabel('1/C')
ax[1].set_xlabel('Normalized Polarization')
plt.subplots_adjust(hspace = 0)
plt.legend(doping, ncols = 5)
plt.axhline(y = 0, c = 'black', linestyle = '--')
plt.show()
