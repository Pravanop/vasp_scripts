import os
import matplotlib.pyplot as plt
from pymatgen.electronic_structure.core import OrbitalType
from pymatgen.electronic_structure.core import Spin
from pymatgen.electronic_structure.plotter import BSDOSPlotter , BSPlotter , DosPlotter
from pymatgen.io.vasp.outputs import BSVasprun , Vasprun
from scipy.integrate import trapezoid , simps
import numpy as np
import warnings

def analyse(file_path) :
	dosrun = Vasprun(filename = file_path , parse_dos = True)
	Cdos = dosrun.complete_dos
	s = Cdos.structure
	s.to('POSCAR')
	dos_by_site = []
	for site in Cdos.structure.sites :
		dos_by_site.append(Cdos.get_site_dos(site , ))
	
	return dos_by_site , Cdos

file_path = "/Users/pravanomprakash/Library/CloudStorage/Box-Box/Charge Doping/(HfZr)O/ZrO/ZrO_dos/pbcm_2.xml"
by_site, Cdos = analyse(file_path)
energies = by_site[0].energies - Cdos.efermi

for i in range(len(by_site)):
	plt.plot(energies, list(by_site[i].get_densities()))

plt.legend(range(len(by_site)))
plt.xlim(-10, 10)
plt.show()