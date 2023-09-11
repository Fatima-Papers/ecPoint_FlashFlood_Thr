import os
import numpy as np
import metview as mv

###################################################################
# CODE DESCRIPTION
# 03_Compute_Climate_Global.py merges the climatologies for each sub-area, 
# and creates a global field.
# Code runtime: the code will take up to x hours.

# DESCRIPTION OF INPUT PARAMETERS
# Acc (integer, in hours): rainfall accumulation period.
# NumSA (integer): number of total considered sub-areas.
# SystemFC (string): forecasting system to consider.
# Git_repo (string): path of local github repository.
# DirIN (string): relative path for the input directory containing ERA5.
# DirOUT (string): relative path for the output directory containing the climatology.

# INPUT PARAMETERS
Acc = 12
NumSA = 160
SystemFC = "ERA5_ecPoint"
GitRepo = "/ec/vol/ecpoint_dev/mofp/Papers_2_Write/ecPoint_FlashFlood_Thr"
FileIN_Sample_Grib_Global = "Data/Raw/Sample_Grib_Global.grib"
DirIN = "Data/Compute/ClimateSA"
DirOUT = "Data/Compute/Climate_Global"
###################################################################


# Reading the global field for the sample grib
sample_grib_global = mv.read(GitRepo + "/" + FileIN_Sample_Grib_Global)
NumGP_g = int(mv.count(mv.values(sample_grib_global)))
NumGP_sa = int(NumGP_g / NumSA)

# Merging the climatologies for all the sub-areas to create global fields
print("Merging the climatologies for all the sub-areas to create global fields")
for ind_SA in range(NumSA):
      
      print(" - Reading the sub-area n." + str(ind_SA) + "/" + str(NumSA))
      DirIN_temp = GitRepo + "/" + DirIN + "/" + SystemFC + "_" + f'{Acc:02d}' + "h"
      FileIN_temp = "ClimateSA_" + f'{ind_SA:03d}' + ".npy"
      tp_SA = np.load(DirIN_temp + "/" + FileIN_temp)
      tp_full_period_sa = np.vstack((tp_full_period_sa, tp_SA))     
npercs = tp_full_period_sa.shape[1]

#  Storing the percentiles as grib
percs_tot_global = None
for ind_perc in range(npercs):
      percs_tot_global = mv.merge(percs_tot_global, mv.set_values(sample_grib_global, tp_full_period_sa[:,ind_perc]))

# Saving the output file
print("Storing the output file")
DirOUT_temp = GitRepo + "/" + DirOUT + "/" + SystemFC + "_" + f'{Acc:02d}' + "h"
if not os.path.exists(DirOUT_temp):
      os.makedirs(DirOUT_temp)
FileOUT = DirOUT_temp + "/Climate_" + SystemFC + "_" + f'{Acc:02d}' + "h.grib"
mv.write(FileOUT, percs_tot_global)