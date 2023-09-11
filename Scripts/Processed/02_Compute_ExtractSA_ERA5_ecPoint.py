import os
from datetime import datetime, timedelta
import numpy as np
import metview as mv

####################################################################
# CODE DESCRIPTION
# 02_Compute_ExtractSA_ERA5_ecPoint.py extracts accumulated rainfall totals 
# from ERA5_ecPoint for a specific number of sub-areas.
# Code runtime: the code will take up to 48 hours to run un serial.

# DESCRIPTION OF INPUT PARAMETERS
# BaseDateS (date, in the format YYYYMMDD): start date to consider.
# BaseDateF (date, in the format YYYYMMDD): final date to consider.
# Acc (integer, in hours): rainfall accumulation period.
# NumSA (integer): number of sub-areas to consider.
# Git_repo (string): path of local github repository.
# DirIN (string): relative path for the input directory containing ERA5.
# DirOUT (string): relative path for the output directory containing the climatology.

# INPUT PARAMETERS
BaseDateS = datetime(1980,1,1,0)
BaseDateF = datetime(2020,12,31,0)
Acc = 12
NumSA = 160
GitRepo = "/ec/vol/ecpoint_dev/mofp/Papers_2_Write/ecPoint_FlashFlood_Thr"
DirIN = "Data/Raw/Reanalysis/ERA5_ecPoint"
DirOUT = "Data/Compute/Reanalysis_SA/ERA5_ecPoint"
####################################################################


# CUSTOM FUNCTIONS

###################################
# Rainfall realizations from ERA5_ecPoint #
###################################

# Note: the rainfall values are already in mm
def tp_ERA5_ecPoint_12h(BaseDateTime, DirIN):

      # Initializing the variable that stores the accumulated rainfall for the accumulation periods 00-12 UTC and 12-00 UTC
      tp_12 = 0
      tp_00 = 0

      # Extracting the accumulated rainfall values for the accumulation period 00-12 UTC
      DirIN_12 = DirIN + "/Pt_BC_PERC/" + BaseDateTime.strftime("%Y%m")
      FileIN_12 =  "Pt_BC_PERC_" + BaseDateTime.strftime("%Y%m%d") + "_12.grib2"
      if os.path.exists(DirIN_12 + "/" + FileIN_12):
            tp_12 = mv.read(DirIN_12 + "/" + FileIN_12)
      
      # Extracting the accumulated rainfall values for the accumulation period 12-00 UTC
      DirIN_00 = DirIN + "/Pt_BC_PERC/" + BaseDateTime.strftime("%Y%m")
      FileIN_00 =  "Pt_BC_PERC_" + BaseDateTime.strftime("%Y%m%d") + "_24.grib2"
      if os.path.exists(DirIN_00 + "/" + FileIN_00):
            tp_00 = mv.read(DirIN_00 + "/" + FileIN_00)

      # Converting the accumulated rainfall totals from m to mm, and creating the variable that stores the independent rainfall realizations
      if tp_12 != 0 and tp_00 != 0: 
            tp_12 = tp_12 * 1000
            tp_00 = tp_00 * 1000               
            tp = mv.merge(tp_12, tp_00)
      else:
            tp = 0

      # Convert the fieldset into a 16-byte float numpy array (to reduce memory consumption)
      tp = mv.values(tp).T.astype(np.float16)
      
      return tp

###############################################################################################################


# Setting input/output directories
DirIN_temp = GitRepo + "/" + DirIN + "_" + f'{Acc:02d}' + "h"

# Computing accumulated rainfall totals from ERA5
print("Extracting accumulated rainfall totals from ERA5")
BaseDate = BaseDateS

while BaseDate <= BaseDateF:
      
      print(" - Processing the date: ", BaseDate)
      tp_temp = tp_ERA5_ecPoint_12h(BaseDate, DirIN_temp)
      NumGP_Global = tp_temp.shape[0]

      # Extracting the sub-areas
      if NumGP_Global != 0:
            
            i = int(0)
            j = int(NumGP_Global/NumSA)
            for ind_SA in range(NumSA):
                  
                  tp_sa_temp = tp_temp[i:j,:]

                  # Saving the extracted sub-areas
                  DirOUT_temp = GitRepo + "/" + DirOUT + "_" + f'{Acc:02d}' + "h/" + BaseDate.strftime("%Y%m%d")
                  if not os.path.exists(DirOUT_temp):
                        os.makedirs(DirOUT_temp)
                  FileOUT_temp = "tp_" + BaseDate.strftime("%Y%m%d") + "_" + f'{ind_SA:03d}' + ".npy"
                  np.save(DirOUT_temp + "/" + FileOUT_temp, tp_sa_temp) 

                  i = int(j)
                  j = int(j + (NumGP_Global/NumSA))
           
      BaseDate = BaseDate + timedelta(days=1)