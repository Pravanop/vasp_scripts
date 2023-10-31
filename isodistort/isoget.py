from isodistort import get
import os

path = '/Users/pravanomprakash/Library/CloudStorage/Box-Box/Charge Doping/(HfZr)O/ZrO/ZrO_relaxed_sym_new/'
lfolder = sorted(os.listdir(path))
out_path = '/Users/pravanomprakash/Library/CloudStorage/Box-Box/Charge Doping/(HfZr)O/ZrO/ZrO_pathway/distortions/'
for i in ["0", "0,5", "1", "1,5", "2"] :
    get(cifname = f"{path}pbcm_{i}.cif",
        outfname = f'{out_path}pbcm_pca21_{i}.txt',
        subcif = f"{path}pbcm_{i}.cif",
        method = 4,
        isoformat = 'distortionfile',
        basis = [0, 1, 0, -1, 0, 0, 0, 0, 1],
        specify = True
        )