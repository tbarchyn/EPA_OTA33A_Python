import numpy as np
from scipy.optimize import curve_fit
from ota33a import OTA33A as d
from ota33a import OTM33A_loadExcel as ex

import pylab as pl; pl.close('all')
import sys
'''
    This software uses EPA's OTA33A Method. From concentration and wind data
    the emission rate from a point source can be estimated.
    
    Any functions that begin with the prefix "d.", information can be found
    within the defs.py file.
    
    This program was coded without the ability to automatically read in all
    different types of files. This is left up to the user. This program will
    only provide a function to perform the data analysis.
    '''
################
#    INPUTS    #
################

# WOULD YOU LIKE TO SEE A PLOT?
make_plot      = True

# DATA FILES AND SOURCE-RECEPTOR DISTANCE
gasConc,ws3,wd3,ws2,wd2,temp,pres,ws3z,ws3y,ws3x = ex.load_excel('STR_3061611_01.xls')

distance = 42. # meters

# TRACER INFORMATION
chemical_name = 'CH4' # for plots
mw_chemical   = 16.04 # [g mol-1]

# BIN LIMITS
theta_start   = 5.
theta_end     = 365.
delta_theta   = 10.

# DATA CUTOFFS
wslimit       = 0.0 # set wind speed cut limit [m s-1]
wdlimit       = 60.0 # set wind angle cut limit [+/- deg]. 180 indicates no filter
cutoff        = 2 # bin density cutoff limit

############################
#    BEGIN CALCULATION     #
############################

a = d.fieldData(gasConc,temp,pres,ws3z,ws3x,ws3y,distance,16.04,'CH4')

massRate, volumeRate = a.getEmissionRate(make_plot=True)

print("The EPA's OTA33A method predicts an emission rate of %.2f g/s" % (massRate))

