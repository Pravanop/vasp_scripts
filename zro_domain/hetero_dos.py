import os
import matplotlib.pyplot as plt
import pandas as pd
from pymatgen.electronic_structure.core import OrbitalType
from pymatgen.electronic_structure.core import Spin
from pymatgen.electronic_structure.plotter import BSDOSPlotter , BSPlotter , DosPlotter
from pymatgen.io.vasp.outputs import BSVasprun , Vasprun
from scipy.integrate import trapezoid , simps
import numpy as np
import warnings
from pymatgen.io.cif import CifWriter

warnings.filterwarnings("ignore")

path = f"/Users/pravanomprakash/Downloads/zro_domain_2_0/vasprun.xml"

def analyse(file_path) :
	dosrun = Vasprun(filename = file_path , parse_dos = True)
	Cdos = dosrun.complete_dos
	dos_by_site = []
	for site in Cdos.structure.sites :
		dos_by_site.append(Cdos.get_site_dos(site , ))
	
	return dos_by_site , Cdos
def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx
file_path = path
by_site, Cdos = analyse(file_path)
print(len(by_site))

# o_polar = {
# 		1: (63, 65),
# 		2: (57,61),
# 		3: (55,59),
# 		4: (36,31),
# 		5: (34,29),
# 		6: (32,37),
# 		7: (39,40),
# 		8: (43,49),
# 		9: (46, 52),
# 		10: (44,50),
# 		11: (73,69),
# 		12: (71,67),
# 		13: (78,76),
# 		14: (80,82),
# 		}
#
# o_non_polar = {
# 		1: (66, 64),
# 		2: (56, 60),
# 		3: (58, 62),
# 		4:(30, 35),
# 		5: (33, 38),
# 		6: (41, 42),
# 		7: (47, 53),
# 		8: (51, 45),
# 		9: (54, 48),
# 		10: (68, 72),
# 		11: (70, 74),
# 		12:(75, 77),
# 		13:(84, 83),
# 		14:(79, 81),
# 		}
#
# zr = {
# 		1 : (19,20),
# 		2: (16, 18),
# 		3: (15,17),
# 		4: (2,5),
# 		5:(1,4),
# 		6: (3,6),
# 		7: (8,7),
# 		8: (13,10),
# 		9 : (12, 9),
# 		10: (14,11),
# 		11: (22,21),
# 		12:(23,24),
# 		13:(25,26),
# 		14:(27,28),
# 		}

o_polar = {
		1: (63, 65),
		2: (57,61),
		3: (55,59),
		4: (36,31),
		5: (34,29),
		6: (32,37),
		7: (39,40),
		8: (43,49),
		9: (46, 52),
		10: (44,50),
		11: (73,69),
		12: (71,67),
		13: (78,76),
		14: (80,82),
		15: (80,82),
		}

o_non_polar = {
		1: (66, 64),
		2: (56, 60),
		3: (58, 62),
		4:(30, 35),
		5: (33, 38),
		6: (41, 42),
		7: (47, 53),
		8: (51, 45),
		9: (54, 48),
		10: (68, 72),
		11: (70, 74),
		12:(75, 77),
		13:(85, 83),
		14:(84, 86),
		15:(79, 81),
		}

zr = {
		1 : (19,20),
		2: (16, 18),
		3: (15,17),
		4: (2,5),
		5:(1,4),
		6: (3,6),
		7: (8,7),
		8: (13,10),
		9 : (12, 9),
		10: (14,11),
		11: (22,21),
		12:(23,24),
		13:(25,26),
		14:(27,28),
		15:(27,28),
		}

polar_dos = {}
for key, value in o_polar.items():
	
	if type(value) is not int :
		densities = by_site[value[0]-1].get_densities()
		densities += by_site[value[1]-1].get_densities()
		densities /= 2
		
		if key == 2:
			densities = np.zeros_like(densities)
		polar_dos.update({key : densities})
	
	else :
		densities = by_site[value].get_densities()
		polar_dos.update({key : densities})

non_polar_dos = {}
for key , value in o_non_polar.items() :
	
	if type(value) is not int:
		densities = by_site[value[0]-1].get_densities()
		densities += by_site[value[1]-1].get_densities()
		densities /= 2
		if key == 9:
			densities = np.zeros_like(densities)
			
		non_polar_dos.update({key : densities})
	
	else:
		densities = by_site[value-1].get_densities()
		non_polar_dos.update({key : densities})
		
zr_dos = {}
for key , value in zr.items() :
	
	if type(value) is not int :
		densities = by_site[value[0]-1].get_densities()
		densities += by_site[value[1]-1].get_densities()
		densities /= 2
		zr_dos.update({key : densities})
	
	else :
		densities = by_site[value-1].get_densities()
		zr_dos.update({key : densities})

energies = by_site[42].energies - Cdos.efermi
layers = 14
fig, ax = plt.subplots(layers , sharex='col', sharey='row', figsize=(6,4))

# df = pd.DataFrame(np.array([zr_dos[i] for i in range(1, 16)]))
# df.to_csv("temp0.csv")

for i in range(layers + 1):
	if i == layers:
		break
		
	start = find_nearest(energies , value = -1)
	end = find_nearest(energies , value = 0)
	
	O1_area = trapezoid(polar_dos[i + 1][start :end] , energies[start :end])
	O2_area = trapezoid(non_polar_dos[i + 1][start :end] , energies[start :end])
	Zr_area = trapezoid(zr_dos[i + 1][start :end] , energies[start :end])
	
	print(f"{i} layer, polar: {O1_area}, non_polar: {O2_area}, metal: {Zr_area}")
	
	ax[i].tick_params(axis = 'both' , which = 'major' , labelsize = 8)
	ax[i].plot(energies, polar_dos[i + 1], c = '#009988', alpha = 1, linewidth = 0.9)
	ax[i].plot(energies , non_polar_dos[i + 1] , c = '#EE7733' , alpha = 1 , linewidth = 0.9)
	ax[i].plot(energies , zr_dos[i + 1] , c = '#555555' , alpha = 1 , linewidth = 0.9)
	ax[i].fill_between(energies , polar_dos[i + 1] , where = energies != 0.0 , color = '#009988' , alpha = 0.7)
	ax[i].fill_between(energies , non_polar_dos[i + 1] , where = energies != 0.0 , color = '#EE7733' , alpha = 0.7)
	ax[i].fill_between(energies , zr_dos[i + 1] , where = energies != 0.0 , color = '#555555' , alpha = 0.7)
	# ax[i].plot(energies , non_polar_dos[i + 1] + polar_dos[i + 1] +  zr_dos[i + 1], c = '#009988' , alpha = 1 , linewidth = 0.9)
	# ax[i].fill_between(energies ,non_polar_dos[i + 1] + polar_dos[i + 1] +  zr_dos[i + 1] , where = energies != 0.0 , color = '#009988' , alpha = 0.7)
	ax[i].axvline(x = 0, color = 'black', linestyle = '-.', alpha = 0.8, linewidth = 0.8)
	ax[i].set_xlim(-4, 5)
	ax[i].set_ylim(0, 2)
	ax[i].set_yticks(np.arange(0, 2, 1))
	ax[i].label_outer()
	ax[i].set_title(f'Layer {i+1}', x = 0.4, y = 0, fontsize = 8)
	ax[i].grid( alpha = 0.4)
	ax[i].spines['top'].set_visible(False)
	ax[i].spines['right'].set_visible(False)

fig.supxlabel("Energy - $E_f$ (eV)", fontsize = 8)
fig.supylabel("DOS", fontsize = 8)
fig.legend(["$O_p$", "$O_{np}$", "Zr"], loc = "upper center", ncols = 3, fontsize = 8)

plt.subplots_adjust(wspace=0, hspace=0)

plt.show()