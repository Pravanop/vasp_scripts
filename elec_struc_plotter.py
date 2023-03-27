import os
import matplotlib.pyplot as plt

from pymatgen.electronic_structure.core import Spin
from pymatgen.electronic_structure.plotter import BSDOSPlotter, BSPlotter, DosPlotter
from pymatgen.io.vasp.outputs import BSVasprun, Vasprun

path = "/Users/pravanomprakash/Downloads/vasprun.xml"
run = BSVasprun(f"{path}", parse_projected_eigen=True)
bs = run.get_band_structure("KPOINTS")

print("number of bands", bs.nb_bands)
print("number of kpoints", len(bs.kpoints))
print("Spin Polarized: ", bs.is_spin_polarized)

print(bs.get_band_gap())
bsplot = BSPlotter(bs)

# bsplot.get_plot(ylim=(-20, 10), zero_to_efermi=True)
bsplot.get_plot(bs = bs)
print(bs.efermi)

# add some features
ax = plt.gca()
ax.set_title("NiO Band Structure", fontsize=20)
xlim = ax.get_xlim()
ax.hlines(0, xlim[0], xlim[1], linestyles="dashed", color="black")

# add legend
ax.plot((), (), "b-", label="spin up")
ax.plot((), (), "r--", label="spin down")
ax.legend(fontsize=16, loc="upper left")

plt.show()