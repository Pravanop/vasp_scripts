from pymatgen.io.vasp.outputs import BSVasprun , Vasprun
from scipy.integrate import trapezoid , simps
import numpy as np
import warnings
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore")

def gd(dos):
    return dos.get_densities()

mode = ['G5z', 'M1z']
mode_name = ['$\Gamma_{z}^{5}$', '$M_{z}^{1}$']
doping = 2
energies = []
Zr = []
Op = []
Onp = []

for i in range(len(mode)):
    
    path = f"/Users/pravanomprakash/Downloads/results/"
    phase = f'{mode[i]}_{doping}'
    
    dosrun = Vasprun(filename = f"{path}{phase}" , parse_dos = True,)
    Cdos = dosrun.complete_dos_normalized
    dos_by_site = []
    for site in Cdos.structure.sites :
        dos_by_site.append(Cdos.get_site_dos(site , ))
    
    energies.append(dos_by_site[0].energies - Cdos.efermi)
    Zr.append((gd(dos_by_site[0])+gd(dos_by_site[1]) + gd(dos_by_site[2]) + gd(dos_by_site[3]))/4)
    Op.append((gd(dos_by_site[4])+gd(dos_by_site[5])+gd(dos_by_site[6])+gd(dos_by_site[7]))/4)
    Onp.append((gd(dos_by_site[8])+gd(dos_by_site[9])+gd(dos_by_site[10])+gd(dos_by_site[11]))/4)

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx

for i in range(len(mode)):

    start = find_nearest(energies[i], value=0)
    end = find_nearest(energies[i], value=1)
    
    O1_area = np.round(trapezoid(Op[i][start:end], energies[i][start:end]), 3)
    O2_area = np.round(trapezoid(Onp[i][start:end], energies[i][start:end]), 3)
    Zr_area = np.round(trapezoid(Zr[i][start:end], energies[i][start:end]), 3)

    print(f"{i} doping, polar: {O1_area}, non_polar: {O2_area}, metal: {Zr_area}")
    
fig, ax = plt.subplots(len(mode) , sharex='col', sharey='row', figsize=(10,6))
for i in range(len(mode)):
    ax[i].plot(energies[i] , Op[i] , c = '#0077BB' , alpha = 1 , linewidth = 0.9)
    ax[i].plot(energies[i] , Onp[i] , c = '#CC6677' , alpha = 1 , linewidth = 0.9)
    ax[i].plot(energies[i] , Zr[i] , c = '#33bbee' , alpha = 1 , linewidth = 0.9)
    ax[i].axvline(x = 0 , color = 'black' , linestyle = '-.' , alpha = 0.8 , linewidth = "0.8")
    ax[i].fill_between(energies[i] , Op[i] , where = energies[i] > 0.0 , color = '#0077BB' , alpha = 0.7)
    ax[i].fill_between(energies[i] , Onp[i] , where = energies[i] > 0.0 , color = '#CC6677' , alpha = 0.7)
    ax[i].set_xlim(-6 , 6)
    ax[i].set_ylim(0 , 3)
    ax[i].grid(alpha = 0.2)
    ax[i].spines['top'].set_visible(False)
    ax[i].spines['right'].set_visible(False)
    ax[i].set_title(mode_name[i])
    
ax[0].legend(['$O_{p}$', '$O_{np}$'])
# plt.show()
