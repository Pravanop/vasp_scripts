from file_utils import file_open
import re


def Kpoints(kpoints):
    kpoints_re = r'\d+  \d+  \d+'
    if isinstance(kpoints, tuple):
        sub = f'{kpoints[0]} {kpoints[1]} {kpoints[2]}'
    ref_file = file_open(path= '/ref_files/KPOINTS')
    for idx, line in enumerate(ref_file):
        if 'Gamma' in line:
            val = idx + 1
            break
    line = ref_file[val]
    ref_file[val] = re.sub(kpoints_re, sub, line)
    return ref_file