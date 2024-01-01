#!/bin/bash

Acc=24
SystemFC="ERA5_ecPoint"
NumSA=220

NumSA_s=0
NumSA_f=29
echo "Computing climatology from $SystemFC for sub-areas from n. $NumSA_s to n. $NumSA_f"
for SA_2_Compute in $(seq $NumSA_s $NumSA_f); do
      sbatch 02_SubmitterATOS_ClimateSA.sh $Acc $SA_2_Compute $SystemFC $NumSA
done

sleep 9h

NumSA_s=30
NumSA_f=59
echo "Computing climatology from $SystemFC for sub-areas from n. $NumSA_s to n. $NumSA_f"
for SA_2_Compute in $(seq $NumSA_s $NumSA_f); do
      sbatch 02_SubmitterATOS_ClimateSA.sh $Acc $SA_2_Compute $SystemFC $NumSA
done

sleep 9h

NumSA_s=60
NumSA_f=89
echo "Computing climatology from $SystemFC for sub-areas from n. $NumSA_s to n. $NumSA_f"
for SA_2_Compute in $(seq $NumSA_s $NumSA_f); do
      sbatch 02_SubmitterATOS_ClimateSA.sh $Acc $SA_2_Compute $SystemFC $NumSA
done

sleep 9h

NumSA_s=90
NumSA_f=119
echo "Computing climatology from $SystemFC for sub-areas from n. $NumSA_s to n. $NumSA_f"
for SA_2_Compute in $(seq $NumSA_s $NumSA_f); do
      sbatch 02_SubmitterATOS_ClimateSA.sh $Acc $SA_2_Compute $SystemFC $NumSA
done

sleep 9h

NumSA_s=120
NumSA_f=149
echo "Computing climatology from $SystemFC for sub-areas from n. $NumSA_s to n. $NumSA_f"
for SA_2_Compute in $(seq $NumSA_s $NumSA_f); do
      sbatch 02_SubmitterATOS_ClimateSA.sh $Acc $SA_2_Compute $SystemFC $NumSA
done

sleep 9h

NumSA_s=150
NumSA_f=179
echo "Computing climatology from $SystemFC for sub-areas from n. $NumSA_s to n. $NumSA_f"
for SA_2_Compute in $(seq $NumSA_s $NumSA_f); do
      sbatch 02_SubmitterATOS_ClimateSA.sh $Acc $SA_2_Compute $SystemFC $NumSA
done

sleep 9h

NumSA_s=180
NumSA_f=209
echo "Computing climatology from $SystemFC for sub-areas from n. $NumSA_s to n. $NumSA_f"
for SA_2_Compute in $(seq $NumSA_s $NumSA_f); do
      sbatch 02_SubmitterATOS_ClimateSA.sh $Acc $SA_2_Compute $SystemFC $NumSA
done

sleep 9h

NumSA_s=210
NumSA_f=219
echo "Computing climatology from $SystemFC for sub-areas from n. $NumSA_s to n. $NumSA_f"
for SA_2_Compute in $(seq $NumSA_s $NumSA_f); do
      sbatch 02_SubmitterATOS_ClimateSA.sh $Acc $SA_2_Compute $SystemFC $NumSA
done

sleep 9h

##################################################################################

# Acc=24
# SystemFC="ERA5"
# NumSA=160

# NumSA_s=0
# NumSA_f=29
# echo "Computing climatology from $SystemFC for sub-areas from n. $NumSA_s to n. $NumSA_f"
# for SA_2_Compute in $(seq $NumSA_s $NumSA_f); do
#       sbatch 02_SubmitterATOS_ClimateSA.sh $Acc $SA_2_Compute $SystemFC $NumSA
# done

# sleep 15m

# NumSA_s=30
# NumSA_f=59
# echo "Computing climatology from $SystemFC for sub-areas from n. $NumSA_s to n. $NumSA_f"
# for SA_2_Compute in $(seq $NumSA_s $NumSA_f); do
#       sbatch 02_SubmitterATOS_ClimateSA.sh $Acc $SA_2_Compute $SystemFC $NumSA
# done

# sleep 15m

# NumSA_s=60
# NumSA_f=89
# echo "Computing climatology from $SystemFC for sub-areas from n. $NumSA_s to n. $NumSA_f"
# for SA_2_Compute in $(seq $NumSA_s $NumSA_f); do
#       sbatch 02_SubmitterATOS_ClimateSA.sh $Acc $SA_2_Compute $SystemFC $NumSA
# done

# sleep 15m

# NumSA_s=90
# NumSA_f=119
# echo "Computing climatology from $SystemFC for sub-areas from n. $NumSA_s to n. $NumSA_f"
# for SA_2_Compute in $(seq $NumSA_s $NumSA_f); do
#       sbatch 02_SubmitterATOS_ClimateSA.sh $Acc $SA_2_Compute $SystemFC $NumSA
# done

# sleep 15m

# NumSA_s=120
# NumSA_f=149
# echo "Computing climatology from $SystemFC for sub-areas from n. $NumSA_s to n. $NumSA_f"
# for SA_2_Compute in $(seq $NumSA_s $NumSA_f); do
#       sbatch 02_SubmitterATOS_ClimateSA.sh $Acc $SA_2_Compute $SystemFC $NumSA
# done

# sleep 15m

# NumSA_s=150
# NumSA_f=159
# echo "Computing climatology from $SystemFC for sub-areas from n. $NumSA_s to n. $NumSA_f"
# for SA_2_Compute in $(seq $NumSA_s $NumSA_f); do
#       sbatch 02_SubmitterATOS_ClimateSA.sh $Acc $SA_2_Compute $SystemFC $NumSA
# done