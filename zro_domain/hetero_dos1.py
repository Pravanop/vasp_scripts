from pymatgen.electronic_structure.core import OrbitalType
from pymatgen.electronic_structure.core import Spin
from pymatgen.electronic_structure.plotter import BSDOSPlotter , BSPlotter , DosPlotter
from pymatgen.io.vasp.outputs import BSVasprun , Vasprun
import matplotlib.pyplot as plt
import numpy as np

path = f"/Users/pravanomprakash/Documents/vasprun.xml"

def analyse(file_path) :
	dosrun = Vasprun(filename = file_path , parse_dos = True)
	Cdos = dosrun.complete_dos
	dos_by_site = []
	for site in Cdos.structure.sites :
		dos_by_site.append(Cdos.get_site_dos(site , ))
	
	return dos_by_site , Cdos

file_path = path
by_site , Cdos = analyse(file_path)

n = 27

o_polar = {
		1  : (81 , 79) ,
		2  : (82 , 84) ,
		3  : (77 , 75) ,
		4  : (66 , 70) ,
		5  : (72 , 68) ,
		6  : (43 , 49) ,
		7  : (51 , 45) ,
		8  : (48 , 42) ,
		9  : (39 , 38) ,
		10 : (36 , 31) ,
		11 : (28 , 33) ,
		12 : (35 , 30) ,
		13 : (54 , 58) ,
		14 : (60 , 56) ,
		15 : (62 , 64)
		}

o_non_polar = {
		1  : (78 , 80) ,
		2  : (85 , 83) ,
		3  : (74 , 76) ,
		4  : (73 , 69) ,
		5  : (67 , 71) ,
		6  : (53 , 47) ,
		7  : (44 , 50) ,
		8  : (52 , 46) ,
		9  : (40 , 41) ,
		10 : (37 , 32) ,
		11 : (29 , 34) ,
		12 : (61 , 57) ,
		13 : (55 , 59) ,
		14 : (65 , 63) ,
		15 : (78 , 80)
		}

zr = {
		1  : (27 , 26) ,
		2  : (25 , 24) ,
		3  : (22 , 23) ,
		4  : (20 , 21) ,
		5  : (13 , 10) ,
		6  : (8 , 11) ,
		7  : (12 , 9) ,
		8  : (6 , 7) ,
		9  : (5 , 2) ,
		10 : (0 , 3) ,
		11 : (4 , 1) ,
		12 : (14 , 16) ,
		13 : (17 , 15) ,
		14 : (18 , 19) ,
		15 : (27 , 26)
		}

polar_dos = {}
for key , value in o_polar.items() :
	
	if type(value) is not int :
		
		densities = by_site[value[0]].get_densities()
		densities += by_site[value[1]].get_densities()
		densities /= 2
		polar_dos.update({key : densities})
	
	else :
		densities = by_site[value].get_densities()
		polar_dos.update({key : densities})

non_polar_dos = {}
for key , value in o_non_polar.items() :
	
	if type(value) is not int :
		densities = by_site[value[0]].get_densities()
		densities += by_site[value[1]].get_densities()
		densities /= 2
		non_polar_dos.update({key : densities})
	
	else :
		densities = by_site[value].get_densities()
		non_polar_dos.update({key : densities})

zr_dos = {}
for key , value in zr.items() :
	
	if type(value) is not int :
		densities = by_site[value[0]].get_densities()
		densities += by_site[value[1]].get_densities()
		densities /= 2
		zr_dos.update({key : densities})
	
	else :
		densities = by_site[value].get_densities()
		zr_dos.update({key : densities})

energies = by_site[28].energies - Cdos.efermi

layers = 15
# fig , ax = plt.subplots(layers , sharex = 'col' , sharey = 'row' , figsize = (10 , 8))
from scipy.integrate import trapezoid

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx

lis = []
for i in range(layers + 1) :
	
	if i == 15 :
		break
		
	start = find_nearest(energies , value = -6)
	# start = find_nearest(energies[i], value=-6)
	end = find_nearest(energies , value = 0)
	
	O1_area = trapezoid(polar_dos[i + 1][start :end] , energies[start :end])
	O2_area = trapezoid(non_polar_dos[i + 1][start :end] , energies[start :end])
	Zr_area = trapezoid(zr_dos[i + 1][start :end] , energies[start :end])
	
	lis.append(O1_area + Zr_area + O2_area)
	print(f"charge: {O1_area + Zr_area + O2_area}")

plt.plot(lis)
plt.show()
# for i in range(layers + 1) :
# 	if i == 15 :
# 		break
# 	ax[i].plot(energies , zr_dos[i + 1] + non_polar_dos[i + 1] + polar_dos[i + 1] , c = '#F76608' , alpha = 1 , \
# 		linewidth = 0.9)
# 	# ax[i].plot(energies , non_polar_dos[i + 1] , c = '#00FF00' , alpha = 1 , linewidth = 0.9)
# 	# ax[i].plot(energies , zr_dos[i + 1] , c = '#000000' , alpha = 1 , linewidth = 0.9)
# 	ax[i].axvline(x = 0 , color = 'black' , linestyle = '-.' , alpha = 0.8 , linewidth = "0.8")
# 	ax[i].set_xlim(-6 , 6)
# 	ax[i].set_ylim(0 , 2)
# 	# ax[i].set_yticklabels([0, 2.5])
# 	ax[i].grid(alpha = 0.4)
# 	ax[i].spines['top'].set_visible(False)
# 	ax[i].spines['right'].set_visible(False)
#
# fig.supxlabel("Energy - $E_f$ (eV)")
# fig.supylabel("DOS")
# fig.legend(["$O_p$" , "$O_{np}$" , "Zr"] , loc = "upper right")
#
# plt.subplots_adjust(wspace = 0 , hspace = 0)
#
# plt.show()