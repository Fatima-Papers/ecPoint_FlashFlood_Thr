#!/bin/bash

#SBATCH --job-name=Climate_ERA5
#SBATCH --output=LogATOS/Climate_ERA5-%J.out
#SBATCH --error=LogATOS/Climate_ERA5-%J.out
#SBATCH --cpus-per-task=1
#SBATCH --mem=64G
#SBATCH --time=2-00:00:00
#SBATCH --qos=nf
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=fatima.pillosu@ecmwf.int

python3 01_Compute_Climate_ERA5.py