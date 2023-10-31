import numpy as np
from pymatgen.io.lobster import Charge, Icohplist
from pymatgen.electronic_structure.core import Spin
import re
from pymatgen.electronic_structure.plotter import CohpPlotter
from pymatgen.electronic_structure.cohp import CompleteCohp
import matplotlib.pyplot as plt
from scipy.integrate import trapezoid , simps

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx

colors = ['#332288' , "#0077BB" , "#009988" , "#EE7733" , "#BBBBBB"]
cp = CohpPlotter()
doping_list = ["0", "0,5", "1","1,5", "2"]
phase_list = ['pca21', 'pbcm', 'p42nmc']
for phase in phase_list:
		print(phase + ':')
		energies = []
		polar = []
		non_polar = []
		for doping in doping_list:
			oxy_list = {
					'pca21'  : {
							'0' : [(8 , 9 , 10 , 11) , (4 , 5 , 6 , 7)] ,
							'0,5': [(4 , 5 , 6 , 7) , (8 , 9 , 10 , 11)],
							'1' : [(8 , 9 , 10 , 11) , (4 , 5 , 6 , 7)] ,
							'1,5': [(8 , 9 , 10 , 11) , (4 , 5 , 6 , 7)],
							'2' : [(4 , 5 , 6 , 7) , (8 , 9 , 10 , 11)],
							
							} ,
					'pbcm'   : {
							'0' : [(4 , 5 , 6 , 7) , (8 , 9 , 10 , 11)] ,
							'0,5': [(4 , 5 , 6 , 7) , (8 , 9 , 10 , 11)],
							'1' : [(4 , 5 , 6 , 7) , (8 , 9 , 10 , 11)] ,
							'1,5': [(4 , 5 , 6 , 7) , (8 , 9 , 10 , 11)],
							'2' : [(4 , 5 , 6 , 7) , (8 , 9 , 10 , 11)]
							} ,
					'p42nmc' : {
							'0' : [(4 , 5 , 6 , 7) , (8 , 9 , 10 , 11)] ,
							'0,5': [(4 , 5 , 6 , 7) , (8 , 9 , 10 , 11)],
							'1' : [(4 , 5 , 6 , 7) , (8 , 9 , 10 , 11)] ,
							'1,5': [(4 , 5 , 6 , 7) , (8 , 9 , 10 , 11)],
							'2' : [(4 , 5 , 6 , 7) , (8 , 9 , 10 , 11)]
							}
						
					}
			path = f"/Users/pravanomprakash/Library/CloudStorage/Box-Box/Charge Doping/(HfZr)O/ZrO/zro2_relaxed_doped/"
			icohplist = Icohplist(filename=f"{path}{phase}_{doping}/ICOHPLIST.lobster")
			complete_chop = CompleteCohp.from_file(
				fmt = 'LOBSTER' , filename =f"{path}{phase}_{doping}/COHPCAR.lobster", structure_file = f"{path}{phase}_{doping}/POSCAR",
				)
			icohp = icohplist.icohpcollection.as_dict()
			res = [[h, int(re.search(r'\d+', i).group()), int(re.search(r'\d+', j).group()), -(k[Spin.up] + k[
				Spin.down]), l] for h, i, j, k, l in zip(icohp['list_labels'],icohp['list_atom1'], icohp['list_atom2'],
			                                             icohp['list_icohp'],
			                                          icohp['list_length'])]
			polar_icohp = []
			non_polar_icohp = []
			polar_length = []
			non_polar_length = []
			polar_list = []
			non_polar_list = []
			for i in res:
				
				if i[1] in oxy_list[phase][doping][0]:
					polar_icohp.append(i[3])
					polar_length.append(i[4])
					polar_list.append(i[0])
				if i[1] in oxy_list[phase][doping][1]:
					non_polar_icohp.append(i[3])
					non_polar_length.append(i[4])
					non_polar_list.append(i[0])
			
	
			
			plotlabelpolar = 'Polar'
			plotlabelnonpolar = 'Non-polar'
			
			polar.append(
				- complete_chop.get_summed_cohp_by_label_list(
						polar_list , divisor = 1 , summed_spin_channels =
						True
						).cohp[Spin.up])
			energies.append(
				complete_chop.get_summed_cohp_by_label_list(
					non_polar_list , divisor = 1 ,
					summed_spin_channels =
					True
					).energies - complete_chop.get_summed_cohp_by_label_list(
					polar_list , divisor = 1 ,
					summed_spin_channels =
					True
					).efermi )
			non_polar.append(- complete_chop.get_summed_cohp_by_label_list(
						non_polar_list , divisor = 1 , summed_spin_channels =
						True
						).cohp[Spin.up])
		
		for i in range(len(polar)) :
			start = find_nearest(energies[i], value=-6)
			end = find_nearest(energies[i] , value = 1)
			energy = energies[i][start:end]
			
			print(f"ICOHP from (0, 1) for {i/10} h/f.u. \nPolar: {round(trapezoid(polar[i][start:end],energy),3)}")
			print(f"Non polar: {round(trapezoid(non_polar[i][start:end], energy),3)}")
			
		fig , axes = plt.subplots(len(polar),1, figsize = (6 , 6), sharex = True, sharey = True)
		for i in range(len(polar)):
			axes[i].plot(energies[i],polar[i] , c = "#0077BB", linewidth = 1 , alpha = 0.8 , linestyle = '-')
			axes[i].plot(energies[i],non_polar[i],  c = '#CC6677', linewidth = 1 , alpha = 0.8 , linestyle = '-')
			axes[i].fill_between(energies[i], non_polar[i], where = energies[i] < 1, color = '#CC6677', alpha = 0.7)
			axes[i].fill_between(energies[i], polar[i], where = energies[i] < 1, color = '#0077BB', alpha = 0.7)
			axes[i].axhline(y = 0 , c = '#000000' , linewidth = 0.8 , alpha = 0.8 , linestyle = '-.')
			axes[i].axvline(x = 0 , c = '#000000' , linewidth = 0.8 , alpha = 0.8 , linestyle = '-.')
			axes[i].set_xlim([-6,6])
		axes[-1].set_xlabel("$E - E_{f}$")
		axes[0].legend(['Polar Zr-O Bonds' , 'Non-polar Zr-O Bonds'], loc = "upper right", ncols = 1)

		fig.supylabel("-COHP")
		plt.subplots_adjust(wspace = 0 , hspace = 0)
		plt.show()

