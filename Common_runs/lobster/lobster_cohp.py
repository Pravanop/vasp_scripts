from pymatgen.electronic_structure.plotter import CohpPlotter
from pymatgen.electronic_structure.cohp import CompleteCohp
from pymatgen.electronic_structure.core import Spin

path = f"/Users/pravanomprakash/Library/CloudStorage/Box-Box/Charge Doping/(HfZr)O/ZrO/zro2_relaxed_doped/"
phase = "pca21"
doping = "0"
oxy_list = {
		'pca21'  : {
				'0'   : [(8 , 9 , 10 , 11) , (4 , 5 , 6 , 7)] ,
				'0,5' : [(4 , 5 , 6 , 7) , (8 , 9 , 10 , 11)] ,
				'1'   : [(8 , 9 , 10 , 11) , (4 , 5 , 6 , 7)] ,
				'1,5' : [(8 , 9 , 10 , 11) , (4 , 5 , 6 , 7)] ,
				'2'   : [(4 , 5 , 6 , 7) , (8 , 9 , 10 , 11)] ,
				
				} ,
		'pbcm'   : {
				'0'   : [(4 , 5 , 6 , 7) , (8 , 9 , 10 , 11)] ,
				'0,5' : [(4 , 5 , 6 , 7) , (8 , 9 , 10 , 11)] ,
				'1'   : [(4 , 5 , 6 , 7) , (8 , 9 , 10 , 11)] ,
				'1,5' : [(4 , 5 , 6 , 7) , (8 , 9 , 10 , 11)] ,
				'2'   : [(4 , 5 , 6 , 7) , (8 , 9 , 10 , 11)]
				} ,
		'p42nmc' : {
				'0'   : [(4 , 5 , 6 , 7) , (8 , 9 , 10 , 11)] ,
				'0,5' : [(4 , 5 , 6 , 7) , (8 , 9 , 10 , 11)] ,
				'1'   : [(4 , 5 , 6 , 7) , (8 , 9 , 10 , 11)] ,
				'1,5' : [(4 , 5 , 6 , 7) , (8 , 9 , 10 , 11)] ,
				'2'   : [(4 , 5 , 6 , 7) , (8 , 9 , 10 , 11)]
				}
			
		}
path = f"/Users/pravanomprakash/Library/CloudStorage/Box-Box/Charge Doping/(HfZr)O/ZrO/zro2_relaxed_doped/"
icohplist = Icohplist(filename = f"{path}{phase}_{doping}/ICOHPLIST.lobster")
complete_chop = CompleteCohp.from_file(
		fmt = 'LOBSTER' , filename = f"{path}{phase}_{doping}/COHPCAR.lobster" ,
		structure_file = f"{path}{phase}_{doping}/POSCAR" ,
		)
icohp = icohplist.icohpcollection.as_dict()
res = [[h , int(re.search(r'\d+' , i).group()) , int(re.search(r'\d+' , j).group()) , -(k[Spin.up] + k[
	Spin.down]) , l] for h , i , j , k , l in zip(
		icohp['list_labels'] , icohp['list_atom1'] , icohp['list_atom2'] ,
		icohp['list_icohp'] ,
		icohp['list_length']
		)]
polar_icohp = []
non_polar_icohp = []
polar_length = []
non_polar_length = []
polar_list = []
non_polar_list = []
for i in res :
	
	if i[1] in oxy_list[phase][doping][0] :
		polar_icohp.append(i[3])
		polar_length.append(i[4])
		polar_list.append(i[0])
	if i[1] in oxy_list[phase][doping][1] :
		non_polar_icohp.append(i[3])
		non_polar_length.append(i[4])
		non_polar_list.append(i[0])

plotlabelpolar = 'Polar'
plotlabelnonpolar = 'Non-polar'

polar.append(
		- complete_chop.get_summed_cohp_by_label_list(
				polar_list , divisor = 1 , summed_spin_channels =
				True
				).icohp[Spin.up]
		)
energies.append(
		complete_chop.get_summed_cohp_by_label_list(
				non_polar_list , divisor = 1 ,
				summed_spin_channels =
				True
				).energies - complete_chop.get_summed_cohp_by_label_list(
				polar_list , divisor = 1 ,
				summed_spin_channels =
				True
				).efermi
		)
non_polar.append(
	- complete_chop.get_summed_cohp_by_label_list(
			non_polar_list , divisor = 1 , summed_spin_channels =
			True
			).icohp[Spin.up]
	)


