from pymatgen.symmetry.bandstructure import HighSymmKpath
from pymatgen.core.structure import Structure
from pymatgen.io.vasp.inputs import Kpoints
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer

struct = Structure.from_file("/Users/pravanomprakash/Library/CloudStorage/Box-Box/Research_Rotation/HfZrO/hafnia"
                             "/pathways/pbcm_pca21/no_doping/pbcm_pca21/cif0010.cif")
kpath = HighSymmKpath(struct)

kpts = Kpoints.automatic_linemode(divisions=40,ibz=kpath)
kpts.write_file("KPOINTS_nsc")