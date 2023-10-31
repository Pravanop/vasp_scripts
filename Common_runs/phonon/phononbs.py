import os
import shutil
import subprocess
from mainRun import run

path = "/Users/pravanomprakash/Downloads/phonopy"

lfolder = os.listdir(path)
if not os.path.isdir(f"{path}/inp/"):
	os.mkdir(path=f"{path}/inp/")

for i in lfolder:

	if i == '.DS_Store':
		continue
	if not os.path.isdir(f"{path}/inp/{i[:-5]}/") :
		os.mkdir(path=f"{path}/inp/{i[:-5]}/")
	try:
		shutil.copy(src = f"{path}/{i}", dst = f"{path}/inp/{i[:-5]}/POSCAR")
	except:
		continue
	size = "2 2 2"
	subprocess.call(["phonopy", "-d", f"--dim={size}", "--tolerance=1e-2"], cwd = f"{path}/inp/{i[:-5]}/",
	                shell = False)
	lfolder1 = os.listdir(f"{path}/inp/{i[:-5]}/")
	print(len(lfolder1))
	for j in lfolder1:
		path1 = f"{path}/inp/{i[:-5]}/"
		
		
		
		if j == "phonopy_disp.yaml":
			continue
		if j == "SPOSCAR":
			continue
		if j == "POSCAR" :
			continue
		
		hole = i[-7 :-5]
		nelect = 768 - 4 * 8 * (float(hole) / 100)
		if not os.path.isdir(f"{path1}inp/") :
			os.mkdir(f"{path1}inp/")
		shutil.move(src = f"{path1}/{j}", dst = f"{path1}inp/")
		runjob_dict = {
				"name"      : "structure_relax" ,
				"comp_name" : "shared" ,
				"nodes"     : 1 ,
				"cores"     : 96 ,
				"hours"     : 3 ,
				"loop"      : False ,
				"static"    : " "
				}

		run(
			cif_folder = f"{path1}inp/" ,
			run_folder = f"{path}/{i[:-5]}/" ,
			func = "LDA" ,
			compound = "zro2" ,
			sel_dyn = "" ,
			runjob_dict = runjob_dict ,
			incar_ref = "/Users/pravanomprakash/Library/CloudStorage/Box-Box/vasp_scripts/ref_files/INCAR/" ,
			incar_set = {"NELECT" : f"{nelect}",
						"MAGMOM": "96*0.6"} ,
			type = ""
			)


		