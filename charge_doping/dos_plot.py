import os
import matplotlib.pyplot as plt
from pymatgen.electronic_structure.core import OrbitalType, Orbital
from pymatgen.electronic_structure.core import Spin
from pymatgen.electronic_structure.plotter import BSDOSPlotter , BSPlotter , DosPlotter
from pymatgen.io.vasp.outputs import BSVasprun , Vasprun
from scipy.integrate import trapezoid , simps
import numpy as np
import warnings

warnings.filterwarnings("ignore")

doping = 3
#path = f"/Users/pravanomprakash/Library/CloudStorage/Box-Box/Research_Rotation/HfZrO/hafnia/pbcm_doping/"
path = "/Users/pravanomprakash/Downloads/structures/vasprun/"
#filename = path + f"pbcm_pca21_+0.{doping}.xml"
filename = path + f"vasprun.xml"

dosrun = Vasprun(filename = filename , parse_dos = True)
Cdos = dosrun.complete_dos
print(dosrun.final_structure)

dos_by_site_px = []
dos_by_site_py = []
dos_by_site_pz = []
dos_by_site_pz2 = []
dos_by_site_pz3 = []
dos_by_site_pz4 = []
dos_by_site_pz5 = []
dos_by_site_pz6 = []
dos_by_site_pz7 = []
for site in Cdos.structure.sites :
	# dos_by_site_px.append(Cdos.get_site_orbital_dos(site , Orbital.dxz))
	# dos_by_site_py.append(Cdos.get_site_orbital_dos(site , Orbital.dxy))
	# dos_by_site_pz.append(Cdos.get_site_orbital_dos(site , Orbital.dx2))
	# dos_by_site_pz2.append(Cdos.get_site_orbital_dos(site , Orbital.dyz))
	# dos_by_site_pz3.append(Cdos.get_site_orbital_dos(site , Orbital.dz2))
	dos_by_site_pz4.append(Cdos.get_site_orbital_dos(site , Orbital.px))
	dos_by_site_pz5.append(Cdos.get_site_orbital_dos(site , Orbital.py))
	dos_by_site_pz6.append(Cdos.get_site_orbital_dos(site , Orbital.pz))

# plt.plot(dos_by_site_px[0].energies - Cdos.efermi, dos_by_site_px[0].get_densities())
# plt.plot(dos_by_site_py[0].energies - Cdos.efermi, dos_by_site_py[0].get_densities())
# plt.plot(dos_by_site_pz[0].energies - Cdos.efermi, dos_by_site_pz[0].get_densities())
# plt.plot(dos_by_site_pz2[0].energies - Cdos.efermi, dos_by_site_pz2[0].get_densities())
# plt.plot(dos_by_site_pz3[0].energies - Cdos.efermi, dos_by_site_pz3[0].get_densities())
plt.plot(dos_by_site_pz4[0].energies - Cdos.efermi, dos_by_site_pz4[0].get_densities())
plt.plot(dos_by_site_pz5[0].energies - Cdos.efermi, dos_by_site_pz5[0].get_densities())
plt.plot(dos_by_site_pz6[0].energies - Cdos.efermi, dos_by_site_pz6[0].get_densities())

plt.axvline(x = 0, color = 'black', linestyle = '-.', alpha = 0.8, linewidth = "0.8")
# plt.legend(["dxz", "dxy", "dx2", "dyz", "dz2", "px", "py", "pz"])
plt.legend([ "px", "py", "pz"])
plt.ylim(0, 0.2)
plt.xlim(-2,2)
plt.show()
# dosplot = DosPlotter()
# dosplot.add_dos("Op_px",dos_by_site_px[8])
# dosplot.add_dos("Op_py",dos_by_site_py[8])
# dosplot.add_dos("Op_pz",dos_by_site_pz[8])
# plt = dosplot.get_plot()
# plt.ylim(-0.25, 0.25)
# plt.xlim(-2,2)
# plt.grid()
# plt.show()
