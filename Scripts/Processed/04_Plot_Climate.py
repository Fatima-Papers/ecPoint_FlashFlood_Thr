import os
import numpy as np
import metview as mv

#############################################################################
# CODE DESCRIPTION
# 04_Plot_Climate.py plots modelled rainfall climatologies.
# Code runtime: negligible

# DESCRIPTION OF INPUT PARAMETERS
# Acc (integer, in hours): rainfall accumulation period.
# Perc (float): percentile to plot.
# Perc_list (list of integers): list of percentiles to compute.
# SystemFC_list (list of strings): list of forecasting systems to consider.
# Git_repo (string): path of local github repository.
# DirIN (string): relative path for the input directory containing ERA5.
# DirOUT (string): relative path for the output directory containing the climatology.

# INPUT PARAMETERS
Acc = 12
Perc = 97
Perc_list = np.append(np.arange(1,100), np.array([99.4, 99.5,99.8,99.95]))
SystemFC_list = ["ERA5"]
GitRepo = "/ec/vol/ecpoint_dev/mofp/Papers_2_Write/RainThr_4FlashFloodFC_ecPointERA5"
DirIN = "Data/Compute/ClimateG"
DirOUT = "Data/Plot/ClimateG"
#############################################################################

# Indexing the percentile to plot
ind_Perc = np.where(Perc_list == Perc)[0][0]

# Determining the event's return period associated to the considered percentile
RP = round(1 / (100 - Perc),1)
if RP.is_integer() == True:
    RP = int(RP)

# Plotting the modelled climatologies for a specific forecasting system
for SystemFC in SystemFC_list:

    print("Plotting the modelled climatology for " + SystemFC + ", RP = " + str(RP) + " years (Perc = " + str(Perc) + "th)")

    # Setting input/output directories
    DirIN_temp = GitRepo + "/" + DirIN + "_" + f'{Acc:02d}' + "h/" + SystemFC
    DirOUT_temp = GitRepo + "/" + DirOUT + "_" + f'{Acc:02d}' + "h/" + SystemFC
    if not os.path.exists(DirOUT_temp):
        os.makedirs(DirOUT_temp)

    # Reading the modelled climatology
    FileIN_temp = "Climate_" + SystemFC  + "_" + f'{Acc:02d}' + "h.grib"
    climate = mv.read(DirIN_temp + "/" + FileIN_temp)
    climate = climate[ind_Perc]

    # Plotting the modelled climatology
    coastlines = mv.mcoast(
        map_coastline_thickness = 2,
        map_coastline_colour = "charcoal",
        map_coastline_resolution = "medium",
        map_boundaries = "on",
        map_boundaries_colour = "charcoal",
        map_boundaries_thickness = 1,
        map_grid = "off",
        map_label = "off"
        )

    contouring = mv.mcont(
        legend = "on",
        contour = "off",
        contour_level_selection_type = "level_list",
        contour_level_list = [0,0.5,2,5,10,20,30,40,50,60,80,100,125,150,200,300,500,50000],
        contour_label = "off",
        contour_shade = "on",
        contour_shade_colour_method = "list",
        contour_shade_method = "area_fill",
        contour_shade_colour_list = ["white","RGB(0.75,0.95,0.93)","RGB(0.45,0.93,0.78)","RGB(0.07,0.85,0.61)","RGB(0.53,0.8,0.13)","RGB(0.6,0.91,0.057)","RGB(0.9,1,0.4)","RGB(0.89,0.89,0.066)","RGB(1,0.73,0.0039)","RGB(1,0.49,0.0039)","red","RGB(0.85,0.0039,1)","RGB(0.63,0.0073,0.92)","RGB(0.37,0.29,0.91)","RGB(0.04,0.04,0.84)","RGB(0.042,0.042,0.43)","RGB(0.45,0.45,0.45)"]
        )

    legend = mv.mlegend(
        legend_text_colour = "charcoal",
        legend_text_font = "arial",
        legend_text_font_size = 0.5,
        legend_entry_plot_direction = "row",
        legend_box_blanking = "on",
        legend_entry_text_width = 50
        )

    title = mv.mtext(
        text_line_count = 3,
        text_line_1 = "Rainfall climatology from " + SystemFC,
        text_line_2 = str(RP) + "-year retrurn period (Perc = " +  str(Perc) + "th)",
        text_line_3 = " ",
        text_colour = "charcoal",
        text_font = "arial",
        text_font_size = 0.5
        )

    # Saving the plot of the modelled climatology
    FileOUT_temp = "ClimateG_" + SystemFC + "_" + f'{Acc:02d}' + "h_" + str(RP) + "RP_" + str(Perc) + ".grib"
    svg = mv.png_output(output_name = DirOUT_temp + "/" + FileOUT_temp)
    mv.setoutput(svg)
    mv.plot(climate, coastlines, contouring, title, legend)