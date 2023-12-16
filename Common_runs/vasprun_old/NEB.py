from pymatgen.core.structure import Structure
import os

file_path_final = "/Users/pravanomprakash/Downloads/zro_neb_test_final.vasp"
file_path_initial = "/Users/pravanomprakash/Downloads/zro_neb_test_final.vasp"
out_folder = "/Users/pravanomprakash/Downloads/neb_zro_test/"

s = Structure.from_file(file_path_initial)
s_fin = Structure.from_file(file_path_final)
images = 8
neb = s.interpolate(s_fin, nimages = images + 1)
for idx, i in enumerate(neb):
	os.mkdir(f"{out_folder}0{idx}/")
	i.to(f"{out_folder}0{idx}/POSCAR")

print(len(neb))
