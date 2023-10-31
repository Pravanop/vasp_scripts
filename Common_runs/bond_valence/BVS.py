from pymatgen.analysis.bond_valence import calculate_bv_sum
from pymatgen.analysis.graphs import StructureGraph
from pymatgen.analysis.local_env import CrystalNN
from pymatgen.core import Structure

for phase in ['G5z', 'M1z']:
	print(phase)
	for doping in ['0', '1', '2']:
		print(doping)
		filename = (f'/Users/pravanomprakash/Downloads/SI_polar_antipolar_modes/{phase}_'
		            f'{doping}.cif')
		
		structure = Structure.from_file(filename)
		bv_sum = {}
		for site in range(len(structure)):
			nn_list = structure.get_neighbors(structure[site], r = 2.4)
			bv = calculate_bv_sum(structure[site],nn_list)
			bv_sum[str(structure[site].specie) + str(site)] = round(bv,3)
		print(bv_sum)