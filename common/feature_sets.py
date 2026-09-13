# Script feature_sets.py
# Define feature sets for the hybrid model

# last edit: 13.09.2026
# Copyright (c) 2026 Andreas Mätzler
# All rights reserved.
# You may not use, copy, modify, distribute, or reproduce this code for any purpose without explicit written permission from the author.

# Time-only base, no topo or radiation features
# TIME = ['PV_SUMME_INSTALLIERT', 'HOUR_DEZ', 'DAY_YEAR', 'SIN_HOUR', 'COS_HOUR', 'SIN_DAY', 'COS_DAY'] # reduced to 'SIN_HOUR', 'COS_HOUR', 'COS_DAY'
TIME = ['SIN_HOUR', 'COS_HOUR', 'COS_DAY']

# GIS + time base, adds pv-size, topography and potential radiation
GIS_TIME = TIME + ['PV_SUMME_INSTALLIERT', 'HEIGHT', 'SOLAR_RADIATION_GLOBALRAD', 'SOLAR_RADIATION_DIRECTRAD', 'SOLAR_RADIATION_DIFFUSERAD']

# 4 SEVIRI WMS bands directly available via EUMETSAT WMS service
SEVIRI4 = ['VIS006', 'IR_039', 'WV_062', 'IR_108']

# All 12 SEVIRI bands
SEVIRI12 = ['VIS006', 'VIS008', 'IR_016', 'IR_039',
         'WV_062', 'WV_073', 'IR_087', 'IR_097',
         'IR_108', 'IR_120', 'IR_134', 'HRV']

# Ground sensor measurements variables
SENSOR = ['GLOBAL_RADIATION_SENSOR_VALUE', 'GLOBAL_RADIATION_SENSOR_TEMPERATURE', 'GLOBAL_RADIATION_SENSOR_DISTANCE']

FEATURE_SETS = {
    'FS1_TIME'            : {'features': TIME},    # time-only base, no topo or radiation features
    'FS2_GIS_TIME'        : {'features': GIS_TIME}, # GIS + time base, adds pv-size, topography and potential radiation
    'FS3_GIS_SENSOR_TIME' : {'features': GIS_TIME + SENSOR}, # GIS + sensor measurements only
    'FS4_SEV4_TIME'       : {'features': TIME + SEVIRI4}, # time + 4 SEVIRI WMS bands directly available via EUMETSAT WMS service
    'FS5_SEV4_GIS_TIME'   : {'features': GIS_TIME + SEVIRI4}, # GIS + time + 4 SEVIRI WMS bands directly available via EUMETSAT WMS service
    'FS6_SEV4_GIS_SENSOR_TIME'  : {'features': GIS_TIME + SEVIRI4 + SENSOR}, # GIS + time + 4 SEVIRI WMS bands + sensor measurements
    'FS7_SEV12_TIME'            : {'features': TIME + SEVIRI12}, # time + 12 SEVIRI WMS bands directly available via EUMETSAT WMS service
    'FS8_SEV12_GIS_TIME'        : {'features': GIS_TIME + SEVIRI12},  # GIS + time + 12 SEVIRI WMS bands directly available via EUMETSAT WMS service
    'FS9_SEV12_GIS_SENSOR_TIME' : {'features': GIS_TIME + SEVIRI12 + SENSOR},   # GIS + time + 12 SEVIRI WMS bands + sensor measurements
}
