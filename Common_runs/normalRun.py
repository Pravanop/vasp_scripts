import shutil
from file_utils import file_write
from incar import INCAR
from kpoints import Kpoints
from poscar import POSCAR
from potcar import POTCAR
from runjob import runjob


def normal_run(path, func, compound, incar_settings, kp, cif_file, sel_dyn, runjob_dict):
    potcar = POTCAR(func, compound)
    shutil.copy(potcar, path)

    incar = INCAR(incar_settings)
    file_write(path, 'INCAR', incar)

    kpoints = Kpoints(kp)
    file_write(path, 'KPOINTS', kpoints)
    
    poscar = POSCAR(path, cif_file, sel_dyn)
    # file_write(path, 'POSCAR', poscar)

    if not runjob_dict["loop"]:
        rj = runjob(name=runjob_dict["name"],
                    comp_name=runjob_dict["comp_name"],
                    nodes=runjob_dict["nodes"],
                    cores=runjob_dict["cores"],
                    hours=runjob_dict["hours"],
                    loop=runjob_dict["loop"])
        with open(f"{path}runjob", "w") as text_file:
            text_file.write(rj)