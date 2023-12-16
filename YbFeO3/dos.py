import matplotlib.pyplot as plt
import numpy as np
from pymatgen.io.vasp import Vasprun
from scipy.integrate import trapezoid, simps
from pymatgen.electronic_structure.core import Spin
import warnings
import pandas as pd
warnings.filterwarnings("ignore")

file_path = "/Users/pravanomprakash/Downloads/YbFeO3/vasprun.xml"
dosrun = Vasprun(filename = file_path, parse_dos = True)
Cdos = dosrun.complete_dos
print(f"Fermi: {Cdos.efermi}, CBM-VBM: {Cdos.get_cbm_vbm()}, Bandgap: {Cdos.get_gap()}")
total_dos = Cdos.get_smeared_densities(sigma = 0.03)
total_dos_up = total_dos[Spin.up]
total_dos_down = total_dos[Spin.down]
# total_dos_down = Cdos.get_densities(Spin.down)
energies = Cdos.energies - Cdos.efermi

dos_by_site = []
for site in Cdos.structure.sites :
	dos_by_site.append(Cdos.get_site_dos(site , ))
	
layer_path = "/Users/pravanomprakash/Library/CloudStorage/Box-Box/New_Project/YbFO_layers.csv"
df = np.array(pd.read_csv(layer_path))[:, 1:]
layer_dos_yb = []
layer_dos_O = []
layer_dos_Fe = []

for idx, i in enumerate(df.T):
	
	
	yb = (dos_by_site[i[0]-1].get_densities() + dos_by_site[i[1]-1].get_densities())
	Fe = (dos_by_site[i[-1]-1].get_densities() + dos_by_site[i[-2]-1].get_densities())
	O = (dos_by_site[i[2]-1].get_densities() + dos_by_site[i[3]-1].get_densities() + dos_by_site[i[
		                                                                                             4]-1].get_densities() + dos_by_site[i[5]-1].get_densities()+ dos_by_site[i[6]-1].get_densities() +
	dos_by_site[i[7]-1].get_densities())
	
	if idx == 6 or idx == 18:
		Fe = (yb + Fe)
		yb = np.zeros_like(yb)
	
	layer_dos_yb.append(yb)
	layer_dos_Fe.append(Fe)
	layer_dos_O.append(O)

layers = len(layer_dos_yb)
fig, ax = plt.subplots(layers , sharex='col', sharey='row', figsize=(10,8))

count = 0
for j in range(layers):
	
	ax[j].plot(energies, layer_dos_yb[j])
	ax[j].plot(energies, layer_dos_Fe[j])
	ax[j].plot(energies, layer_dos_O[j])
	ax[j].set_xlim(-3, 3)
	ax[j].set_ylim(0, 10)
	ax[j].axvline(x = 0 , color = 'black' , linestyle = '-.' , alpha = 0.8 , linewidth = 0.8)
	ax[j].label_outer()
	ax[j].set_title(f'Layer {count + 1}' , x = 0.4 , y = 0 , fontsize = 8)
	ax[j].grid(alpha = 0.4)
	ax[j].spines['top'].set_visible(False)
	ax[j].spines['right'].set_visible(False)
	count += 1
plt.legend(['Yb', 'Fe', 'O'])
plt.show()



