from pymatgen.analysis.bond_valence import BVAnalyzer, calculate_bv_sum
from pymatgen.core.structure import Structure
from pymatgen.analysis.local_env import CrystalNN

s = Structure.from_file("/Users/pravanomprakash/Downloads/structures/p21c_f3.cif")
nn_list = CrystalNN().get_nn_data(s, 1)
print(nn_list)
print(calculate_bv_sum(s[1], nn_list[0]))
