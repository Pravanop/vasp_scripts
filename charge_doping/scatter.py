import matplotlib.pyplot as plt
import numpy as np

x = [0 , 0.05, 0.1 ,0.15, 0.2]
# x = [0,
# 0.03,
# 0.04,
# 0.06,
# 0.07,
# 0.09,
# 0.11,
# 0.12,
# 0.13,
# 0.14,
# 0.16,
# 0.17,
# 0.18,
# 0.19,
# ]
y_pbcm = [
132.25,
108.45,
98.5,
80,
65.25,
37.75,
5.5,
-13.25,
-29.25,
-46.5,
-78.5,
-101.75,
-121.25,
-137]
y_p42nmc = [
10,
-2.5,
-3.75,
-15.75,
-26.5,
-45.75,
-56.25,
-71.5,
-82.5,
-92.75,
-110.5,
-118.75,
-127.5,
-138.9
		]
zro = {
		
		'$Pca2_{1}$'   : [-10 , 3 , 27 , 46 , 107] ,
		'$Pbcm$'       : [122 , 102 , 68 , 5 , -31] ,
		'$P4_{2}/nmc$' : [0 , 0 , 0 , 0 , 0]
		
		}
y0 = np.array([39 , 51 , 76 , 111 , 167])
y1 = np.array([133 , 99 , 41 , 67 , 159])
y2 = [930 , 813 , 696]
y3 = [903 , 822 , 743]
y4 = [-1.76 ,
      -3.37 ,
      -4.92 ,
      -6.54 ,
      -7.55 , ]
y5 = [0.00 ,
      -1.06 ,
      -2.21 ,
      -3.29 ,
      -4.10]
y6 = [-1.00,	-1.14,	-0.70,	-1.09,	-1.70]
y7 = [0.00 ,
      0.04 ,
      0.07 ,
      0.10 ,
      0.13
      ]
y8 = [0.00 ,
      0.01 ,
      0.01 ,
      0.02 ,
      0.02
      ]
y9 = [
		0.00 ,
		0.01 ,
		0.01 ,
		0.01 ,
		0.01
		]
y10 = [0.00 ,
       0.03 ,
       0.07 ,
       0.11 ,
       0.15
       ]
y11 = [
		-7.25 ,
		-6.80 ,
		-6.62 ,
		-6.63 ,
		-5.03
		
		]
y12 = [
		-3.66 ,
		-4.42 ,
		-3.30 ,
		-3.15 ,
		-4.75
		]
y13 = [-2.35 ,
       -1.19 ,
       -0.30 ,
       0.05 ,
       0.59 ,
       
       ]
y14 = [
		-2.28 ,
		-1.15 ,
		0.20 ,
		0.95 ,
		1.33
		]
y15 = [
		49.82/4,	44.54/4,	32.52/4,	42.45/4,	91.31/4
		]
y16 = [
		44.06/4,	44.06/4,	49.26/4,	87.47/4,	128.48/4
		]
y17 = [53, 53, 54, 54, 54]
y18 = [67, 67, 65, 65, 64]
y19 = [3.91,
3.99,
4.07,
4.15,
4.25]
y20 = [-1.95,
-2.00,
-2.04,
-2.08,
-2.12]
y21 = [-1.95,
-2.00,
-2.04,
-2.08,
-2.12]
y22 = [3.65,
3.64,
3.63,
4.13,
4.21]
y23 = [-1.51,
-1.47,
-1.43,
-1.93,
-2.01]
y24 = [-2.14,
-2.18,
-2.19,
-2.20,
-2.20]
y25 = [3.89,
3.97,
4.07,
4.16,
4.25]
y26 = [-1.89,
-1.91,
-1.92,
-1.94,
-1.95]
y27 = [-1.99,
-2.07,
-2.15,
-2.22,
-2.30]
wf = zro['$Pca2_{1}$']
# for keys, value in zro.items():
# 	zro[keys] =  [value[i] - wf[i] for i in range(len(value))]
colors = ['#332288' , "#0077BB" , "#009988" , "#EE7733" , "#BBBBBB"]
# plt.axhline(y = 0, c = 'black', linestyle = '--')
# plt.plot(x , y_pbcm, c = '#CC6677' , marker = '^' , linestyle = '--' , ms = 8 , linewidth = 1 , alpha = 0.8)
# plt.plot(x , y_p42nmc , c = "#0077BB" , marker = 'o' , linestyle = '--' , ms = 8 , linewidth = 1 , alpha = 0.8)

# plt.plot(x , y27 , c = "#EE7733" , marker = 'd' , linestyle = '--' , ms = 5 , linewidth = 1 , alpha = 0.8)
# plt.plot(x, zro['$P4_{2}/nmc$'], c = "black" , marker = 'D' , linestyle = '--' , ms = 5 , linewidth = 1, alpha = 0.8)
plt.xticks(x , fontsize = 12)
plt.yticks(np.linspace(-2, 0, 9), fontsize = 12)
plt.plot(x, y6, c = 'black' , linewidth = 3 , alpha = 0.45 )
plt.scatter(x, y6, marker = 'o', edgecolor='black', s = 90, facecolor = 'black')
plt.xlabel('Holes/f.u.' , fontsize = 12)
plt.ylabel('1/C (Normalized)' , fontsize = 12)
# plt.legend(['Zr', '$O_{np}$', '$O_{p}$'] , fontsize = 12 , bbox_to_anchor = (0.75 , 1.15) , ncols = 3)
#
# plt.savefig('/Users/pravanomprakash/Library/CloudStorage/Box-Box/Charge Doping/Figures/zro_polarization.png' ,
            # dpi = 100)
plt.show()
