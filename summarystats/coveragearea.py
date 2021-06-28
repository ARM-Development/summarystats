import pyart
import numpy as np

def rain_coverage(radar, gate_rain=1):
    """ Returns percent coverage of rain snow """
    temp_radar = radar.extract_sweeps([0])
    ref = temp_radar.fields['gate_id']['data']
    total_len= len(ref.flatten())
    ref_rain = len(np.argwhere(ref==gate_rain))
    ref_rain_per = (ref_rain/total_len)*100
    del temp_radar
    return ref_rain_per

def snow_coverage(radar, gate_snow=2):
    """ Returns percent coverage of snow gates """
    temp_radar = radar.extract_sweeps([0])
    ref = temp_radar.fields['gate_id']['data']
    total_len= len(ref.flatten())
    ref_snow = len(np.argwhere(ref==gate_snow))
    ref_snow_per = (ref_snow/total_len)*100
    del temp_radar
    return ref_snow_per

def convection_coverage(radar, convection_threshold=40.0):
    """ Returns percent of convection """
    temp_radar = radar.extract_sweeps([0])
    ref = temp_radar.fields['corrected_reflectivity']['data']
    total_len = len(ref.flatten())
    ref_conv = len(np.argwhere(ref >= convection_threshold))
    ref_conv_per = (ref_conv/total_len)*100
    del temp_radar
    return ref_conv_per
