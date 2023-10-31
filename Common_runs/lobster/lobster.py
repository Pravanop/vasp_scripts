from pymatgen.electronic_structure.cohp import CompleteCohp
from pymatgen.electronic_structure.plotter import CohpPlotter
from pymatgen.electronic_structure.core import OrbitalType , Orbital

COHP_path = "/Users/pravanomprakash/Downloads/zro2_relaxed_doped/pca21_1/COHPCAR.lobster"
POSCAR_path = "/Users/pravanomprakash/Downloads/zro2_relaxed_doped/pca21_1/POSCAR"

complete_coop = CompleteCohp.from_file(fmt = 'LOBSTER' , filename = COHP_path , structure_file = POSCAR_path)
label = "13"
non_polar_label = "15"
cp = CohpPlotter()

plotlabel1 = "Zr-O (polar)"
plotlabel2 = "Zr-O (non-polar)"
#
# for i in range(1, 8):
# 	label = str(i)
# 	if i < 4:
# 		plotlabel1 = f"Zr-O {i} (polar)"
# 	else:
# 		plotlabel1 = f"Zr-O {i} (non polar)"
cp.add_cohp(
	plotlabel1 , complete_coop.get_orbital_resolved_cohp(
		label = '13' ,
		orbitals = [[2, Orbital.pz], [4, Orbital.dxy]],
		summed_spin_channels = True
		)
	)

# cp.add_cohp(plotlabel2, complete_coop.get_cohp_by_label(label=non_polar_label))


x = cp.get_plot(integrated = False)
x.ylim([-6 , 6])

x.show()
