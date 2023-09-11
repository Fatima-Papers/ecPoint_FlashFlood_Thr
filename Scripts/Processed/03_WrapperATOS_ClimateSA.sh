#!/bin/bash

NumSA_s=0
NumSA_f=19
SystemFC="ERA5_ecPoint"
for SA_2_Compute in $(seq $NumSA_s $NumSA_f); do
      sbatch 03_SubmitterATOS_ClimateSA.sh $SA_2_Compute $SystemFC
done

# NumSA_s=20
# NumSA_f=39
# SystemFC="ERA5_ecPoint"
# for SA_2_Compute in $(seq $NumSA_s $NumSA_f); do
#       sbatch 03_SubmitterATOS_ClimateSA.sh $SA_2_Compute $SystemFC
# done

# NumSA_s=40
# NumSA_f=59
# SystemFC="ERA5_ecPoint"
# for SA_2_Compute in $(seq $NumSA_s $NumSA_f); do
#       sbatch 03_SubmitterATOS_ClimateSA.sh $SA_2_Compute $SystemFC
# done

# NumSA_s=60
# NumSA_f=79
# SystemFC="ERA5_ecPoint"
# for SA_2_Compute in $(seq $NumSA_s $NumSA_f); do
#       sbatch 03_SubmitterATOS_ClimateSA.sh $SA_2_Compute $SystemFC
# done

# NumSA_s=80
# NumSA_f=99
# SystemFC="ERA5_ecPoint"
# for SA_2_Compute in $(seq $NumSA_s $NumSA_f); do
#       sbatch 03_SubmitterATOS_ClimateSA.sh $SA_2_Compute $SystemFC
# done

# NumSA_s=100
# NumSA_f=119
# SystemFC="ERA5_ecPoint"
# for SA_2_Compute in $(seq $NumSA_s $NumSA_f); do
#       sbatch 03_SubmitterATOS_ClimateSA.sh $SA_2_Compute $SystemFC
# done

# NumSA_s=120
# NumSA_f=139
# SystemFC="ERA5_ecPoint"
# for SA_2_Compute in $(seq $NumSA_s $NumSA_f); do
#       sbatch 03_SubmitterATOS_ClimateSA.sh $SA_2_Compute $SystemFC
# done

# NumSA_s=140
# NumSA_f=160
# SystemFC="ERA5_ecPoint"
# for SA_2_Compute in $(seq $NumSA_s $NumSA_f); do
#       sbatch 03_SubmitterATOS_ClimateSA.sh $SA_2_Compute $SystemFC
# done

# NumSA_s=0
# NumSA_f=19
# SystemFC="ERA5"
# for SA_2_Compute in $(seq $NumSA_s $NumSA_f); do
#       sbatch 03_SubmitterATOS_ClimateSA.sh $SA_2_Compute $SystemFC
# done

# NumSA_s=20
# NumSA_f=39
# SystemFC="ERA5"
# for SA_2_Compute in $(seq $NumSA_s $NumSA_f); do
#       sbatch 03_SubmitterATOS_ClimateSA.sh $SA_2_Compute $SystemFC
# done

# NumSA_s=40
# NumSA_f=59
# SystemFC="ERA5"
# for SA_2_Compute in $(seq $NumSA_s $NumSA_f); do
#       sbatch 03_SubmitterATOS_ClimateSA.sh $SA_2_Compute $SystemFC
# done

# NumSA_s=60
# NumSA_f=79
# SystemFC="ERA5"
# for SA_2_Compute in $(seq $NumSA_s $NumSA_f); do
#       sbatch 03_SubmitterATOS_ClimateSA.sh $SA_2_Compute $SystemFC
# done

# NumSA_s=80
# NumSA_f=99
# SystemFC="ERA5"
# for SA_2_Compute in $(seq $NumSA_s $NumSA_f); do
#       sbatch 03_SubmitterATOS_ClimateSA.sh $SA_2_Compute $SystemFC
# done

# NumSA_s=100
# NumSA_f=119
# SystemFC="ERA5"
# for SA_2_Compute in $(seq $NumSA_s $NumSA_f); do
#       sbatch 03_SubmitterATOS_ClimateSA.sh $SA_2_Compute $SystemFC
# done

# NumSA_s=120
# NumSA_f=139
# SystemFC="ERA5"
# for SA_2_Compute in $(seq $NumSA_s $NumSA_f); do
#       sbatch 03_SubmitterATOS_ClimateSA.sh $SA_2_Compute $SystemFC
# done

# NumSA_s=140
# NumSA_f=160
# SystemFC="ERA5"
# for SA_2_Compute in $(seq $NumSA_s $NumSA_f); do
#       sbatch 03_SubmitterATOS_ClimateSA.sh $SA_2_Compute $SystemFC
# done