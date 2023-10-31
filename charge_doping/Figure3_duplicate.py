import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from scipy.optimize import curve_fit
mpl.rc('font',family='Helvetica')

fig_path = '/Users/pravanomprakash/Library/CloudStorage/Box-Box/Charge Doping/Figures/Figures_revised/'
save = False
def flipper(arr):
	arr = arr.astype(int)
	temp = np.flip(arr[1:])
	return np.concatenate((temp, arr))

def energy_func(x, a, b ,c , d):
	return (a/2)*(x**2) + (b/4)*(x**4) + (c/6)*(x**6) + (d/8)*(x**8)

def electric_func(x, a, b, c, d):
    return a*x + b*x**3 + c*x**5 + d*x**7

def capacitance_func(x, a, b, c, d):
    return a + 3*b*x**2 + 5*c*x**4

x = np.linspace(-1.5, 1.5, 39)

p42nmc_002 = np.array([0,4,15,26,36,42,43,39,32,21,11,1,-5,-6,-1,14,38,73,121,183])
p42nmc_002 = flipper(p42nmc_002)
popt, _ = curve_fit(energy_func, x, p42nmc_002)
print(popt)
energy_002 = energy_func(x, *popt)
electric_002 = electric_func(x, *popt)
c_002 = capacitance_func(x, *popt)

p42nmc_003 = np.array([0,4,15,27,38,44,45,42,34,24,13,4,-3,-4,2,16,40,76,125,187])
p42nmc_003 = flipper(p42nmc_003)
popt, _ = curve_fit(energy_func, x, p42nmc_003)
print(popt)
energy_003 = energy_func(x, *popt)
electric_003 = electric_func(x, *popt)
c_003 = capacitance_func(x, *popt)

p42nmc_004 = np.array([0,5,19,34,46,53,54,50,42,31,19,8,1,-1,6,23,51,93,149,222])
p42nmc_004 = flipper(p42nmc_004)
popt, _ = curve_fit(energy_func, x, p42nmc_004)
print(popt)
energy_004 = energy_func(x, *popt)
electric_004 = electric_func(x, *popt)
c_004 = capacitance_func(x, *popt)

p42nmc_006 = np.array([0,7,24,43,58,66,69,65,56,44,31,19,11,9,16,34,66,113,176,258])
p42nmc_006 = flipper(p42nmc_006)
popt, _ = curve_fit(energy_func, x, p42nmc_006)
print(popt)
energy_006 = energy_func(x, *popt)
electric_006 = electric_func(x, *popt)
c_006 = capacitance_func(x, *popt)


pbcm_008 = np.array([0,0,2,3,3,1,-4,-11,-21,-33,-45,-55,-63,-64,-58,-44,-20,15,60,116])
pbcm_008 = flipper(pbcm_008)
popt, _ = curve_fit(energy_func, x, pbcm_008)
print(popt)
energy_008 = energy_func(x, *popt)
electric_008 = electric_func(x, *popt)
c_008 = capacitance_func(x, *popt)

pbcm_014 = np.array([0,1,6,16,26,35,42,46,46,40,31,20,13,12,20,38,67,110,165,233])
pbcm_014 = flipper(pbcm_014)
popt, _ = curve_fit(energy_func, x, pbcm_014)
print(popt)
energy_014 = energy_func(x, *popt)
electric_014 = electric_func(x, *popt)
c_014 = capacitance_func(x, *popt)

pbcm_018 = np.array([0,6,22,44,68,91,112,127,135,136,130,122,114,113,121,141,173,220,280,356])
pbcm_018 = flipper(pbcm_018)
popt, _ = curve_fit(energy_func, x, pbcm_018)
print(popt)
energy_018 = energy_func(x, *popt)
electric_018 = electric_func(x, *popt)
c_018 = capacitance_func(x, *popt)

pbcm_020 = np.array([0,8,28,55,84,114,141,161,173,178,176,167,160,159,167,187,221,268,331,410])
pbcm_020 = flipper(pbcm_020)
popt, _ = curve_fit(energy_func, x, pbcm_020)
print(popt)
energy_020 = energy_func(x, *popt)
electric_020 = electric_func(x, *popt)
c_020 = capacitance_func(x, *popt)

print(min(c_008), min(c_014), min(c_018),min(c_020))
fontsize = 16
colors = ["#FEDA8B" , "#F67E4B", "#DD3D2D", "#A50026"]
# colors.reverse()
linewidth = 4.5
alpha = 0.45

fig, axs = plt.subplots(2, 1, figsize = (3.81*3, 2.54*3))
plt.rcParams["font.family"] = "sans"
plt.subplots_adjust(hspace = 0)
count = 0
for ax in axs:
	if count == 0:
		# ax.plot(x ,electric_002 ,  linewidth = linewidth , alpha = alpha , c = colors[0] , zorder = 3)
		# ax.plot(x ,electric_003 ,  linewidth = linewidth , alpha = alpha , c = colors[1] , zorder = 3)
		# ax.plot(x ,electric_004 ,  linewidth = linewidth , alpha = alpha , c = colors[2] , zorder = 3)
		# ax.plot(x ,electric_006 ,  linewidth = linewidth , alpha = alpha , c = colors[3] , zorder = 3)
		ax.plot(x ,electric_008 ,  linewidth = linewidth , alpha = alpha , c = colors[0] , zorder = 3)
		ax.plot(x ,electric_014 ,  linewidth = linewidth , alpha = alpha , c = colors[1] , zorder = 3)
		ax.plot(x ,electric_018 ,  linewidth = linewidth , alpha = alpha , c = colors[2] , zorder = 3)
		ax.plot(x , electric_020 , linewidth = linewidth , alpha = alpha , c = colors[3] , zorder = 3)
		ax.axhline(y =0, c = 'black', linestyle = '-', linewidth = 2, alpha = 0.5, zorder = 1)
		ax.axvline(x =0, c = 'black', linestyle = '-', linewidth = 2, alpha = 0.5, zorder = 2)
		size = 50
		marker = 'D'
		# ax.scatter(x,electric_002,  marker = marker, edgecolor='black', s = size, facecolor = colors[0], zorder=4)
		# ax.scatter(x,electric_003,  marker = marker, edgecolor='black', s = size, facecolor = colors[1], zorder=4)
		# ax.scatter(x,electric_004,  marker = marker, edgecolor='black', s = size, facecolor = colors[2], zorder=4)
		# ax.scatter(x,electric_006,  marker = marker, edgecolor='black', s = size, facecolor = colors[3], zorder=4)
		ax.scatter(x,electric_008,  marker = marker, edgecolor='black', s = size, facecolor = colors[0], zorder=4)
		ax.scatter(x,electric_014,   marker = marker, edgecolor='black', s = size, facecolor = colors[1], zorder=4)
		ax.scatter(x,electric_018,   marker = marker, edgecolor='black', s = size, facecolor = colors[2], zorder=4)
		ax.scatter(x,electric_020,  marker = marker , edgecolor = 'black' , s = size , facecolor = colors[3] ,
		           zorder = 4)
		# ax.set_yticks(np.linspace(-140, 100, 5).astype(int))
		ax.label_outer()
		ax.tick_params(axis = 'both' , which = 'major' , labelsize = fontsize, top = False)
			# ax.set_xlim([-1, 1])
			# ax.set_ylim([-250, 250])
		ax.set_ylabel('E', fontsize = fontsize)
		yticks = ax.yaxis.get_major_ticks()
		yticks[-1].label1.set_visible(False)
		count +=1
	else:
		# ax.plot(x , c_002 , linewidth = linewidth , alpha = alpha , c = colors[0] , zorder = 3)
		# ax.plot(x , c_003 , linewidth = linewidth , alpha = alpha , c = colors[1] , zorder = 3)
		# ax.plot(x , c_004 , linewidth = linewidth , alpha = alpha , c = colors[2] , zorder = 3)
		# ax.plot(x , c_006 , linewidth = linewidth , alpha = alpha , c = colors[3] , zorder = 3)
		ax.plot(x , c_008 , linewidth = linewidth , alpha = alpha , c = colors[0] , zorder = 3)
		ax.plot(x , c_014 , linewidth = linewidth , alpha = alpha , c = colors[1] , zorder = 3)
		ax.plot(x , c_018 , linewidth = linewidth , alpha = alpha , c = colors[2] , zorder = 3)
		ax.plot(x , c_020 , linewidth = linewidth , alpha = alpha , c = colors[3] , zorder = 3)
		ax.axhline(y = 0 , c = 'black' , linestyle = '-' , linewidth = 2 , alpha = 0.5 , zorder = 1)
		ax.axvline(x = 0 , c = 'black' , linestyle = '-' , linewidth = 2 , alpha = 0.5 , zorder = 2)
		size = 50
		marker = 'D'
		# ax.scatter(x , c_002 , marker = marker , edgecolor = 'black' , s = size , facecolor = colors[0] , zorder = 4)
		# ax.scatter(x , c_003 , marker = marker , edgecolor = 'black' , s = size , facecolor = colors[1] , zorder = 4)
		# ax.scatter(x , c_004 , marker = marker , edgecolor = 'black' , s = size , facecolor = colors[2] , zorder = 4)
		# ax.scatter(x , c_006 , marker = marker , edgecolor = 'black' , s = size , facecolor = colors[3] , zorder = 4)
		ax.scatter(x , c_008 , marker = marker , edgecolor = 'black' , s = size , facecolor = colors[0] , zorder = 4)
		ax.scatter(x , c_014 , marker = marker , edgecolor = 'black' , s = size , facecolor = colors[1] , zorder = 4)
		ax.scatter(x , c_018 , marker = marker , edgecolor = 'black' , s = size , facecolor = colors[2] , zorder = 4)
		ax.scatter(x , c_020 , marker = marker , edgecolor = 'black' , s = size , facecolor = colors[3] , zorder = 4)
		# ax.set_yticks(np.linspace(-140 , 100 , 5).astype(int))

		ax.label_outer()
		ax.set_xlabel('Normalized Polarization', fontsize = fontsize)
		ax.set_ylabel('1/C', fontsize = fontsize)
		ax.set_xlim([-1 , 1])
		ax.set_ylim([-1200, 1000])
		ax.tick_params(axis = 'both' , which = 'major' , labelsize = fontsize , top = False)
		yticks = ax.yaxis.get_major_ticks()
		yticks[-1].label1.set_visible(False)
		count += 1
#axes labels
# fig.text(0.05, 0.5, 'Energy (meV/f.u.)', va='center', rotation='vertical', fontsize = fontsize)

#axes
# plt.xticks(np.round(np.linspace(-1.5, 1.5, 11),2), fontsize = fontsize, rotation = 0)
# plt.yticks(np.linspace(-140, 100, 9).astype(int), fontsize = fontsize)
legend = plt.legend([ '0.08', '0.14','0.18', '0.20'], bbox_to_anchor=(0.85,2.3),ncols = 4,
                    title = 'Holes/f.u.',
                    fontsize =
fontsize)
plt.setp(legend.get_title(),fontsize=fontsize)

if save:
	plt.savefig(f"{fig_path}negative_capacitance.png", dpi = 300, bbox_inches='tight')
plt.show()
