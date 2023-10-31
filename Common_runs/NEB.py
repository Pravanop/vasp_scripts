from pymatgen.core.structure import Structure
import os

file_path_initial = "/Users/pravanomprakash/Library/CloudStorage/Box-Box/ZrO_domain/pca21_14L_2_1.vasp"
file_path_final = "/Users/pravanomprakash/Library/CloudStorage/Box-Box/ZrO_domain/pca21_14L_2_3.vasp"
out_folder = "/Users/pravanomprakash/Downloads/neb_zro_domain/"

s = Structure.from_file(file_path_initial)
s_fin = Structure.from_file(file_path_final)
images = 8
neb = s.interpolate(s_fin, nimages = images + 1, autosort_tol = 1.5)
for idx, i in enumerate(neb):
	os.mkdir(f"{out_folder}0{idx}/")
	i.to(f"{out_folder}0{idx}/POSCAR")

print(len(neb))
