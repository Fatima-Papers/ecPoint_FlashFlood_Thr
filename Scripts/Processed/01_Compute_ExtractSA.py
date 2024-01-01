import os
from datetime import datetime, timedelta
import numpy as np
import metview as mv

#############################################################################
# CODE DESCRIPTION
# 01_Compute_ExtractSA.py extracts indipendent accumulated rainfall realizations for a 
# specific number of sub-areas. Current valid accumulations are 12-hourly, and current valid 
# forecasting systems are ERA5 and ERA5_ecPoint.
# Code runtime: the code will take up to 48 hours to run in serial.

# DESCRIPTION OF INPUT PARAMETERS
# BaseDateS (date, in the format YYYYMMDD): start date to consider.
# BaseDateF (date, in the format YYYYMMDD): final date to consider.
# Acc (integer, in hours): rainfall accumulation period.
# NumSA (integer): number of sub-areas to consider.
# SystemFC (string): forecasting system to consider.
# Git_repo (string): path of local github repository.
# DirIN (string): relative path for the input directory containing ERA5.
# DirOUT (string): relative path for the output directory containing the climatology.

# INPUT PARAMETERS
BaseDateS = datetime(2000,1,2,0)
BaseDateF = datetime(2020,12,31,0)
Acc = 24
NumSA = 220
SystemFC = "ERA5"
GitRepo = "/ec/vol/ecpoint_dev/mofp/Papers_2_Write/RainThr_4FlashFloodFC_ecPointERA5"
DirIN = "Data/Raw/Reanalysis"
DirOUT = "Data/Compute/01_ExtractSA"
#############################################################################


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


def tp_ERA5_24h(BaseDateTime, DirIN):

      # Computing the accumulated rainfall totals
      BaseDateTime_0 = BaseDateTime + timedelta(hours=6)
      BaseDateTime_1 = BaseDateTime - timedelta(days=1) + timedelta(hours=18)
      count_steps = 0 # to make sure that both required dates are available in  the datebase
      tp = 0
      
      for Step in range(7,(12+1)):
            DirIN_1 = DirIN + "/" + BaseDateTime_1.strftime("%Y") + "/" + BaseDateTime_1.strftime("%Y%m%d%H")
            FileIN_1 =  "tp_" + BaseDateTime_1.strftime("%Y%m%d") + "_" + BaseDateTime_1.strftime("%H") + "_" + f'{Step:03d}' + ".grib"
            if os.path.exists(DirIN_1 + "/" + FileIN_1):
                  count_steps = count_steps + 1
                  tp = tp + mv.read(DirIN_1 + "/" + FileIN_1)

      for Step in range(1,(18+1)):  
            DirIN_0 = DirIN + "/" + BaseDateTime_0.strftime("%Y") + "/" + BaseDateTime_0.strftime("%Y%m%d%H")
            FileIN_0 =  "tp_" + BaseDateTime_0.strftime("%Y%m%d") + "_" + BaseDateTime_0.strftime("%H") + "_" + f'{Step:03d}' + ".grib"
            if os.path.exists(DirIN_0 + "/" + FileIN_0):
                  count_steps = count_steps + 1
                  tp = tp + mv.read(DirIN_0 + "/" + FileIN_0)

      # Converting the accumulated rainfall totals from m to mm, and converting the fieldset into a 16-byte float numpy array (to reduce memory consumption)
      if count_steps == 24:
            tp = tp * 1000
            tp = mv.values(tp).T.astype(np.float16)
      else:
            tp = 0
      
      return tp
      
      
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

      # Creating the variable that stores the independent rainfall realizations
      if tp_12 != 0 and tp_00 != 0: 
            tp = mv.merge(tp_12, tp_00)
      else:
            tp = 0

      # Convert the fieldset into a 16-byte float numpy array (to reduce memory consumption)
      tp = mv.values(tp).T.astype(np.float16)
      
      return tp


# Note: the rainfall values are already in mm and are valid for the period 00-00 UTC
def tp_ERA5_ecPoint_24h(BaseDateTime, DirIN):

      # Reading the accumulated rainfall values
      DirIN = DirIN + "/Pt_BC_PERC/" + BaseDateTime.strftime("%Y%m")
      FileIN =  "Pt_BC_PERC_" + BaseDateTime.strftime("%Y%m%d") + ".grib2"
      if os.path.exists(DirIN + "/" + FileIN):
            tp = mv.read(DirIN + "/" + FileIN)
      
      # Convert the fieldset into a 16-byte float numpy array (to reduce memory consumption)
      tp = mv.values(tp).T.astype(np.float16)
      
      return tp

###############################################################################################################


# Extracting the indipendent accumulated rainfall realizations for a specific number of sub-areas
print("Extracting accumulated rainfall totals from " + SystemFC)
BaseDate = BaseDateS

while BaseDate <= BaseDateF:
      
      print(" - Processing the date: ", BaseDate)

      # Computing the indipendent accumulated rainfall totals
      if SystemFC == "ERA5" and Acc == 12:
            DirIN_temp = GitRepo + "/" + DirIN + "/" + SystemFC
            tp_temp = tp_ERA5_12h(BaseDate, DirIN_temp)
      if SystemFC == "ERA5" and Acc == 24:
            DirIN_temp = GitRepo + "/" + DirIN + "/" + SystemFC
            tp_temp = tp_ERA5_24h(BaseDate, DirIN_temp)      
      elif SystemFC == "ERA5_ecPoint" and Acc == 12:
            DirIN_temp = GitRepo + "/" + DirIN + "/" + SystemFC + "_" + f'{Acc:02d}' + "h"
            tp_temp = tp_ERA5_ecPoint_12h(BaseDate, DirIN_temp)
      elif SystemFC == "ERA5_ecPoint" and Acc == 24:
            DirIN_temp = GitRepo + "/" + DirIN + "/" + SystemFC + "_" + f'{Acc:02d}' + "h"
            tp_temp = tp_ERA5_ecPoint_24h(BaseDate, DirIN_temp)
      NumGP_Global = tp_temp.shape[0]

      # Extracting the sub-areas
      if NumGP_Global != 0:
            
            i = int(0)
            j = int(NumGP_Global/NumSA)
            for ind_SA in range(NumSA):
                  
                  tp_sa_temp = tp_temp[i:j,:]

                  # Saving the extracted sub-areas
                  DirOUT_temp = GitRepo + "/" + DirOUT + "_" + f'{Acc:02d}' + "h/" + SystemFC + "/" + BaseDate.strftime("%Y%m%d")
                  if not os.path.exists(DirOUT_temp):
                        os.makedirs(DirOUT_temp)
                  FileOUT_temp = "tp_" + BaseDate.strftime("%Y%m%d") + "_" + f'{ind_SA:03d}' + ".npy"
                  np.save(DirOUT_temp + "/" + FileOUT_temp, tp_sa_temp) 

                  i = int(j)
                  j = int(j + (NumGP_Global/NumSA))

      BaseDate = BaseDate + timedelta(days=1)