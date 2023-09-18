#!/bin/bash

NumSA_s=0
NumSA_f=19
SystemFC="ERA5_ecPoint"
for SA_2_Compute in $(seq $NumSA_s $NumSA_f); do
      sbatch 02_SubmitterATOS_ClimateSA.sh $SA_2_Compute $SystemFC
done

sleep 9h

echo "Running jobs from 20 to 39"
NumSA_s=20
NumSA_f=39
SystemFC="ERA5_ecPoint"
for SA_2_Compute in $(seq $NumSA_s $NumSA_f); do
      sbatch 02_SubmitterATOS_ClimateSA.sh $SA_2_Compute $SystemFC
done

sleep 9h

echo "Running jobs from 40 to 59"
NumSA_s=40
NumSA_f=59
SystemFC="ERA5_ecPoint"
for SA_2_Compute in $(seq $NumSA_s $NumSA_f); do
      sbatch 02_SubmitterATOS_ClimateSA.sh $SA_2_Compute $SystemFC
done

sleep 9h

NumSA_s=60
NumSA_f=79
SystemFC="ERA5_ecPoint"
for SA_2_Compute in $(seq $NumSA_s $NumSA_f); do
      sbatch 02_SubmitterATOS_ClimateSA.sh $SA_2_Compute $SystemFC
done

sleep 9h

NumSA_s=80
NumSA_f=99
SystemFC="ERA5_ecPoint"
for SA_2_Compute in $(seq $NumSA_s $NumSA_f); do
      sbatch 02_SubmitterATOS_ClimateSA.sh $SA_2_Compute $SystemFC
done

sleep 9h

NumSA_s=100
NumSA_f=119
SystemFC="ERA5_ecPoint"
for SA_2_Compute in $(seq $NumSA_s $NumSA_f); do
      sbatch 02_SubmitterATOS_ClimateSA.sh $SA_2_Compute $SystemFC
done

sleep 9h

NumSA_s=120
NumSA_f=139
SystemFC="ERA5_ecPoint"
for SA_2_Compute in $(seq $NumSA_s $NumSA_f); do
      sbatch 02_SubmitterATOS_ClimateSA.sh $SA_2_Compute $SystemFC
done

sleep 9h

NumSA_s=140
NumSA_f=159
SystemFC="ERA5_ecPoint"
for SA_2_Compute in $(seq $NumSA_s $NumSA_f); do
      sbatch 02_SubmitterATOS_ClimateSA.sh $SA_2_Compute $SystemFC
done

sleep 9h

NumSA_s=160
NumSA_f=179
SystemFC="ERA5_ecPoint"
for SA_2_Compute in $(seq $NumSA_s $NumSA_f); do
      sbatch 02_SubmitterATOS_ClimateSA.sh $SA_2_Compute $SystemFC
done

sleep 9h

NumSA_s=180
NumSA_f=199
SystemFC="ERA5_ecPoint"
for SA_2_Compute in $(seq $NumSA_s $NumSA_f); do
      sbatch 02_SubmitterATOS_ClimateSA.sh $SA_2_Compute $SystemFC
done

sleep 9h

NumSA_s=200
NumSA_f=219
SystemFC="ERA5_ecPoint"
for SA_2_Compute in $(seq $NumSA_s $NumSA_f); do
      sbatch 02_SubmitterATOS_ClimateSA.sh $SA_2_Compute $SystemFC
done

sleep 9h

NumSA_s=220
NumSA_f=239
SystemFC="ERA5_ecPoint"
for SA_2_Compute in $(seq $NumSA_s $NumSA_f); do
      sbatch 02_SubmitterATOS_ClimateSA.sh $SA_2_Compute $SystemFC
done

##################################################################################

# NumSA_s=0
# NumSA_f=19
# SystemFC="ERA5"
# for SA_2_Compute in $(seq $NumSA_s $NumSA_f); do
#       sbatch 02_SubmitterATOS_ClimateSA.sh $SA_2_Compute $SystemFC
# done

# NumSA_s=20
# NumSA_f=39
# SystemFC="ERA5"
# for SA_2_Compute in $(seq $NumSA_s $NumSA_f); do
#       sbatch 02_SubmitterATOS_ClimateSA.sh $SA_2_Compute $SystemFC
# done

# NumSA_s=40
# NumSA_f=59
# SystemFC="ERA5"
# for SA_2_Compute in $(seq $NumSA_s $NumSA_f); do
#       sbatch 02_SubmitterATOS_ClimateSA.sh $SA_2_Compute $SystemFC
# done

# NumSA_s=60
# NumSA_f=79
# SystemFC="ERA5"
# for SA_2_Compute in $(seq $NumSA_s $NumSA_f); do
#       sbatch 02_SubmitterATOS_ClimateSA.sh $SA_2_Compute $SystemFC
# done

# NumSA_s=80
# NumSA_f=99
# SystemFC="ERA5"
# for SA_2_Compute in $(seq $NumSA_s $NumSA_f); do
#       sbatch 02_SubmitterATOS_ClimateSA.sh $SA_2_Compute $SystemFC
# done

# NumSA_s=100
# NumSA_f=119
# SystemFC="ERA5"
# for SA_2_Compute in $(seq $NumSA_s $NumSA_f); do
#       sbatch 02_SubmitterATOS_ClimateSA.sh $SA_2_Compute $SystemFC
# done

# NumSA_s=120
# NumSA_f=139
# SystemFC="ERA5"
# for SA_2_Compute in $(seq $NumSA_s $NumSA_f); do
#       sbatch 02_SubmitterATOS_ClimateSA.sh $SA_2_Compute $SystemFC
# done

# NumSA_s=140
# NumSA_f=159
# SystemFC="ERA5"
# for SA_2_Compute in $(seq $NumSA_s $NumSA_f); do
#       sbatch 02_SubmitterATOS_ClimateSA.sh $SA_2_Compute $SystemFC
# done