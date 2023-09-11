#!/bin/bash

###########################################################################
# CODE DESCRIPTION
# Retrieve_ERA5_ecPoint.sh retrieves (short-range) ERA5_ecPoint rainfall forecasts 
# (point-scale rainfall totals over the ERA5 grid, at 31 km spatial resolution). The total 
# precipitation is already accumulated over the period of interest.

# DESCRIPTION OF INPUT PARAMETERS
# Git_repo (string): path of local github repository
# DirIN_full (string): full path of the database containing the ecPoint-ERA5 rainfall forecasts.
# DirOUT (string): relative path for the output directory

# INPUT PARAMETERS
Git_repo="/ec/vol/ecpoint_dev/mofp/Papers_2_Write/ecPoint_FlashFlood_Thr"
DirIN_full="/ec/vol/highlander/ERA5_ecPoint_70yr/Rainfall_12h"
DirOUT="Data/Raw/Reanalysis/ERA5_ecPoint_12h"
###########################################################################


# Setting input directories
DirIN_full_Grid=${DirIN_full}/Grid_BC_VALS
DirIN_full_Pt=${DirIN_full}/Pt_BC_PERC
DirIN_full_WT=${DirIN_full}/WT

# Setting output directories
DirOUT_Grid=${Git_repo}/${DirOUT}/Grid_BC_VALS
DirOUT_Pt=${Git_repo}/${DirOUT}/Pt_BC_PERC
DirOUT_WT=${Git_repo}/${DirOUT}/WT
mkdir -p ${DirOUT_Grid}
mkdir -p ${DirOUT_Pt}
mkdir -p ${DirOUT_WT}

# Retrieving ecPoint_ERA5 rainfall forecasts
for Year in ${Years_array[@]}; do
      
      echo "Retrieving year " ${Year}

      cd ${DirIN_full_Grid}; cp -r 198* 199* 200* 201* 2020*  ${DirOUT_Grid}
      cd ${DirIN_full_Pt}; cp -r 198* 199* 200* 201* 2020* ${DirOUT_Pt}
      cd ${DirIN_full_WT};  cp -r 198* 199* 200* 201* 2020* ${DirOUT_WT}

done