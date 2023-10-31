import os
import matplotlib.pyplot as plt
from pymatgen.electronic_structure.core import OrbitalType
from pymatgen.electronic_structure.core import Spin
from pymatgen.electronic_structure.plotter import BSDOSPlotter, BSPlotter, DosPlotter
from pymatgen.io.vasp.outputs import BSVasprun, Vasprun
from scipy.integrate import trapezoid
import numpy as np

#bookkeeping

phase = 'Fm3m'
doping = 1
path = f"/Users/pravanomprakash/Downloads/{phase}_{doping}/static/dos/"


#extract band structure

run = Vasprun(filename = path + "vasprun.xml", parse_projected_eigen=True)
bs = run.get_band_structure(path + "KPOINTS")

print(f"Number of bands: {bs.nb_bands} \n"
      f"Number of Kpoints: {len(bs.kpoints)} \n"
      f"Is this a metal: {bs.is_metal()}\n"
      f"Is this spin-polarized: {bs.is_spin_polarized}\n"
      f"Fermi Energy: {bs.efermi}\n"
      f"Bandgap: {bs.get_band_gap()['energy']}")
#

completeDos = run.complete_dos
dosplot = DosPlotter()
dosplot.add_dos("Total DOS", completeDos)
dosplot.add_dos_dict(completeDos.get_element_dos())
plt = dosplot.get_plot()
plt.ylim(-10, 10)
plt.xlim(-7.5,7.5)
plt.grid()
plt.show()
#

