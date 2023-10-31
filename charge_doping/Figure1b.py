import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

mpl.rc('font' , family = 'Helvetica')

fig_path = '/Users/pravanomprakash/Library/CloudStorage/Box-Box/Charge Doping/Figures/Figures_revised/'
save = True

def flipper(arr) :
	arr = arr.astype(int)
	temp = np.flip(arr[1 :])
	return np.concatenate((temp , arr))

pbcm_000 = np.array(
		[0 , -1 , -5 , -12 , -22 , -35 , -50 , -66 , -83 , -99 , -113 , -124 , -131 , -132 , -126 , -113 , -90 , -57 ,
		 -13 , 44]
		)
pbcm_000 = flipper(pbcm_000)
pbcm_003 = np.array(
		[0 , -1.25 , -3.5 , -8.25 , -15.5 , -25.5 , -37.75 , -51.75 , -67 , -82.25 , -96.5 , -107.5 , -114.25 , -115.5 ,
		 -110 , -96.25 , -74 , -41.75 , 0.5 , 53.25]
		)
pbcm_003 = flipper(pbcm_003)
pbcm_004 = np.array(
		[0 , -1 , -3 , -6.5 , -12.75 , -21.25 , -32.5 , -45.5 , -60 , -74.75 , -88.75 , -100 , -106.5 , -107.75 ,
		 -101.75 , -87.75 , -64.5 , -31.75 , 11.25 , 65]
		)
pbcm_004 = flipper(pbcm_004)
pbcm_006 = np.array(
		[0 , 0 , -1 , -2 , -5 , -11 , -19 , -29 , -42 , -56 , -69 , -80 , -87 , -88 , -82 , -68 , -44 , -11 , 33 , 87]
		)
pbcm_006 = flipper(pbcm_006)
pbcm_007 = np.array(
		[0 , 0 , 0 , 0 , -1 , -5 , -11 , -20 , -32 , -45 , -57 , -68 , -76 , -77 , -71 , -56 , -32 , 3 , 47 , 102]
		)
pbcm_007 = flipper(pbcm_007)
pbcm_008 = np.array(
		[0 , 0 , 2 , 3 , 3 , 1 , -4 , -11 , -21 , -33 , -45 , -55 , -63 , -64 , -58 , -44 , -20 , 15 , 60 , 116]
		)
pbcm_008 = flipper(pbcm_008)
pbcm_012 = np.array([0 , 2 , 8 , 16 , 24 , 30 , 35 , 36 , 32 , 25 , 15 , 4 , -3 , -5 , 2 , 19 , 47 , 86 , 137 , 201])
pbcm_012 = flipper(pbcm_012)
pbcm_014 = np.array([0 , 1 , 6 , 16 , 26 , 35 , 42 , 46 , 46 , 40 , 31 , 20 , 13 , 12 , 20 , 38 , 67 , 110 , 165 , 233])
pbcm_014 = flipper(pbcm_014)
pbcm_016 = np.array(
		[0 , 4 , 17 , 33 , 51 , 68 , 82 , 93 , 97 , 96 , 88 , 79 , 72 , 71 , 78 , 97 , 128 , 171 , 229 , 299]
		)
pbcm_016 = flipper(pbcm_016)
pbcm_018 = np.array(
		[0 , 6 , 22 , 44 , 68 , 91 , 112 , 127 , 135 , 136 , 130 , 122 , 114 , 113 , 121 , 141 , 173 , 220 , 280 , 356]
		)
pbcm_018 = flipper(pbcm_018)
pbcm_020 = np.array(
		[0 , 8 , 28 , 55 , 84 , 114 , 141 , 161 , 173 , 178 , 176 , 167 , 160 , 159 , 167 , 187 , 221 , 268 , 331 , 410]
		)
pbcm_020 = flipper(pbcm_020)
p42nmc_000 = np.array(
		[0, 4, 14, 25, 34, 39, 39, 35, 28, 18, 7, -3, -9, -10, -4, 10, 33, 68, 115, 174]
		)
p42nmc_000 = flipper(p42nmc_000)
p42nmc_003 = np.array([0 , 4 , 15 , 27 , 38 , 44 , 45 , 42 , 34 , 24 , 13 , 4 , -3 , -4 , 2 , 16 , 40 , 76 , 125 , 187])
p42nmc_003 = flipper(p42nmc_003)
p42nmc_004 = np.array([0 , 5 , 19 , 34 , 46 , 53 , 54 , 50 , 42 , 31 , 19 , 8 , 1 , -1 , 6 , 23 , 51 , 93 , 149 , 222])
p42nmc_004 = flipper(p42nmc_004)
p42nmc_007 = np.array(
		[0, 8, 27, 49, 66, 76, 79, 75, 66, 53, 39, 26, 17, 15, 23, 44, 79, 131, 201, 292]
		)
p42nmc_007 = flipper(p42nmc_007)
p42nmc_012 = np.array([0, 13, 41, 74, 104, 124, 133, 131, 122, 108, 91, 75, 64, 61, 70, 94, 137, 200, 287, 399])
p42nmc_012 = flipper(p42nmc_012)

p42nmc_014 = np.array(
		[0 , 13 , 41 , 74 , 104 , 124 , 133 , 131 , 122 , 108 , 91 , 75 , 64 , 61 , 70 , 94 , 137 , 200 , 287 , 399]
		)
p42nmc_014 = flipper(p42nmc_014)

p42nmc_016 = np.array([0, 14, 45, 83, 118, 144, 158, 160, 152, 139, 123, 108, 98, 96, 105, 130, 174, 240, 330, 446])
p42nmc_016 = flipper(p42nmc_016)

p42nmc_018 = np.array(
		[0 , 14 , 46 , 85 , 122 , 150 , 167 , 170 , 164 , 152 , 138 , 124 , 114 , 112 , 120 , 144 , 186 , 250 , 337 ,
		 451]
		)
p42nmc_018 = flipper(p42nmc_018)
p42nmc_020 = np.array(
		[0 , 14 , 48 , 88 , 127 , 158 , 177 , 181 , 177 , 166 , 153 , 139 , 129 , 127 , 135 , 158 , 199 , 262 , 348 , 461]
		)
p42nmc_020 = flipper(p42nmc_020)
x = np.linspace(-1.5 , 1.5 , 39)
fontsize = 26
colors = ['#332288' , "#0077BB" , "#009988" , "#CC3311" , "#EE7733" , "#BBBBBB"]
colors.reverse()
linewidth = 4.5
alpha = 0.45

fig , axs = plt.subplots(2 , 1 , sharex = True , sharey = True , figsize = (3.39 * 5 , 3.39 * 5))
plt.rcParams["font.family"] = "sans"
plt.subplots_adjust(hspace = 0)
size = 50
marker = 'D'
count = 0
for ax in axs :
	if count == 0 :
		ax.plot(x , pbcm_000 , linewidth = linewidth , alpha = alpha , c = colors[0] , zorder = 3)
		ax.plot(x , pbcm_004 , linewidth = linewidth , alpha = alpha , c = colors[1] , zorder = 3)
		ax.plot(x , pbcm_007 , linewidth = linewidth , alpha = alpha , c = colors[2] , zorder = 3)
		ax.plot(x , pbcm_012 , linewidth = linewidth , alpha = alpha , c = colors[3] , zorder = 3)
		ax.plot(x , pbcm_016 , linewidth = linewidth , alpha = alpha , c = colors[4] , zorder = 3)
		ax.plot(x , pbcm_020 , linewidth = linewidth , alpha = alpha , c = colors[5] , zorder = 3)
		ax.scatter(x , pbcm_000 , marker = marker , edgecolor = 'black' , s = size , facecolor = colors[0] , zorder = 4)
		ax.scatter(x , pbcm_004 , marker = marker , edgecolor = 'black' , s = size , facecolor = colors[1] , zorder = 4)
		ax.scatter(x , pbcm_007 , marker = marker , edgecolor = 'black' , s = size , facecolor = colors[2] , zorder = 4)
		ax.scatter(x , pbcm_012 , marker = marker , edgecolor = 'black' , s = size , facecolor = colors[3] , zorder = 4)
		ax.scatter(x , pbcm_016 , marker = marker , edgecolor = 'black' , s = size , facecolor = colors[4] , zorder = 4)
		ax.scatter(x , pbcm_020 , marker = marker , edgecolor = 'black' , s = size , facecolor = colors[5] , zorder = 4)
		
		ax.axhline(y = 0 , c = 'black' , linestyle = '-' , linewidth = 1 , alpha = 0.8 , zorder = 1)
		ax.axvline(x = 0 , c = 'black' , linestyle = '-' , linewidth = 1 , alpha = 0.8 , zorder = 1)
		
		ax.text(x = 0.505 , y = 0.15 , s = '$Pbcm$' , fontsize = fontsize , transform = ax.transAxes)
		ax.text(x = 0.25 , y = 0.85 , s = 'Shift Across' , fontsize = fontsize , transform = ax.transAxes , )
		ax.label_outer()
		ax.tick_params(axis = 'both' , which = 'major' , labelsize = fontsize , top = False)
		yticks = ax.yaxis.get_major_ticks()
		yticks[-1].label1.set_visible(False)
		count += 1
	else :
		ax.plot(x , p42nmc_000 , linewidth = linewidth , alpha = alpha , c = colors[0] , zorder = 3)
		ax.plot(x , p42nmc_004 , linewidth = linewidth , alpha = alpha , c = colors[1] , zorder = 3)
		ax.plot(x , p42nmc_007 , linewidth = linewidth , alpha = alpha , c = colors[2] , zorder = 3)
		ax.plot(x , p42nmc_012 , linewidth = linewidth , alpha = alpha , c = colors[3] , zorder = 3)
		ax.plot(x , p42nmc_016 , linewidth = linewidth , alpha = alpha , c = colors[4] , zorder = 3)
		ax.plot(x , p42nmc_020 , linewidth = linewidth , alpha = alpha , c = colors[5] , zorder = 3)
		ax.scatter(
				x , p42nmc_000 , marker = marker , edgecolor = 'black' , s = size , facecolor = colors[0] , zorder = 4
				)
		ax.scatter(
				x , p42nmc_004 , marker = marker , edgecolor = 'black' , s = size , facecolor = colors[1] ,
				zorder = 4
				)
		ax.scatter(
				x , p42nmc_007 , marker = marker , edgecolor = 'black' , s = size , facecolor = colors[2] , zorder = 4
				)
		ax.scatter(
				x , p42nmc_012 , marker = marker , edgecolor = 'black' , s = size , facecolor = colors[3] , zorder = 4
				)
		ax.scatter(
				x , p42nmc_016 , marker = marker , edgecolor = 'black' , s = size , facecolor = colors[4] ,
				zorder = 4
				)
		ax.scatter(
				x , p42nmc_020 , marker = marker , edgecolor = 'black' , s = size , facecolor = colors[5] ,
				zorder = 4
				)
		
		ax.axhline(y = 0 , c = 'black' , linestyle = '-' , linewidth = 1 , alpha = 0.8 , zorder = 1)
		ax.axvline(x = 0 , c = 'black' , linestyle = '-' , linewidth = 1 , alpha = 0.8 , zorder = 2)
		
		ax.set_xlabel('Polarization (Normalized)' , fontsize = fontsize)
		ax.text(x = 0.505 , y = 0.15 , s = '$P$4$_{2}/nmc$' , fontsize = fontsize , transform = ax.transAxes)
		ax.text(x = 0.16 , y = 0.15 , s = '$Pca2_{1}$' , fontsize = fontsize , transform = ax.transAxes)
		ax.text(x = 0.77 , y = 0.15 , s = '$Pca2_{1}$' , fontsize = fontsize , transform = ax.transAxes)
		ax.label_outer()
		ax.tick_params(axis = 'both' , which = 'major' , labelsize = fontsize , top = True)
		ax.text(
				x = 0.25 , y = 0.85 , s = 'Shift Inside' , fontsize = fontsize , transform = ax.transAxes
				)
		count += 1
# axes labels
legend = plt.legend(
		['0' , '0.04' , '0.07' , '0.12' , '0.16' , '0.2'] , bbox_to_anchor = (1.05 , 2.25) , ncols = 6 ,
		title = 'Holes/f.u.' , labelspacing = 0.0, borderpad = 0.8,
		fontsize = fontsize
		)
plt.setp(legend.get_title() , fontsize = fontsize)
fig.text(0.04 , 0.5 , 'Energy (meV/f.u.)' , va = 'center' , rotation = 'vertical' , fontsize = fontsize)

# axes
# plt.xticks(np.round(np.linspace(-1.5, 1.5, 11),2), fontsize = fontsize, rotation = 0)
# plt.yticks(np.linspace(-140, 100, 9).astype(int), fontsize = fontsize)

if save :
	plt.savefig(f"{fig_path}switching_pathways.png")
plt.show()
