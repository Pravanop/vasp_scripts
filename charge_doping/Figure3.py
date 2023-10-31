import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from scipy.optimize import curve_fit

mpl.rc('font' , family = 'Helvetica')

fig_path = '/Users/pravanomprakash/Library/CloudStorage/Box-Box/Charge Doping/Figures/Figures_revised/'
save = True

def flipper(arr) :
	arr = arr.astype(int)
	temp = np.flip(arr[1 :])
	return np.concatenate((temp , arr))

def energy_func(x , a , b , c , d) :
	return (a / 2) * (x ** 2) + (b / 4) * (x ** 4) + (c / 6) * (x ** 6) + (d / 8) * (x ** 8)

def electric_func(x , a , b , c , d) :
	return a * x + b * x ** 3 + c * x ** 5 + d * x ** 7

def capacitance_func(x , a , b , c , d) :
	return a + 3 * b * x ** 2 + 5 * c * x ** 4

x = np.linspace(-1.5 , 1.5 , 39)
c = []
p42nmc_000 = np.array(
		[0 , 4 , 14 , 25 , 34 , 39 , 39 , 35 , 28 , 18 , 7 , -3 , -9 , -10 , -4 , 10 , 33 , 68 , 115 , 174]
		)
p42nmc_000 = flipper(p42nmc_000)
popt , _ = curve_fit(energy_func , x , p42nmc_000)
print(popt)
energy_000 = energy_func(x , *popt)
electric_000 = electric_func(x , *popt)
c_000 = capacitance_func(x , *popt)
c.append(min(c_000))
p42nmc_002 = np.array(
		[0 , 4 , 15 , 26 , 36 , 42 , 43 , 39 , 32 , 21 , 11 , 1 , -5 , -6 , -1 , 14 , 38 , 73 , 121 , 183]
		)
p42nmc_002 = flipper(p42nmc_002)
popt , _ = curve_fit(energy_func , x , p42nmc_002)
print(popt)
energy_002 = energy_func(x , *popt)
electric_002 = electric_func(x , *popt)
c_002 = capacitance_func(x , *popt)
c.append(min(c_002))
p42nmc_004 = np.array([0 , 5 , 19 , 34 , 46 , 53 , 54 , 50 , 42 , 31 , 19 , 8 , 1 , -1 , 6 , 23 , 51 , 93 , 149 , 222])
p42nmc_004 = flipper(p42nmc_004)
popt , _ = curve_fit(energy_func , x , p42nmc_004)
print(popt)
energy_004 = energy_func(x , *popt)
electric_004 = electric_func(x , *popt)
c_004 = capacitance_func(x , *popt)
c.append(min(c_004))

p42nmc_006 = np.array(
		[0 , 7 , 24 , 43 , 58 , 66 , 69 , 65 , 56 , 44 , 31 , 19 , 11 , 9 , 16 , 34 , 66 , 113 , 176 , 258]
		)
p42nmc_006 = flipper(p42nmc_006)
popt , _ = curve_fit(energy_func , x , p42nmc_006)
print(popt)
energy_006 = energy_func(x , *popt)
electric_006 = electric_func(x , *popt)
c_006 = capacitance_func(x , *popt)
c.append(min(c_006))
p42nmc_007 = np.array(
		[0, 8, 27, 49, 66, 76, 79, 75, 66, 53, 39, 26, 17, 15, 23, 44, 79, 131, 201, 292]
		)
p42nmc_007 = flipper(p42nmc_007)
popt , _ = curve_fit(energy_func , x , p42nmc_007)
print(popt)
energy_007 = energy_func(x , *popt)
electric_007 = electric_func(x , *popt)
c_007 = capacitance_func(x , *popt)
c.append(min(c_007))

pbcm_007 = np.array(
		[0 , 0 , 0 , 0 , -1 , -5 , -11 , -20 , -32 , -45 , -57 , -68 , -76 , -77 , -71 , -56 , -32 , 3 , 47 , 102]
		)
pbcm_007 = flipper(pbcm_007)
popt , _ = curve_fit(energy_func , x , pbcm_007)
print(popt)
energy_007 = energy_func(x , *popt)
electric_007 = electric_func(x , *popt)
c_007 = capacitance_func(x , *popt)
c.append(min(c_007))
pbcm_008 = np.array(
		[0 , 0 , 2 , 3 , 3 , 1 , -4 , -11 , -21 , -33 , -45 , -55 , -63 , -64 , -58 , -44 , -20 , 15 , 60 , 116]
		)
pbcm_008 = flipper(pbcm_008)
popt , _ = curve_fit(energy_func , x , pbcm_008)
print(popt)
energy_008 = energy_func(x , *popt)
electric_008 = electric_func(x , *popt)
c_008 = capacitance_func(x , *popt)
c.append(min(c_008))

pbcm_012 = np.array([0 , 2 , 8 , 16 , 24 , 30 , 35 , 36 , 32 , 25 , 15 , 4 , -3 , -5 , 2 , 19 , 47 , 86 , 137 , 201])
pbcm_012 = flipper(pbcm_012)
popt , _ = curve_fit(energy_func , x , pbcm_012)
print(popt)
energy_012 = energy_func(x , *popt)
electric_012 = electric_func(x , *popt)
c_012 = capacitance_func(x , *popt)
c.append(min(c_012))

pbcm_014 = np.array([0, 3, 12, 24, 36, 48, 57, 62, 63, 58, 50, 40, 33, 32, 39, 57, 86, 128, 183, 251])
pbcm_014 = flipper(pbcm_014)
popt , _ = curve_fit(energy_func , x , pbcm_014)
print(popt)
energy_014 = energy_func(x , *popt)
electric_014 = electric_func(x , *popt)
c_014 = capacitance_func(x , *popt)
c.append(min(c_014))
pbcm_016 = np.array(
		[0 , 4 , 17 , 33 , 51 , 68 , 82 , 93 , 97 , 96 , 88 , 79 , 72 , 71 , 78 , 97 , 128 , 171 , 229 , 299]
		)
pbcm_016 = flipper(pbcm_016)
popt , _ = curve_fit(energy_func , x , pbcm_016)
print(popt)
energy_016 = energy_func(x , *popt)
electric_016 = electric_func(x , *popt)
c_016 = capacitance_func(x , *popt)
c.append(min(c_016))
pbcm_018 = np.array(
		[0 , 6 , 22 , 44 , 68 , 91 , 112 , 127 , 135 , 136 , 130 , 122 , 114 , 113 , 121 , 141 , 173 , 220 , 280 , 356]
		)
pbcm_018 = flipper(pbcm_018)
popt , _ = curve_fit(energy_func , x , pbcm_018)
print(popt)
energy_018 = energy_func(x , *popt)
electric_018 = electric_func(x , *popt)
c_018 = capacitance_func(x , *popt)
c.append(min(c_018))

pbcm_020 = np.array(
		[0 , 8 , 28 , 55 , 84 , 114 , 141 , 161 , 173 , 178 , 176 , 167 , 160 , 159 , 167 , 187 , 221 , 268 , 331 , 410]
		)
pbcm_020 = flipper(pbcm_020)
popt , _ = curve_fit(energy_func , x , pbcm_020)
print(popt)
energy_020 = energy_func(x , *popt)
electric_020 = electric_func(x , *popt)
c_020 = capacitance_func(x , *popt)
c.append(min(c_020))

print(min(c_008) , min(c_014) , min(c_018) , min(c_020))
fontsize = 16
colors = ["#F9D576" , "#FD9A44" , "#E94C1F" , "#A01813"]
colors0 = ["#9DCCEF" , "#42A7C6" , "#238F9D" , "#125A56"]
# colors.reverse()
linewidth = 4.5
alpha = 0.45

fig , axs = plt.subplots(2 , 1 , sharex = True , figsize = (6.77 * 2 , 3.39 * 2))
plt.rcParams["font.family"] = "sans"
plt.subplots_adjust(hspace = 0)
count = 0
size = 50
marker = 'D'
for ax in axs :
	if count == 0 :
		ax.plot(x , electric_000 , linewidth = linewidth , alpha = alpha , c = colors0[0] , zorder = 3)
		ax.plot(x , electric_002 , linewidth = linewidth , alpha = alpha , c = colors0[1] , zorder = 3)
		ax.plot(x , electric_004 , linewidth = linewidth , alpha = alpha , c = colors0[2] , zorder = 3)
		ax.plot(x , electric_006 , linewidth = linewidth , alpha = alpha , c = colors0[3] , zorder = 3)
		ax.axhline(y = 0 , c = 'black' , linestyle = '-' , linewidth = 1 , alpha = 1 , zorder = 1)
		ax.axvline(x = 0 , c = 'black' , linestyle = '-' , linewidth = 1 , alpha = 1 , zorder = 2)
		
		ax.scatter(
			x , electric_000 , marker = marker , edgecolor = 'black' , s = size , facecolor = colors0[0] ,
			zorder = 4
			)
		ax.scatter(
			x , electric_002 , marker = marker , edgecolor = 'black' , s = size , facecolor = colors0[1] ,
			zorder = 4
			)
		ax.scatter(
			x , electric_004 , marker = marker , edgecolor = 'black' , s = size , facecolor = colors0[2] , zorder = 4
			)
		ax.scatter(
			x , electric_006 , marker = marker , edgecolor = 'black' , s = size , facecolor = colors0[3] , zorder = 4
			)
		ax.set_ylim(-500 , 500)
		ax.tick_params(axis = 'both' , which = 'major' , labelsize = fontsize , top = False)
		ax.legend(
				[0.0 , 0.02 , 0.04 , '0.06'] , fontsize = fontsize , loc = "upper right", ncols = 4
				)
		count += 1
	else :
		
		ax.plot(x , electric_008 , linewidth = linewidth , alpha = alpha , c = colors[0] , zorder = 3)
		ax.plot(x , electric_012 , linewidth = linewidth , alpha = alpha , c = colors[1] , zorder = 3)
		ax.plot(x , electric_016 , linewidth = linewidth , alpha = alpha , c = colors[2] , zorder = 3)
		ax.plot(x , electric_020 , linewidth = linewidth , alpha = alpha , c = colors[3] , zorder = 3)
		ax.axhline(y = 0 , c = 'black' , linestyle = '-' , linewidth = 1 , alpha = 1 , zorder = 1)
		ax.axvline(x = 0 , c = 'black' , linestyle = '-' , linewidth = 1 , alpha = 1 , zorder = 2)
		
		ax.scatter(
			x , electric_008 , marker = marker , edgecolor = 'black' , s = size , facecolor = colors[0] , zorder = 4
			)
		ax.scatter(
			x , electric_012 , marker = marker , edgecolor = 'black' , s = size , facecolor = colors[1] ,
			zorder = 4
			)
		ax.scatter(
			x , electric_016 , marker = marker , edgecolor = 'black' , s = size , facecolor = colors[2] ,
			zorder = 4
			)
		ax.scatter(
			x , electric_020 , marker = marker , edgecolor = 'black' , s = size , facecolor = colors[3] , zorder = 4
			)
		ax.set_xlabel('Normalized Polarization' , fontsize = fontsize)
		ax.set_xlim([-1 , 1])
		ax.set_ylim(-500 , 500)
		ax.tick_params(axis = 'both' , which = 'major' , labelsize = fontsize , top = True)
		ax.legend([0.08 , 0.12 , 0.16 , '0.20'] , fontsize = fontsize, ncols = 4, loc = 'lower right')
		count += 1
# axes labels
fig.text(0.05 , 0.5 , 'Electric Field' , va = 'center' , rotation = 'vertical' , fontsize = fontsize)

if save :
	plt.savefig(f"{fig_path}electric_field.png" , dpi = 300 , bbox_inches = 'tight')
plt.show()
