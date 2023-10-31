import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1.5 , 1.5 , 19)

p42nmc = {
		0    : [174 , 64 , 6 , -10 , 2 , 23 , 39 , 36 , 16 , 0 , 16 , 36 , 39 , 23 , 2 , -10 , 6 , 64 , 174] ,
		0.05 : [197 , 79 , 18 , 3 , 15 , 37 , 51 , 44 , 18 , 0 , 18 , 44 , 51 , 37 , 15 , 3 , 18 , 79 , 197] ,
		0.1  : [264 , 120 , 47 , 27 , 40 , 63 , 76 , 64 , 28 , 0 , 28 , 64 , 76 , 63 , 40 , 27 , 47 , 120 , 264] ,
		0.15 : [394 , 181 ,73 ,44 ,62 ,93 ,111 ,93 ,40 ,0 ,40 ,93 ,111 ,93 ,62 ,44 ,73 ,181 ,394] ,
		0.2  : [476 ,252 ,137 ,108 ,127 ,157 ,167 ,130 ,53 ,0 ,53 ,130 ,167 ,157 ,127 ,108 ,137 ,252 ,476]
		}

pbcm = {
		0    : [44 ,-61 ,-116 ,-133 ,-120 ,-90 ,-55 ,-25 ,-6 ,0 ,-6 ,-25 ,-55 ,-90 ,-120 ,-133 ,-116 ,-61 ,44],
		0.05 : [72 ,-28 ,-83 ,-99 ,-87 ,-58 ,-30 ,-10 ,-1 ,0 ,-1 ,-10 ,-30 ,-58 ,-87 ,-99 ,-83 ,-28 ,72] ,
		0.1  : [138 ,33 ,-25 ,-41 ,-28 ,-4 ,11 ,13 ,6 ,0 ,6 ,13 ,11 ,-4 ,-28 ,-41 ,-25 ,33 ,138] ,
		0.15 : [240 ,121 ,56 ,39 ,52 ,67 ,63 ,41 ,14 ,0 ,14 ,41 ,63 ,67 ,52 ,39 ,56 ,121 ,240] ,
		0.2  : [384 ,239 ,160 ,139 ,152 ,159 ,134 ,81 ,25 ,0 ,25 ,81 ,134 ,159 ,152 ,139 ,160 ,239 ,384]
		}

colors = ['#332288' , "#0077BB" , "#009988" , "#EE7733" , "#BBBBBB"]
colors.reverse()
barrier = []
phase = pbcm
i = 0
size = 50
marker = 'D'
linewidth = 4.5
alpha = 0.45

for key , value in phase.items() :
	# polar = value[-4]
	# value = [i - polar for i in value]
	plt.plot(x , value , linewidth = linewidth , alpha = alpha , c = colors[i] , zorder = 3)
	plt.scatter(x , value , marker = marker , edgecolor = 'black' , s = size , facecolor = colors[i])
	i += 1
# plt.legend(list(phase.keys()) , ncols = 3 , title = "Holes/f.u" , loc = "upper center")
plt.xlabel("Normalized Polarization")
plt.ylabel("Energy (meV/f.u)")
plt.ylim([-150 , 500])
# plt.savefig(
# 		'/Users/pravanomprakash/Library/CloudStorage/Box-Box/Charge Doping/Figures/switching_pathway_pbcm.png' ,
# 		dpi = 100 ,
# 		bbox_inches = 'tight'
# 		)
plt.show()
