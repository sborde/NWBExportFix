# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 15:31:24 2020

@author: TG ProBook
"""


from datetime import datetime
from dateutil.tz import tzlocal
from pynwb import NWBFile
import numpy as np
from pynwb import NWBHDF5IO
import pynwb.icephys


## inputs ##############################################################################################
Input_file = 'E:\spyder_projects\\1806203fs-3.nwb'
Donor_Input_file = 'E:\spyder_projects\\1805102mg-2.nwb'
Output_Modified_NWB_file = 'E:\spyder_projects\\output_test_file.nwb'

Donor_series = [1, 2, 3, 26, 27]
Series_to_replace = [1, 2, 3, 40, 53]

## read input file #####################################################################################
io = NWBHDF5IO(Input_file, 'r+')
inputNWB_file = io.read()
List_of_series = inputNWB_file.acquisition.keys() 

## get general data from nwb file ######################################################################
Ext_session_start_time = inputNWB_file.session_start_time
Ext_identifier = inputNWB_file.identifier
Ext_session_description = inputNWB_file.session_description
Ext_timestamps_reference_time = inputNWB_file.timestamps_reference_time

## create an NWB file and set general data ############################################################
nwbfile = NWBFile(session_description = Ext_session_description,  # required
                  identifier = Ext_identifier,  # required
                  session_start_time = Ext_session_start_time,  # required
                  timestamps_reference_time = Ext_timestamps_reference_time)  # optional

## read the donor file ################################################################################
io2 = NWBHDF5IO(Donor_Input_file, 'r+')
Donor_nwbfile = io2.read()
Donor_list_of_series = Donor_nwbfile.acquisition.keys()

## start of the for loop ###############################################################################
Correct_stimulus_cycle = 0;
Donor_cycle = 1;

for Loopcycle in len(List_of_series)
        
    ## get Neurodatatype 
    NeuroData_type = inputNWB_file.acquisition['index_000'].neurodata_type
    Acquisition_data = inputNWB_file.acquisition.pop('index_000')
    TimeSeries_name = inputNWB_file.acquisition.keys
    
    if Loopcycle in Series_to_replace ## replace with the donor series
    print('Series is corrupted')
    
        if 
        StimData = Donor_nwbfile.stimulus.get('index__00')
    
    print
    
##export ##############################################################################################
nwbfile.add_acquisition(output_Acquisition2)

io30 = NWBHDF5IO(Output_Modified_NWB_file, 'w')
io30.write(nwbfile, link_data=False)
io30.close()

with NWBHDF5IO(Output_Modified_NWB_file, 'w') as io3:
    io3.write(nwbfile,link_data=False)
    

from pynwb import NWBFile, NWBHDF5IO, get_manager
manager = get_manager()
with NWBHDF5IO(Output_Modified_NWB_file, mode='w', manager=manager) as io4:
    io4.write(nwbfile, link_data=False)

### functions ########################################################################################

def copy_VoltageClampSeries(input_acquisition_data, TimeSeries_name):
          
    ## get VC parameters, compress and write 
    rawdata = Acquisition_data.data[:]
        
    output_Acquisition2 = pynwb.icephys.VoltageClampSeries(
            name = TimeSeries_name,
            data = rawdata,
            capacitance_fast = Acquisition_data.capacitance_fast,
            capacitance_slow = Acquisition_data.capacitance_slow,
            comments =  Acquisition_data.comments,
            conversion = Acquisition_data.conversion,
            description = Acquisition_data.description,
            electrode = Acquisition_data.electrode,
            gain = Acquisition_data.gain,
            rate = Acquisition_data.rate,
            resistance_comp_bandwidth = Acquisition_data.resistance_comp_bandwidth,
            resistance_comp_correction = Acquisition_data.resistance_comp_correction,
            resistance_comp_prediction = Acquisition_data.resistance_comp_prediction,
            resolution = Acquisition_data.resolution,
            starting_time = Acquisition_data.starting_time,
            # starting_time_unit = Acquisition_data.starting_time_unit,
            stimulus_description = Acquisition_data.stimulus_description,
            sweep_number = Acquisition_data.sweep_number,
            unit = Acquisition_data.unit,
            whole_cell_capacitance_comp = Acquisition_data.whole_cell_capacitance_comp,
            whole_cell_series_resistance_comp = Acquisition_data.whole_cell_series_resistance_comp
        )
    return output_Acquisition


###################### TESTING SEGMENT ###############################################################

output_Acquisition = copy_VoltageClampSeries(Acquisition_data, TimeSeries_name)
print(Acquisition_data)


print(ExtractedParameters['electrode'])

a = Acquisition_data.data
print(Acquisition_data.data)







## could be important 
session_start_time = inputNWB_file.acquisition.keys() ## list the index elements
test = Donor_nwbfile.stimulus.get('index_00')
print(test.)
print(Donor_nwbfile.acquisition.pop('index_00'))



 ## get prameters 
    ExtractedParameters = {
        'capacitance_fast': [Acquisition_data.capacitance_fast],
        'capacitance_slow': [Acquisition_data.capacitance_slow],
        'comments': [Acquisition_data.comments],
        'conversion': [Acquisition_data.conversion],
        'description': [Acquisition_data.description],
        'electrode': [Acquisition_data.electrode],
        'gain': [Acquisition_data.gain],
        'rate': [Acquisition_data.rate],
        'resistance_comp_bandwidth': [Acquisition_data.resistance_comp_bandwidth],
        'resistance_comp_correction': [Acquisition_data.resistance_comp_correction],
        'resistance_comp_prediction': [Acquisition_data.resistance_comp_prediction],
        'resolution': [Acquisition_data.resolution],
        'starting_time': [Acquisition_data.starting_time],
        'starting_time_unit': [Acquisition_data.starting_time_unit],
        'stimulus_description': [Acquisition_data.stimulus_description],
        'sweep_number': [Acquisition_data.sweep_number],
        'unit': [Acquisition_data.unit],
        'whole_cell_capacitance_comp': [Acquisition_data.whole_cell_capacitance_comp],
        'whole_cell_series_resistance_comp': [Acquisition_data.whole_cell_series_resistance_comp]
        }
    
    
    
    
    for key in inputNWB_file.acquisition.keys():
        print(key)
    
    
    key_iterable = dictionary.keys()
    key_list = list(inputNWB_file.acquisition.keys())
    
    
    
    
     output_Acquisition2 = pynwb.icephys.VoltageClampSeries(
            name = 'index_000',
            data = rawdata,
            capacitance_fast = Acquisition_data.capacitance_fast,
            capacitance_slow = Acquisition_data.capacitance_slow,
            comments =  Acquisition_data.comments,
            conversion = Acquisition_data.conversion,
            description = Acquisition_data.description,
            electrode = Acquisition_data.electrode,
            gain = Acquisition_data.gain,
            rate = Acquisition_data.rate,
            resistance_comp_bandwidth = Acquisition_data.resistance_comp_bandwidth,
            resistance_comp_correction = Acquisition_data.resistance_comp_correction,
            resistance_comp_prediction = Acquisition_data.resistance_comp_prediction,
            resolution = Acquisition_data.resolution,
            starting_time = Acquisition_data.starting_time,
            # starting_time_unit = Acquisition_data.starting_time_unit,
            stimulus_description = Acquisition_data.stimulus_description,
            sweep_number = Acquisition_data.sweep_number,
            unit = Acquisition_data.unit,
            whole_cell_capacitance_comp = Acquisition_data.whole_cell_capacitance_comp,
            whole_cell_series_resistance_comp = Acquisition_data.whole_cell_series_resistance_comp
        )