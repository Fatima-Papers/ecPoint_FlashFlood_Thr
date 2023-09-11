#!/bin/bash

#SBATCH --job-name=ClimateSA
#SBATCH --output=LogATOS/ClimateSA-%J.out
#SBATCH --error=LogATOS/ClimateSA-%J.out
#SBATCH --cpus-per-task=1
#SBATCH --mem=64G
#SBATCH --time=2-00:00:00
#SBATCH --qos=nf
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=fatima.pillosu@ecmwf.int

# INPUTS
SA_2_Compute=${1}
SystemFC=${2}

python3 03_Compute_ClimateSA.py $SA_2_Compute $SystemFC