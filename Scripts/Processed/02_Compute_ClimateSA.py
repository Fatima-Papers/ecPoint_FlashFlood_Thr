import os
import sys
from datetime import datetime, timedelta
import numpy as np
import metview as mv

#################################################################################
# CODE DESCRIPTION
# 02_Compute_ClimateSA.py computes modelled rainfall climatology for a specific sub-area.
# Code runtime: the code will take up to 9 hours considering 240 sub-areas.

# DESCRIPTION OF INPUT PARAMETERS
# BaseDateS (date, in the format YYYYMMDD): start date to consider.
# BaseDateF (date, in the format YYYYMMDD): final date to consider.
# Acc (integer, in hours): rainfall accumulation period.
# Perc_list (list of integers): list of percentiles to compute.
# SA_2_Compute (integer): index for the sub-area to consider.
# SystemFC (string): forecasting system to consider.
# NumSA (integer): number of total considered sub-areas.
# Git_repo (string): path of local github repository.
# FileIN_Sample_Grib_Global (string): path of the file containing the global field sample.
# DirIN_RainSA (string): relative path for the input directory containing ERA5.
# DirOUT (string): relative path for the output directory containing the climatology.

# INPUT PARAMETERS
BaseDateS = datetime(2000,1,2,0)
BaseDateF = datetime(2000,1,3,0)
Acc = int(sys.argv[1])
Perc_list = np.append(np.arange(1,100), np.array([99.8, 99.9, 99.95, 99.98, 99.99, 99.995, 99.998]))
SA_2_Compute = int(sys.argv[2])
SystemFC = sys.argv[3]
NumSA = int(sys.argv[4])
GitRepo = "/ec/vol/ecpoint_dev/mofp/Papers_2_Write/RainThr_4FlashFloodFC_ecPointERA5"
FileIN_Sample_Grib_Global = "Data/Raw/Sample_Grib_Global.grib"
DirIN_RainSA = "Data/Compute/01_ExtractSA"
DirOUT = "Data/Compute/02_ClimateSA"
#################################################################################


# NOTES
# The percentiles correspond roughly to the following return periods:
# 99th -> 3 times in a year
# 99.8th -> once in 1 year
# 99.9th -> once in 2 years
# 99.95th -> once in 5 years
# 99.98th -> once in 10 years
# 99.99th -> once in 20 years
# 99.995th -> once in 50 years
# 99.998th -> once in 100 years

# Reading the global field for the sample grib
sample_grib_global = mv.read(GitRepo + "/" + FileIN_Sample_Grib_Global)
NumGP_g = int(mv.count(mv.values(sample_grib_global)))
NumGP_sa = int(NumGP_g / NumSA)

# Initializing the variable that will contain the indipendent rainfall realizations for the full period, for a specific sub-area
if Acc == 24 and SystemFC == "ERA5":
      tp_full_period_sa = np.empty((NumGP_sa))
else:
      tp_full_period_sa = np.empty((NumGP_sa,0))

# Reading the indipendent rainfall realizations for the full period, for a specific sub-area
print("Reading the indipendent rainfall realizations for " + SystemFC + ", for the full climatological period and for the sub-area n." + str(SA_2_Compute) + "/" + str(NumSA))
BaseDate = BaseDateS
while BaseDate <= BaseDateF:

      print(" - Processing the date: ", BaseDate)
      DirIN_temp = GitRepo + "/" + DirIN_RainSA + "_" + f'{Acc:02d}' + "h/" + SystemFC + "/" + BaseDate.strftime("%Y%m%d")
      FileIN_temp = "tp_" + BaseDate.strftime("%Y%m%d") + "_" + f'{SA_2_Compute:03d}' + ".npy"
      tp_SA = np.load(DirIN_temp + "/" + FileIN_temp)

      if Acc == 24 and SystemFC == "ERA5":
            tp_full_period_sa = np.vstack((tp_full_period_sa, tp_SA))
      else:
            tp_full_period_sa = np.hstack((tp_full_period_sa, tp_SA))
      
      BaseDate = BaseDate + timedelta(days=1)

# Eliminating the empty elements when a 1-d array is initiated; 2-d arrays ar intitated for other Acc/SytemFC combination, so this passage is not required
if Acc == 24 and SystemFC == "ERA5":
      tp_full_period_sa = tp_full_period_sa.T
      tp_full_period_sa = tp_full_period_sa[:,1:]

# Computing the rainfall climatology as percentiles
print("Computing the rainfall climatology as percentiles")
percs_sa = np.percentile(tp_full_period_sa, Perc_list, axis=1).T

# Saving the rainfall climatology for the specific sub-area
print("Saving the rainfall climatology")
DirOUT_temp = GitRepo + "/" + DirOUT + "_" + f'{Acc:02d}' + "h/" + SystemFC
if not os.path.exists(DirOUT_temp):
      os.makedirs(DirOUT_temp)
FileOUT_temp = "ClimateSA_" + f'{SA_2_Compute:03d}' + ".npy"
np.save(DirOUT_temp + "/" + FileOUT_temp, percs_sa)