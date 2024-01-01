#!/bin/bash

#SBATCH --job-name=ClimateSA
#SBATCH --output=LogATOS/ClimateSA-%J.out
#SBATCH --error=LogATOS/ClimateSA-%J.out
#SBATCH --cpus-per-task=64
#SBATCH --mem=128G
#SBATCH --time=2-00:00:00
#SBATCH --qos=nf
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=fatima.pillosu@ecmwf.int

# INPUTS
Acc=${1}
SA_2_Compute=${2}
SystemFC=${3}
NumSA=${4}

python3 02_Compute_ClimateSA.py $Acc $SA_2_Compute $SystemFC $NumSA