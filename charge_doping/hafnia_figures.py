import matplotlib.pyplot as plt
import numpy as np
from pymatgen.io.vasp.outputs import Vasprun
from scipy.ndimage import gaussian_filter1d as gf

plt.rcParams['text.usetex'] = True
params = {'mathtext.default' : 'regular'}

zr_data = {
		'm':[-91.24,
48.56,
-29.48,
-203.90,
-421.39],
'oIII': [-52.32,
35.94,
114.17,
-203.77,
-421.39],
'o-ref':[80.05,
75.56,
-29.43,
-203.77,
-421.39
		],
'c':[0, 0, 0, 0, 0
		],
't':[
-42.27,
9.22,
0.46,
0.10,
0.00
		]
		}
#
hf_data = {
		'm':[-171.88,
-45.19,
79.12,
-185.27,
-385.58],
'oIII': [-118.97,
-32.58,
42.09,
104.98,
163.80],
'o-ref':[50.59,
59.14,
-29.33,
-185.48,
-385.63
		],
'c':[0, 0, 0, 0, 0
		],
't':[
-56.40,
6.69,
0.33,
0.70,
0.11
		]
		}
#
# hfzro_data = {
# 		'm':[-132.43,
# 1.07,
# 127.53,
# -195.65,
# -403.94],
# 'oIII': [-87.44,
# -0.60,
# 75.69,
# 142.00,
# -403.94],
# 'o-ref':[80.05,
# 75.56,
# -29.43,
# -203.77,
# -421.39
# 		],
# 'c':[0, 0, 0, 0, 0
# 		],
# 't':[
# -49.13,
# 8.23,
# 0.63,
# 0.02,
# -2.45
# 		]
# 		}
#
# space_group_zro = {
# 		't': r"$\emph{t}-ZrO_{2} \emph{[P4\textsubscript{2}/nmc]}$",
# 		'm': r"$\emph{m}-ZrO_{2} \emph{[P2\textsubscript{1}/c]}$",
# 		'c': r"$\emph{c}-ZrO_{2} \emph{[Fm\bar{3}m]}$",
# 		'o-ref': r"$\emph{o-ref}-ZrO_{2} \emph{[Pbcm]}$",
# 		'oIII': r"$\emph{o-III}-ZrO_{2} \emph{[Pca2\textsubscript{1}]}$"
# 		}
#
# space_group_hfo = {
# 		't': r"$\emph{t}-HfO_{2} \emph{[P4\textsubscript{2}/nmc]}$",
# 		'm': r"$\emph{m}-HfO_{2} \emph{[P2\textsubscript{1}/c]}$",
# 		'c': r"$\emph{c}-HfO_{2} \emph{[Fm\bar{3}m]}$",
# 		'o-ref': r"$\emph{o-ref}-HfO_{2} \emph{[Pbcm]}$",
# 		'oIII': r"$\emph{o-III}-HfO_{2} \emph{[Pca2\textsubscript{1}]}$"
# 		}
#
# space_group_hfzro = {
# 		't': r"$\emph{t}-Hf_{0.5}Zr_{0.5}O_{2} \emph{[P4\textsubscript{2}/nmc]}$",
# 		'm': r"$\emph{m}-Hf_{0.5}Zr_{0.5}O_{2}} \emph{[P2\textsubscript{1}/c]}$",
# 		'c': r"$\emph{c}-Hf_{0.5}Zr_{0.5}O_{2} \emph{[Fm\bar{3}m]}$",
# 		'o-ref': r"$\emph{o-ref}-Hf_{0.5}Zr_{0.5}O_{2} \emph{[Pbcm]}$",
# 		'oIII': r"$\emph{o-III}-Hf_{0.5}Zr_{0.5}O_{2} \emph{[Pca2\textsubscript{1}]}$"
# 		}
#
# holes = [0, 0.1, 0.2, 0.3, 0.4]
# fig, axs = plt.subplots(3, 1, sharex = True, sharey = True)
# fig.subplots_adjust(hspace=0, wspace = 0)
#
# fontsize = 9
# # fig.suptitle(r'Phase stabilities in $HfO\textsubscript{2}$, '
# #              r'$Hf\textsubscript{0.5}Zr\textsubscript{0.5}O\textsubscript{2}$ and '
# #              r'$ZrO\textsubscript{2}$ with hole doping', fontsize = 10)
# axs[2].tick_params(axis='both', which='major', labelsize=fontsize)
# axs[2].plot(holes, zr_data['oIII'], c = '#0077BB', linestyle = '--', marker = 's')
# axs[2].plot(holes, zr_data['m'], c = '#44AA99', linestyle = '-.', marker = 'D')
# axs[2].plot(holes, zr_data['o-ref'], c = '#EE7733', linestyle = '-', marker = 'v')
# axs[2].plot(holes, zr_data['c'], c = '#33bbee', linestyle = ':',marker = '*')
# axs[2].plot(holes, zr_data['t'], c = '#CC6677', marker = 'o')
# axs[2].set_yticks(np.arange(-450, 100, 150))
# axs[2].set_xticks(np.arange(0, 0.45, 0.1))
# axs[2].set_title(r'$ZrO\textsubscript{2}$', y = 0.0, fontsize = fontsize)
# axs[2].set_xlabel('Holes/f.u.', fontsize = fontsize)
#
# axs[0].plot(holes, hf_data['oIII'], c = '#0077BB', linestyle = '--', marker = 's')
# axs[0].plot(holes, hf_data['m'], c = '#44AA99', linestyle = '-.', marker = 'D')
# axs[0].plot(holes, hf_data['o-ref'], c = '#EE7733', linestyle = '-', marker = 'v')
# axs[0].plot(holes, hf_data['c'], c = '#33bbee', linestyle = ':',marker = '*')
# axs[0].plot(holes, hf_data['t'], c = '#CC6677', marker = 'o')
# axs[0].set_title(r'$HfO\textsubscript{2}$', y = 0.0, fontsize = fontsize)
#
#
# axs[1].plot(holes, hfzro_data['oIII'], c = '#0077BB', linestyle = '--', marker = 's')
# axs[1].plot(holes, hfzro_data['m'], c = '#44AA99', linestyle = '-.', marker = 'D')
# axs[1].plot(holes, hfzro_data['o-ref'], c = '#EE7733', linestyle = '-', marker = 'v')
# axs[1].plot(holes, hfzro_data['c'], c = '#33bbee', linestyle = ':',marker = '*')
# axs[1].plot(holes, hfzro_data['t'], c = '#CC6677', marker = 'o')
# axs[1].set_title(r'$Hf\textsubscript{0.5}Zr\textsubscript{0.5}O\textsubscript{2}$', y = 0.0, fontsize = fontsize)
# axs[1].set_ylabel(r'$\delta$ E (meV/f.u)', fontsize=fontsize)
#
# fig.legend([r'$\emph{o-III}$  $\emph{[Pca2\textsubscript{1}]}$',
#             r"$\emph{m}$  $\emph{[P2\textsubscript{1}/c]}$",
#             r"$\emph{o-ref}$  $\emph{[Pbcm]}$",
# 			r"$\emph{c}$  $\emph{[Fm3m]}$",
# 			r"$\emph{t}$  $\emph{[P4\textsubscript{2}/nmc]}$"
#             ],
#            loc = 'upper center',
#            fontsize = fontsize,
#            ncol = 3)

#

# plt.savefig("fig1a.png", bbox_inches = 'tight', pad_inches = 0.01, dpi=150)
# plt.show()

pbcm = {
		0.0: [
0,
6,
21,
42,
66,
88,
108,
122,
130,
132,
130,
122,
108,
88,
66,
42,
21,
6,
0,
				]
	,0.05 : [
0,
6,
21,
41,
61,
77,
89,
96,
98,
99,
98,
96,
89,
77,
61,
41,
21,
6,
0,
			],
		0.1:[
0,
7,
21,
37,
49,
54,
53,
48,
43,
40,
43,
48,
53,
54,
49,
37,
21,
7,
0,
				]
		}

p42nmc = {
		0.0:[
0,
6,
19,
34,
45,
50,
46,
33,
18,
10,
18,
33,
46,
50,
45,
34,
19,
6,
0]	,
		0.05:[
0,
6,
19,
34,
46,
49,
42,
26,
7,
-2,
7,
26,
42,
49,
46,
34,
19,
6,
0,
				],
		0.1:[
0,
7,
21,
37,
47,
48,
36,
14,
-12,
-27,
-12,
14,
36,
48,
47,
37,
21,
7,
0
				]
		}

image = [-1,
-0.88,
-0.77,
-0.66,
-0.55,
-0.44,
-0.33,
-0.22,
-0.11,
0,
0.11,
0.22,
0.33,
0.44,
0.55,
0.66,
0.77,
0.88,
1,]
fontsize = 10
fig, ax = plt.subplots(2,1, sharex = True, sharey = True, figsize = (4, 6))

fig.subplots_adjust(hspace=0, wspace = 0)
ax[0].set_title(r'$\emph{o-ref-ZrO\textsubscript{2}}$', y = 0.0, fontsize = fontsize)

# ax[0].axvline(0, linestyle = ":", c = "black", linewidth = 0.8)


ax[0].plot(image, pbcm[0.0], marker = '.', linestyle = "--", color = '#EE7733')
ax[0].plot(image, pbcm[0.05], marker = '.', linestyle = "--", color = '#44AA99')
ax[0].plot(image, pbcm[0.1], marker = '.',  linestyle = "--", color = '#0077BB')
ax[0].spines["bottom"].set_visible(False)
ax[1].set_title(r'$\emph{t-ZrO\textsubscript{2}}$', y = .6, fontsize = fontsize)

# ax[1].axvline(0, linestyle = ":", c = "black", linewidth = 0.8)
ax[1].plot(image, p42nmc[0.0], marker = '.', linestyle = "--", color = '#EE7733')
ax[1].plot(image, p42nmc[0.05], marker = '.', linestyle = "--", color = '#44AA99')
ax[1].plot(image, p42nmc[0.1], marker = '.', linestyle = "--", color = '#0077BB')
ax[1].set_xlabel('Normalized Distortion', fontsize = fontsize)
ax[1].spines["top"].set_visible(False)
ax[0].axhline(0, linestyle = ":", c = "black", linewidth = 0.8)
ax[1].axhline(0, linestyle = ":", c = "black", linewidth = 0.8)
fig.legend(['0.1', '0.05', '0.0'], loc = "upper center", ncols = 3, fontsize = fontsize, title = "Holes/f.u.")
fig.text(0.02, 0.5, r'$\Delta$ E (meV/f.u)',fontsize=fontsize, ha="center", va="center", rotation=90)
plt.savefig("fig4.png", bbox_inches = 'tight', pad_inches = 0.01, dpi=150)
plt.show()

# path = f"/Users/pravanomprakash/Downloads/structures/vasprun/"
#
# def analyse(file_path) :
# 	dosrun = Vasprun(filename = file_path , parse_dos = True)
# 	Cdos = dosrun.complete_dos
# 	dos_by_site = []
# 	for site in Cdos.structure.sites :
# 		dos_by_site.append(Cdos.get_site_dos(site , ))
#
# 	return dos_by_site , Cdos
#
# O1_list , O2_list , Zr_list = [] , [] , []
# energies = []
# for i in [0 , 1] :
#
# 	file_path = path + f"pbcm_{i}.xml"
# 	by_site , Cdos = analyse(file_path)
# 	energies.append(by_site[0].energies - Cdos.efermi)
# 	O1_list.append(
# 		gf(by_site[4].get_densities() + by_site[5].get_densities() + by_site[6].get_densities() + by_site[
# 			7].get_densities() / 4, sigma = 0.5)
# 		)
# 	O2_list.append(
# 		gf(by_site[8].get_densities() + by_site[9].get_densities() + by_site[10].get_densities() + by_site[
# 			11].get_densities() / 4, sigma = 0.5)
# 		)
# 	Zr_list.append(
# 		gf(by_site[0].get_densities() + by_site[1].get_densities() + by_site[2].get_densities() + by_site[
# 			3].get_densities() / 4, sigma = 0.5)
# 		)
#
# O1_list_pca , O2_list_pca , Zr_list_pca = [] , [] , []
# energies_pca = []
# for i in [0 , 1] :
#
# 	file_path = path + f"pca21_{i}.xml"
# 	by_site , Cdos = analyse(file_path)
# 	energies_pca.append(by_site[0].energies - Cdos.efermi)
# 	O1_list_pca.append(
# 			gf(
# 				by_site[4].get_densities() + by_site[5].get_densities() + by_site[6].get_densities() + by_site[
# 					7].get_densities() / 4 , sigma = 0.9
# 				)
# 			)
# 	O2_list_pca.append(
# 			gf(
# 				by_site[8].get_densities() + by_site[9].get_densities() + by_site[10].get_densities() + by_site[
# 					11].get_densities() / 4 , sigma = 0.9
# 				)
# 			)
# 	Zr_list_pca.append(
# 			gf(
# 				by_site[0].get_densities() + by_site[1].get_densities() + by_site[2].get_densities() + by_site[
# 					3].get_densities() / 4 , sigma = 0.9
# 				)
# 			)
#
# fig , ax = plt.subplots(2, 2 , sharex = 'col' , sharey = 'row' , figsize = (6.750 , 3.375))
# fontsize = 10
#
# ax[0][0].tick_params(axis='both', which='major', labelsize=fontsize)
# ax[0][0].plot(energies[0] , O1_list[0] , c = '#0077BB' , alpha = 1 , linewidth = 0.9)
# ax[0][0].plot(energies[0] , O2_list[0] , c = '#CC6677' , alpha = 1 , linewidth = 0.9)
# ax[0][0].plot(energies[0] , Zr_list[0] , c = '#33bbee' , alpha = 1 , linewidth = 0.9)
# ax[0][0].axvline(x = 0 , color = 'black' , linestyle = '-.' , alpha = 0.8 , linewidth = 0.8)
# ax[0][0].fill_between(energies[0], O2_list[0], where = energies[0] > 0.0, color = '#CC6677', alpha = 0.7)
# ax[0][0].set_xlim(-2 , 1)
# ax[0][0].set_ylim(0 , 4)
# ax[1][0].set_yticks(np.arange(0, 4, 2))
# ax[0][0].grid(alpha = 0.4)
# ax[0][0].label_outer()
#
# ax[1][0].tick_params(axis='both', which='major', labelsize=fontsize)
# ax[1][0].plot(energies[1] , O1_list[1] , c = '#0077BB' , alpha = 1 , linewidth = 0.9)
# ax[1][0].plot(energies[1] , O2_list[1] , c = '#CC6677' , alpha = 1 , linewidth = 0.9)
# ax[1][0].plot(energies[1] , Zr_list[1] , c = '#33bbee' , alpha = 1 , linewidth = 0.9)
# ax[1][0].axvline(x = 0 , color = 'black' , linestyle = '-.' , alpha = 0.8 , linewidth = 0.8)
# ax[1][0].fill_between(energies[1], O2_list[1], where = energies[1] > 0.0, color = '#CC6677', alpha = 0.7)
# ax[1][0].set_xlim(-2 , 1)
# ax[1][0].set_ylim(0 , 4)
# ax[1][0].set_yticks(np.arange(0, 4, 2))
# ax[1][0].grid(alpha = 0.4)
# ax[1][0].label_outer()
#
# ax[0][1].tick_params(axis='both', which='major', labelsize=fontsize)
# ax[0][1].plot(energies_pca[0] , O1_list_pca[0] , c = '#0077BB' , alpha = 1 , linewidth = 0.9)
# ax[0][1].plot(energies_pca[0] , O2_list_pca[0] , c = '#CC6677' , alpha = 1 , linewidth = 0.9)
# ax[0][1].plot(energies_pca[0] , Zr_list_pca[0] , c = '#33bbee' , alpha = 1 , linewidth = 0.9)
# ax[0][1].axvline(x = 0 , color = 'black' , linestyle = '-.' , alpha = 0.8 , linewidth = 0.8)
# ax[0][1].fill_between(energies_pca[0], O1_list_pca[0], where = energies_pca[0] > 0.0, color = '#0077BB', alpha = 0.7)
# ax[0][1].set_xlim(-2 , 1)
# ax[0][1].set_ylim(0 , 4)
# ax[0][1].set_yticks(np.arange(0, 4, 2))
# ax[0][1].grid(alpha = 0.4)
# ax[0][1].label_outer()
#
# ax[1][1].tick_params(axis='both', which='major', labelsize=fontsize)
# ax[1][1].plot(energies_pca[1] , O1_list_pca[1] , c = '#0077BB' , alpha = 1 , linewidth = 0.9)
# ax[1][1].plot(energies_pca[1] , O2_list_pca[1] , c = '#CC6677' , alpha = 1 , linewidth = 0.9)
# ax[1][1].plot(energies_pca[1] , Zr_list_pca[1] , c = '#33bbee' , alpha = 1 , linewidth = 0.9)
# ax[1][1].fill_between(energies_pca[1], O1_list_pca[1], where = energies_pca[1] > 0.0, color = '#0077BB', alpha = 0.7)
# ax[1][1].axvline(x = 0 , color = 'black' , linestyle = '-.' , alpha = 0.8 , linewidth = 0.8)
# ax[1][1].set_xlim(-2 , 1)
# ax[1][1].set_ylim(0 , 4)
# ax[1][1].set_yticks(np.arange(0, 4, 2))
# ax[1][1].grid(alpha = 0.4)
# ax[1][1].label_outer()
#
#
# fig.supxlabel("Energy - $E_f$ (eV)", fontsize = fontsize)
# fig.supylabel("DOS", fontsize = fontsize)
# fig.legend(["$O3$" , "$O4$" , "Zr"] , loc = "upper center", ncols = 3 , fontsize = fontsize)
#
# plt.subplots_adjust(hspace = 0)
# plt.savefig("fig3a.png", bbox_inches = 'tight', pad_inches = 0.01, dpi=300)
# plt.show()

# fig, ax = plt.subplots(1, 2, figsize = (6.750 , 3.375), sharex = True, sharey = True)
# fig.subplots_adjust(hspace = 0)
#
# pca21_data = {'O3': (0, 0.021, 0.038), 'O4': (0, 0, 0)}
# pbcm_data = {'O3':(0.0, 0.00001, 0.0073), 'O4':(0, 0.0184, 0.069)}

# fontsize = 10
# holes = [0, 0.05, 0.1]
# ax[1].plot(holes, pca21_data['O3'], c = '#0077BB', linestyle = "--", marker = 's')
# ax[1].plot(holes, pca21_data['O4'], c = '#CC6677', linestyle = "--", marker = 's')
# ax[1].set_title(r'$\emph{oIII}-ZrO_{2}$', y = 5, fontsize = fontsize)
# ax[1].set_yticks(np.arange(0, 0.1, 0.03))
# ax[1].set_xticks(np.arange(0.0, 0.11, 0.05))
# ax[1].tick_params(axis='both', which='major', labelsize=fontsize)
# ax[0].plot(holes, pbcm_data['O3'], c = '#0077BB', linestyle = "--", marker = 's')
# ax[0].plot(holes, pbcm_data['O4'], c = '#CC6677', linestyle = "--", marker = 's')
# ax[0].set_title(r'$\emph{o-ref}-ZrO_{2}$', y = 5, fontsize = fontsize)
# ax[0].tick_params(axis='both', which='major', labelsize=fontsize)
#
#
# fig.supxlabel('Holes/f.u.', fontsize = fontsize)
# fig.supylabel('Valence band integrated DOS',fontsize=fontsize)
# # fig.legend(['O3', 'O4'], fontsize = fontsize, loc = "right")
# plt.savefig("fig3b.png")
# plt.show()

# do = [0.68762 ,
#       0.68364 ,
#       0.66848 ,
#       0.66575 ,
#       0.66095 ,
#       0.61176]
#
# dt = [0.55497 ,
#       0.55294 ,
#       0.56412 ,
#       0.56392 ,
#       0.56604 ,
#       0.60795]
#
# fontsize = 10
# holes = [0 , 0.05 , 0.1 , 0.15 , 0.2, 0.3]
# plt.plot(holes , do , c = '#BB5566' , linestyle = "--" , marker = 's')
# plt.plot(holes , dt , c = '#DDAA33' , linestyle = "--" , marker = 'o')
# plt.yticks(np.arange(0.5 , 0.7 , 0.03))
# plt.xticks(np.arange(0.0 , 0.35 , 0.05))
# plt.tick_params(axis = 'both' , which = 'major' , labelsize = fontsize)
# plt.xlabel("Holes/f.u.", fontsize = fontsize)
# plt.ylabel("Polar displacement ($\AA$)", fontsize = fontsize)
# plt.legend(["$d_o$", "$d_t$"])
# plt.show()

fig, (ax, ax2) = plt.subplots(2, 1, figsize = (6.750 , 3.375), sharex = True)
fontsize = 10
holes = [0 , 0.05 , 0.1 , 0.15]
gm5 = [0.657,	0.661,	0.676,	0.678]
gm1 = [0.253,	0.246,	0.248,	0.249]
m3 = [0.539,	0.549,	0.569,	0.579]
m1 = [0.621,	0.619,	0.631,	0.631]
gm1p = [0.438,	0.435,	0.409,	0.403]
g2 = [1.906,	1.903,	1.866,	1.863]
#
ax.plot(holes, gm5,  c = '#BB5566' , linestyle = "--" , marker = 's')
ax.plot(holes, m1,  c = '#DDAA33' , linestyle = "--" , marker = 's')
ax.plot(holes, m3,  c = '#44AA99' , linestyle = "--" , marker = 's')
ax2.plot(holes, gm1,  c = '#0077BB' , linestyle = "--" , marker = 's')
# ax.plot(holes, g2,  c = '#0077BB' , linestyle = "--" , marker = 's')
# ax2.plot(holes, gm1p,  c = '#44AA99' , linestyle = "--" , marker = 's')

ax.set_ylim(0.5, 0.7)
ax2.set_ylim(0.1, 0.3)
ax2.set_xlabel("holes/f.u.", fontsize = 14)
fig.supylabel("Displacement ($\AA$)", fontsize = 14)
ax.spines['bottom'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax.xaxis.tick_top()
ax.tick_params(labeltop=False)  # don't put tick labels at the top
ax2.xaxis.tick_bottom()
ax.tick_params(axis='both', which='major', labelsize=14)
ax2.tick_params(axis='both', which='major', labelsize=14)


fig.legend(["$\Gamma_5^-$", "$M_1$", "$M_3$", "$\Gamma_1^+$"], ncols = 4, loc = "upper center", fontsize = 14)
# fig.legend(["$\Gamma_2^-$", "$\Gamma_1^+$"])
d = .005  # how big to make the diagonal lines in axes coordinates
# arguments to pass to plot, just so we don't keep repeating them
kwargs = dict(transform=ax.transAxes, color='k', clip_on=False)
ax.plot((-d, +d), (-d, +d), **kwargs)        # top-left diagonal
ax.plot((1 - d, 1 + d), (-d, +d), **kwargs)  # top-right diagonal

kwargs.update(transform=ax2.transAxes)  # switch to the bottom axes
ax2.plot((-d, +d), (1 - d, 1 + d), **kwargs)  # bottom-left diagonal
ax2.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)
plt.show()
