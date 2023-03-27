from pymatgen.core import Structure
from file_utils import file_open, file_write

def POSCAR(path , cif_file, sel_dyn):
    s = Structure.from_file(cif_file)
    poscar_file = s.to(f'{path}/POSCAR')
    
    if sel_dyn !="":
        poscar_file = file_open(f'{path}/POSCAR')
        for idx, line in enumerate(poscar_file):
    
            if idx <= 7:
                continue
    
            poscar_file[idx] = line + ' ' + sel_dyn
        file_write(path = path ,filename = 'POSCAR', file_list = poscar_file)
    
    return 0