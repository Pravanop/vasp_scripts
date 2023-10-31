import os
import json
from tqdm import tqdm
from normalRun import normal_run
from Common_runs.run_files.runjob import runjob


def run(cif_folder, run_folder, func, compound, sel_dyn, runjob_dict, incar_ref, incar_set, type):
    lfolder = sorted(os.listdir(cif_folder))

    with open(f'{incar_ref}INCAR_relax.json') as f:
        incar_set_relax = json.load(f)

    with open(f'{incar_ref}INCAR_static.json') as f:
        incar_set_static = json.load(f)
    
    with open(f'{incar_ref}INCAR_dos.json') as f:
        incar_set_dos = json.load(f)

    if '.DS_Store' in lfolder:
        lfolder.remove('.DS_Store')
    
    for idx, cif_file in tqdm(enumerate(lfolder)):
        path = f"{run_folder}{cif_file}/"
        runjob_dict.update({'name': cif_file})
        if not os.path.exists(path):
            os.makedirs(path)
        if type == "relax":
            incar_set_relax.update(incar_set)
            incar_set_static.update(incar_set)
            incar_set_dos.update(incar_set)
            normal_run(path, func, compound, incar_set_relax, (4, 4, 4), f"{cif_folder}/{cif_file}", sel_dyn,
                       runjob_dict)
            os.mkdir(path=f"{path}static/")
            normal_run(f"{path}static/", func, compound, incar_set_static, (8, 8, 8), f"{cif_folder}/{cif_file}",
                       sel_dyn, runjob_dict)
            os.mkdir(path =f"{path}static/dos/")
            normal_run(
                f"{path}static/dos/" , func , compound , incar_set_dos, (12 , 12 , 12) , f"{cif_folder}"
                                                                                             f"/{cif_file}" ,
                sel_dyn , runjob_dict
                )
            
        else:
            incar_set_static.update(incar_set)
            normal_run(path, func, compound, incar_set_static, (4, 2, 4), f"{cif_folder}/{cif_file}", sel_dyn,
                       runjob_dict)

    if type == "relax":
        if runjob_dict["loop"]:
            rj = runjob(name=runjob_dict["name"],
                        comp_name=runjob_dict["comp_name"],
                        nodes=runjob_dict["nodes"],
                        cores=runjob_dict["cores"],
                        hours=runjob_dict["hours"],
                        loop=runjob_dict["loop"],
                        folder=run_folder,
                        static=runjob_dict["static"])
            with open(f"{run_folder}runjob_relax", "w") as text_file:
                text_file.write(rj)

            runjob_dict["name"] = "distortion_static"
            runjob_dict["static"] = "static/ "
            rj = runjob(name=runjob_dict["name"],
                        comp_name=runjob_dict["comp_name"],
                        nodes=runjob_dict["nodes"],
                        cores=runjob_dict["cores"],
                        hours=runjob_dict["hours"],
                        loop=runjob_dict["loop"],
                        folder=run_folder)
            with open(f"{run_folder}runjob_static", "w") as text_file:
                text_file.write(rj)
    else:
        if runjob_dict["loop"]:
            runjob_dict["name"] = runjob_dict["name"] + "_static"
            runjob_dict["static"] = " "
            rj = runjob(name=runjob_dict["name"],
                        comp_name=runjob_dict["comp_name"],
                        nodes=runjob_dict["nodes"],
                        cores=runjob_dict["cores"],
                        hours=runjob_dict["hours"],
                        loop=runjob_dict["loop"],
                        folder=run_folder)
            with open(f"{run_folder}runjob_static", "w") as text_file:
                text_file.write(rj)
