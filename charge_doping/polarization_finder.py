from pymatgen.core.structure import Structure
import numpy as np
import os

folder_path = "/Users/pravanomprakash/Library/CloudStorage/Box-Box/Charge Doping/(HfZr)O/more_points_sym"
lfolder = os.listdir(folder_path)
lfolder.sort()
for i in lfolder:
	if "pca" in i:
		print(i)
		s = Structure.from_file(f"{folder_path}/{i}")
		
		dist = (s[3].frac_coords[2] - s[5].frac_coords[2])*s.lattice.abc[2]
		polar = np.round(2*dist,4)
		conversion = polar*1e-8*1.602e-19*1e+6/(131*1e-24)
		polarization = conversion*4
		print(polarization/68*100)


