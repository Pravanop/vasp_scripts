from pymatgen.core.structure import Structure

s = Structure.from_file("/Users/pravanomprakash/Downloads/structures/misc_structures/pca21_0.cif")
s.make_supercell(2)

s.to(fmt='POSCAR', filename = 'pca21_222')
print(s)