from file_utils import file_open, file_write
import os


def INCAR(incar_settings, path:str = ""):
    
    if path != "":
        incar_file = file_open(f"{path}/INCAR")
    
        for idx, line in enumerate(incar_file):
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


# if __name__ == "__main__":
#     vol = [125.64,
#            125.85,
#            126.05,
#            126.25,
#            126.45,
#            126.65,
#            126.85,
#            127.05,
#            127.25,
#            127.45]
#     folder_path = "/Users/pravanomprakash/Library/CloudStorage/Box-Box/Research_Rotation/HfZrO/hafnia/pathways" \
#                   "/p42nmc_pca21/hole doping/23/p42nmc_pca21rev_run"
#     lfolder = sorted(os.listdir(folder_path))
#
#     if '.DS_Store' in lfolder:
#         lfolder.remove('.DS_Store')
#
#     for idx, i in enumerate(lfolder):
#         elect = 88 - 2 * vol[idx] / 100
#         print(elect)
#         INCAR(incar_settings={'NELECT': elect}, path=f"{folder_path}/{i}")
