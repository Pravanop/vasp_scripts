from mainRun import run
import numpy as np

path = "/Users/pravanomprakash/Downloads/zro_domain_hh"

runjob_dict = {
    "name": "structure_relax",
    "comp_name": "compute",
    "nodes":2,
    "cores":128,
    "hours":6,
    "loop": False,
    "static": " "
}


run(cif_folder = f"{path}/",
    run_folder = f"{path}_run/",
    func = "LDA",
    compound = "zro2",
    sel_dyn = "",
    runjob_dict = runjob_dict,
    incar_ref = "../ref_files/INCAR/",
    incar_set = "",
    type="relax")
