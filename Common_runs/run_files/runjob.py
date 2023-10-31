import os


def runjob(name: str,
           comp_name: str,
           nodes: str,
           cores: int,
           hours: int,
           loop: bool,
           **kwargs):

    basic_commands = f"#!/bin/bash\n#SBATCH --job-name={name}\n#SBATCH --partition=\"{comp_name}\"\n#SBATCH --time 0" \
                     f"{hours}:00:00\n#SBATCH --output=vasp.out\n#SBATCH --nodes={nodes}\n#SBATCH --ntasks-per-node=" \
                     f"{cores}\n#SBATCH --account=tg-dmr160007"
    run_commands = f"\nmodule purge\nmodule load cpu/0.15.4\nmodule load  intel/19.1.1.217\nmodule load slurm\nmodule " \
                   f"load intel-mkl/2019.1.144\nmodule load intel-mpi/2019.8.254\n"

    if loop:
        rang = ''
        for i in sorted(os.listdir(kwargs["folder"])):
            rang += f'{str(i)}/{kwargs["static"]}'

        for_commands = f"for i in {rang} do \n  cd ./$i/{kwargs['static']} \n    ibrun $VASP >> stdout\n    cd ..     "

        runjob = basic_commands + run_commands + for_commands

    else:
        for_commands = f"mpirun $VASP > stdout\n"
        runjob = basic_commands + run_commands + for_commands

    return runjob