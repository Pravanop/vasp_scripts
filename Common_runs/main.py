from mainRun import run

runjob_dict = {
    "name": "structure_relax",
    "comp_name": "skx-normal",
    "nodes":2,
    "cores":96,
    "hours":2,
    "loop": False,
    "static": " "
}
run(cif_folder = "/Users/pravanomprakash/Downloads/pbcm_nodope_strained",
    run_folder = "/Users/pravanomprakash/Downloads/pbcm_nodope_strained_run/",
    func = "LDA",
    compound = "hfo2",
    sel_dyn = "",
    runjob_dict = runjob_dict,
    incar_ref = "/Users/pravanomprakash/Documents/vasp_scripts/ref_files/INCAR/",
    incar_set = "",
    type="")
