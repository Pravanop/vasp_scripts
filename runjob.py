import os


def runjob(name: str,
           comp_name: str,
           nodes: int,
           cores: int,
           hours: int,
           loop: bool,
           **kwargs):

    basic_commands = f"#!/bin/bash\n#SBATCH -J {name}          # Job name\n#SBATCH -o status.o%j        # Name of " \
                     f"stdout output file(%j expands to jobId)\n#SBATCH -e status.e%j        # Name of stderr output " \
                     f"file(%j expands to jobId)\n#SBATCH -p {comp_name}        # Submit to the 'normal' or " \
                     f"'development' queue\n#SBATCH -N {nodes}                  # Total number of nodes requested (16 " \
                     f"cores/node)\n#SBATCH -n {cores}                 # Total number of mpi tasks requested\n#SBATCH " \
                     f"-t 0{hours}:00:00           # Run time (hh:mm:ss) - 24 hours\n#SBATCH -A TG-DMR160007\n"
    run_commands = f"#export OMP_NUM_THREADS=1\nexport FORT_BUFFERED=TRUE\nmodule load intel/18.0.2\n# module load " \
                   f"vasp/5.4.4\n# module load remora\n# remora ibrun $VASP2D >> stdout\n# remora ibrun $VASPZ >> " \
                   f"stdout\n"

    if loop:
        rang = ''
        for i in sorted(os.listdir(kwargs["folder"])):
            rang += f'{str(i)}/{kwargs["static"]}'

        for_commands = f"for i in {rang} do \n  cd ./$i/{kwargs['static']} \n    ibrun $VASP >> stdout\n    cd ..     "

        runjob = basic_commands + run_commands + for_commands

    else:
        for_commands = f"ibrun $VASP >> stdout\n"
        runjob = basic_commands + run_commands + for_commands

    return runjob