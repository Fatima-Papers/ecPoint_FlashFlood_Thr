import os
from datetime import datetime, timedelta
import numpy as np
import metview as mv

####################################################################
# CODE DESCRIPTION
# 01_Compute_ExtractSA_ERA5.py extracts accumulated rainfall totals from ERA5 
# for a specific number of sub-areas.
# Code runtime: the code will take up to 48 hours to run in serial.

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
DirIN = "Data/Raw/Reanalysis/ERA5"
DirOUT = "Data/Compute/Reanalysis_SA/ERA5"
####################################################################


# CUSTOM FUNCTIONS

############################
# Rainfall realizations from ERA5 #
############################

def tp_ERA5_12h(BaseDateTime, DirIN):
      
      # Initializing the variable that stores the accumulated rainfall for the accumulation periods 00-12 UTC and 12-00 UTC
      tp_12 = 0
      tp_00 = 0

      # Extracting the accumulated rainfall values for the accumulation period 00-12 UTC
      BaseDateTime_1 = BaseDateTime - timedelta(days=1) + timedelta(hours=18)
      BaseDateTime_0 = BaseDateTime + timedelta(hours=6)
      for Step in range(7,(12+1)):
            DirIN_1 = DirIN + "/" + BaseDateTime_1.strftime("%Y") + "/" + BaseDateTime_1.strftime("%Y%m%d%H")
            FileIN_1 =  "tp_" + BaseDateTime_1.strftime("%Y%m%d") + "_" + BaseDateTime_1.strftime("%H") + "_" + f'{Step:03d}' + ".grib"
            if os.path.exists(DirIN_1 + "/" + FileIN_1):
                  tp_12 = tp_12 + mv.read(DirIN_1 + "/" + FileIN_1)
      for Step in range(1,(6+1)):  
            DirIN_0 = DirIN + "/" + BaseDateTime_0.strftime("%Y") + "/" + BaseDateTime_0.strftime("%Y%m%d%H")
            FileIN_0 =  "tp_" + BaseDateTime_0.strftime("%Y%m%d") + "_" + BaseDateTime_0.strftime("%H") + "_" + f'{Step:03d}' + ".grib"
            if os.path.exists(DirIN_0 + "/" + FileIN_0):
                  tp_12 = tp_12 + mv.read(DirIN_0 + "/" + FileIN_0)

      # Extracting the accumulated rainfall values for the accumulation period 12-00 UTC
      BaseDateTime_0 = BaseDateTime + timedelta(hours=6)
      BaseDateTime_1 = BaseDateTime + timedelta(hours=18)
      for Step in range(7,(12+1)):
            DirIN_0 = DirIN + "/" + BaseDateTime_0.strftime("%Y") + "/" + BaseDateTime_0.strftime("%Y%m%d%H")
            FileIN_0 =  "tp_" + BaseDateTime_0.strftime("%Y%m%d") + "_" + BaseDateTime_0.strftime("%H") + "_" + f'{Step:03d}' + ".grib"
            if os.path.exists(DirIN_0 + "/" + FileIN_0):
                  tp_00 = tp_00 + mv.read(DirIN_0 + "/" + FileIN_0)
      for Step in range(1,(6+1)):
            DirIN_1 = DirIN + "/" + BaseDateTime_1.strftime("%Y") + "/" + BaseDateTime_1.strftime("%Y%m%d%H")
            FileIN_1 =  "tp_" + BaseDateTime_1.strftime("%Y%m%d") + "_" + BaseDateTime_1.strftime("%H") + "_" + f'{Step:03d}' + ".grib"
            if os.path.exists(DirIN_1 + "/" + FileIN_1):
                  tp_00 = tp_00 + mv.read(DirIN_1 + "/" + FileIN_1)

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
DirIN_temp = GitRepo + "/" + DirIN

# Computing accumulated rainfall totals from ERA5
print("Extracting accumulated rainfall totals from ERA5")
BaseDate = BaseDateS

while BaseDate <= BaseDateF:
      
      print(" - Processing the date: ", BaseDate)
      tp_temp = tp_ERA5_12h(BaseDate, DirIN_temp)
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