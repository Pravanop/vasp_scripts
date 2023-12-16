from Common_runs.vasprun_old.file_utils import file_open, file_write
import os


def INCAR(incar_settings, path:str = ""):
    
    if path != "":
        incar_file = file_open(f"{path}/INCAR")
    
        for idx, line in enumerate(incar_file):
            if "LCHARG" in line:
                incar_file[idx] = "LCHARG = .FALSE."
            if "NELECT" in line:
                incar_file.pop(idx)
        for key, value in incar_settings.items():
            line = f"{key} = {value}"
            incar_file.append(line)
            
        file_write(path , '/INCAR' , incar_file)
    else:
        incar_file = []
        for key, value in incar_settings.items():
            line = f"{key} = {value}"
            incar_file.append(line)
    return incar_file


if __name__ == "__main__":
    
    for doping in [1, 2, 3, 4]:
        folder_path = f"/Users/pravanomprakash/Documents/Projects/BFO/BFO_run/Pnma_{doping}"
        lfolder = sorted(os.listdir(folder_path))
    
        if '.DS_Store' in lfolder:
            lfolder.remove('.DS_Store')
    
        elect = 228 - doping*0.4  # 342
        print(elect)
        INCAR(incar_settings={'NELECT': elect}, path=f"{folder_path}/")
        INCAR(incar_settings={'NELECT': elect}, path=f"{folder_path}/static")
