import os

from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
from pymatgen.core.structure import Structure
from pymatgen.io.cif import CifWriter

path = '/Users/pravanomprakash/Downloads/more_points'
lfolder = sorted(os.listdir(path))
out_path = '/Users/pravanomprakash/Downloads/more_points_sym/'
for file in lfolder:
    if file == ".DS_Store":
        continue
    filename = f"{file}"
    
    structure = Structure.from_file(f"{path}/{filename}")
    
    spg = SpacegroupAnalyzer(structure, symprec = 0.01)
    print(f"{file} : {spg.get_space_group_symbol()} ({spg.get_space_group_number()})")
    cifwrite = CifWriter(struct = structure, symprec = 0.01)
    cifwrite.write_file(f"{out_path}{file[:-5]}.cif")
