import os
from datetime import datetime, timedelta
import numpy as np
import metview as mv

#####################################################################
# CODE DESCRIPTION
# 03_Compute_Climate_ERA5.py computes modelled rainfall climatology from ERA5.
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
BaseDateS = datetime(2000,1,1,0)
BaseDateF = datetime(2020,12,31,0)
Acc = 12
Perc_list = np.append(np.arange(1,100), np.array([99.4, 99.5,99.8,99.95]))
GitRepo = "/ec/vol/ecpoint_dev/mofp/Papers_2_Write/ecPoint_FlashFlood_Thr"
DirIN = "Data/Raw/Reanalysis/ERA5"
DirOUT = "Data/Compute/Climate/ERA5"
#####################################################################


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

      # Extract the considered sub-area, and convert the fieldset into a 16-byte float numpy array (to reduce memory consumption)
      tp = mv.values(mv.mask(tp, Sub_Area, "missing")).T.astype(np.float16)
      ind_sa = ~np.all(np.isnan(tp), axis=1)
      tp_sa = tp[ind_sa]
      
      return ind_sa, tp_sa

###############################################################################################################


# Setting input/output directories
DirIN_temp = GitRepo + "/" + DirIN
DirOUT_temp = GitRepo + "/" + DirOUT + "_" + f'{Acc:02d}' + "h"
if not os.path.exists(DirOUT_temp):
      os.makedirs(DirOUT_temp)

# Setting the grib sample where to store the percentiles as grib
BaseDate = BaseDateS + timedelta(hours=6)
DirIN_sample = GitRepo + "/" + DirIN + "/" + BaseDate.strftime("%Y") + "/" + BaseDate.strftime("%Y%m%d%H")
FileIN_sample =  "tp_" + BaseDate.strftime("%Y%m%d") + "_" + BaseDate.strftime("%H") + "_000.grib"
percs_sample_global_grib = mv.read(DirIN_sample + "/" + FileIN_sample)
percs_sample_global_array = mv.values(percs_sample_global_grib[0]).T
percs_sample_sa = mv.values(mv.mask(percs_sample_global_grib, Sub_Area, "missing")).T
NumGP = percs_sample_sa[~np.isnan(percs_sample_sa)].shape[0]

# Extracting the independent rainfall realizations from ERA5
print("Extracting the independent rainfall realizations")
tp_tot_sa = np.empty((NumGP,0))
BaseDate = BaseDateS
while BaseDate <= BaseDateF:
      print(" - Reading the date: ", BaseDate)
      ind_sa, tp_temp = tp_ERA5_12h(BaseDate, DirIN_temp)
      if tp_temp.shape != 0:
            tp_tot_sa = np.hstack((tp_tot_sa, tp_temp))
      BaseDate = BaseDate + timedelta(days=1)

# Compute the percentiles 
print("Computing the rainfall climatology")
percs_sa = np.percentile(tp_tot_sa, Perc_list, axis=1).T
npercs = percs_sa.shape[1]

#  Storing the percentiles as grib while restoring the global field
percs_tot_global = None
for ind_perc in range(npercs):
      temp_perc_sa = percs_sa[:,ind_perc]
      percs_sample_global_array[ind_sa] = temp_perc_sa
      percs_tot_global = mv.merge(percs_tot_global, mv.set_values(percs_sample_global_grib[0], percs_sample_global_array))

# Saving the output file
print("Storing the output file")
FileOUT = DirOUT_temp + "/Climate_ERA5_Italy_" + f'{Acc:02d}' + "h.grib"
mv.write(FileOUT, percs_tot_global)