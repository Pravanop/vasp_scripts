import os
import matplotlib.pyplot as plt
from pymatgen.electronic_structure.core import OrbitalType, Orbital
from pymatgen.electronic_structure.core import Spin
from pymatgen.electronic_structure.plotter import BSDOSPlotter , BSPlotter , DosPlotter
from pymatgen.io.vasp.outputs import BSVasprun , Vasprun
from scipy.integrate import trapezoid , simps
import numpy as np
import warnings

warnings.filterwarnings("ignore")
# bookkeeping

path = f"/Users/pravanomprakash/Library/CloudStorage/Box-Box/Charge Doping/(HfZr)O/ZrO/ZrO_dos_new/"
phase = 'pca21'

def analyse(file_path) :
	dosrun = Vasprun(filename = file_path , parse_dos = True,)
	Cdos = dosrun.complete_dos_normalized
	dos_by_site = []
	print(Cdos.efermi, Cdos.get_cbm_vbm())
	for site in Cdos.structure.sites :
		dos_by_site.append(Cdos.get_site_dos(site,))

	
	return dos_by_site , Cdos

Op_list, Onp_list, Zr_list = [], [], []
energies = []
oxy_list = {
		'pca21'  : {
				'0'   : [(8 , 9 , 10 , 11) , (4 , 5 , 6 , 7)] ,
				'f1' : [(4 , 5 , 6 , 7) , (8 , 9 , 10 , 11)] ,
				'1'   : [(8 , 9 , 10 , 11) , (4 , 5 , 6 , 7)] ,
				'f3' : [(8 , 9 , 10 , 11) , (4 , 5 , 6 , 7)] ,
				'2'   : [(4 , 5 , 6 , 7) , (8 , 9 , 10 , 11)] ,
				
				} ,
		'pbcm'   : {
				'0'   : [(4 , 5 , 6 , 7) , (8 , 9 , 10 , 11)] ,
				'f1' : [(4 , 5 , 6 , 7) , (8 , 9 , 10 , 11)] ,
				'1'   : [(4 , 5 , 6 , 7) , (8 , 9 , 10 , 11)] ,
				'f3' : [(4 , 5 , 6 , 7) , (8 , 9 , 10 , 11)] ,
				'2'   : [(4 , 5 , 6 , 7) , (8 , 9 , 10 , 11)]
				} ,
		'p42nmc' : {
				'0'   : [(4 , 5 , 6 , 7) , (8 , 9 , 10 , 11)] ,
				'f1' : [(4 , 5 , 6 , 7) , (8 , 9 , 10 , 11)] ,
				'1'   : [(4 , 5 , 6 , 7) , (8 , 9 , 10 , 11)] ,
				'f3' : [(4 , 5 , 6 , 7) , (8 , 9 , 10 , 11)] ,
				'2'   : [(4 , 5 , 6 , 7) , (8 , 9 , 10 , 11)]
				}
			
		}
for i in ['0','f1', '1', 'f3','2']:
	
	file_path = path + f"{phase}_{i}.xml"
	by_site, Cdos = analyse(file_path)
	energies.append(by_site[0].energies - Cdos.efermi)
	p_list = oxy_list[phase][i][0]
	np_list = oxy_list[phase][i][1]
	Op_list.append((by_site[p_list[0]].get_densities() + by_site[p_list[1]].get_densities() + by_site[
		p_list[2]].get_densities() + by_site[p_list[3]].get_densities())/4)
	Onp_list.append((by_site[np_list[0]].get_densities() + by_site[np_list[1]].get_densities() + by_site[
		np_list[2]].get_densities() + by_site[np_list[3]].get_densities())/4)
	Zr_list.append((by_site[0].get_densities() + by_site[1].get_densities() + by_site[2].get_densities() + by_site[
		3].get_densities())/4)

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx

for i in range(5):

	start = find_nearest(energies[i], value=0)
	end = find_nearest(energies[i], value=1)

	O1_area = trapezoid(Op_list[i][start:end], energies[i][start:end])
	O2_area = trapezoid(Onp_list[i][start:end], energies[i][start:end])
	Zr_area = trapezoid(Zr_list[i][start:end], energies[i][start:end])

	print(f"{i} doping, polar: {O1_area}, non_polar: {O2_area}, metal: {Zr_area}")
	
fig, ax = plt.subplots(3 , sharex='col', sharey='row', figsize=(10,6))
for i in range(3):
	ax[i].plot(energies[i], Op_list[i], c = '#0077BB', alpha = 1, linewidth = 0.9)
	ax[i].plot(energies[i], Onp_list[i], c = '#CC6677', alpha = 1, linewidth = 0.9)
	ax[i].plot(energies[i], Zr_list[i], c = '#33bbee', alpha = 1, linewidth = 0.9)
	ax[i].axvline(x = 0, color = 'black', linestyle = '-.', alpha = 0.8, linewidth = "0.8")
	ax[i].fill_between(energies[i] , Op_list[i] , where = energies[i] > 0.0 , color = '#0077BB' , alpha = 0.7)
	ax[i].fill_between(energies[i] , Onp_list[i] , where = energies[i] > 0.0 , color = '#CC6677' , alpha = 0.7)
	ax[i].set_xlim(-6, 6)
	ax[i].set_ylim(0, 3)
	ax[i].grid( alpha = 0.2)
	ax[i].spines['top'].set_visible(False)
	ax[i].spines['right'].set_visible(False)
	if i == 0:
		ax[i].legend(["$O_p$" , "$O_{np}$" , "Zr"] , loc = "right")
		ax[i].set_xlabel("Energy - $E_f$ (eV)")
	if i == 1:
		ax[i].set_ylabel("DOS")
	ax[i].label_outer()
	ax[i].set_yticks(np.arange(0 , 1.5 , 3))

fig.suptitle(f"$ZrO_2$ {phase} DOS for increasing charge density (holes/f.u.)")
# fig.legend(["$O_p$", "$O_{np}$", "Zr"], loc = "right")

plt.subplots_adjust(wspace=0, hspace=0)
# plt.savefig('/Users/pravanomprakash/Library/CloudStorage/Box-Box/Charge Doping/Figures/fig4b.png', dpi=100,
#             bbox_inches='tight')
plt.show()
