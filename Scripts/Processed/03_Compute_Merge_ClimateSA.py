import os
from datetime import datetime, timedelta
import numpy as np
import metview as mv

#####################################################################
# CODE DESCRIPTION
# 03_Compute_Merge_ClimateSA.py computes modelled rainfall climatology from ERA5.
# The script is very memory demanding, so the raw ERA5 values are converted to 
# 16-bytes floats.
# Code runtime: the code will take up to x hours.

# DESCRIPTION OF INPUT PARAMETERS
# BaseDateS (date, in the format YYYYMMDD): start date to consider.
# BaseDateF (date, in the format YYYYMMDD): final date to consider.
# Acc (integer, in hours): rainfall accumulation period.
# Perc_list (list of integers): list of percentiles to compute
# Git_repo (string): path of local github repository.
# DirIN (string): relative path for the input directory containing ERA5.
# DirOUT (string): relative path for the output directory containing the climatology.

# INPUT PARAMETERS
BaseDateS = datetime(1980,1,1,0)
BaseDateF = datetime(2020,12,31,0)
Acc = 12
NumSA = 160
SystemFC = "ERA5_ecPoint"
Perc_list = np.append(np.arange(1,100), np.array([99.4, 99.5,99.8,99.95]))
GitRepo = "/ec/vol/ecpoint_dev/mofp/Papers_2_Write/ecPoint_FlashFlood_Thr"
FileIN_Sample_Grib_Global = "Data/Raw/Sample_Grib_Global.grib"
DirIN_RainSA = "Data/Compute/Reanalysis_SA"
DirOUT = "Data/Compute/Climate"
#####################################################################


# Reading the global field for the sample grib
sample_grib_global = mv.read(GitRepo + "/" + FileIN_Sample_Grib_Global)
NumGP = int(mv.count(mv.values(sample_grib_global)))
NumSA = int(NumGP / NumSA)


for ind_SA in range(NumSA):
      
      tp_full_period_sa = np.empty((NumSA,0))
      
      
      # Reading the sub-areas containing the raw rainfall realizations 
      BaseDate = BaseDateS
      
      while BaseDate <= BaseDateF:
      
            print(" - Processing the date: ", BaseDate)
            DirIN_temp = GitRepo + "/" + DirIN_RainSA + "/" + SystemFC + "_" + f'{Acc:02d}' + "h" + "/" + BaseDate.strftime("%Y%m%d")
            FileIN_temp = "tp_" + BaseDate.strftime("%Y%m%d") + "_" + f'{ind_SA:03d}' + ".npy"
            tp_SA = np.load(DirIN_temp + "/" + FileIN_temp)
            tp_full_period_sa = np.hstack((tp_full_period_sa, tp_SA))     

            BaseDate = BaseDate + timedelta(days=1)

      percs_sa = np.percentile(tp_full_period_sa, Perc_list, axis=1).T
      



      
exit()



#  Storing the percentiles as grib while restoring the global field
percs_tot_global = None
for ind_perc in range(npercs):
      temp_perc_sa = percs_sa[:,ind_perc]
      percs_sample_global_array[ind_sa] = temp_perc_sa
      percs_tot_global = mv.merge(percs_tot_global, mv.set_values(percs_sample_global_grib[0], percs_sample_global_array))

# Saving the output file
print("Storing the output file")
DirOUT_temp = GitRepo + "/" + DirOUT + "/" + SystemFC + "_" + f'{Acc:02d}' + "h"
if not os.path.exists(DirOUT_temp):
      os.makedirs(DirOUT_temp)
FileOUT = DirOUT_temp + "/Climate_ERA5_Italy_" + f'{Acc:02d}' + "h.grib"
mv.write(FileOUT, percs_tot_global)