
from datetime import datetime
from dateutil.tz import tzlocal
from pynwb import NWBFile
import numpy as np
from pynwb import NWBHDF5IO
import pynwb.icephys

from helper_functions import load_file, clone_with_general_data
from channel_create_functions import channel_copy_functions, create_mock_electrode

## Parameter definitions################################################

base_dir = 'E:\spyder_projects\\'

input_path = base_dir + '1806203fs-3.nwb'
donor_path = base_dir + '1805102mg-2.nwb'
output_path = base_dir + 'output_test_file.nwb'

donor_series_idx = [1, 2, 3, 26, 27]
replace_series_idx = [1, 2, 3, 40, 53]

## Load input and donor files ##########################################
input_file, input_series = load_file(input_path)
donor_file, donor_series = load_file(donor_path)

## Create a new NWB file with the general data #########################
nwbfile = clone_with_general_data(input_file)


## start of the for loop ###############################################
Correct_stimulus_cycle = 0;
Donor_cycle = 1;

electrode = create_mock_electrode(nwbfile)

for series_idx, series_name in enumerate(input_series):
    
    acquisition_data = input_file.acquisition.get(series_name)    
    NeuroData_type = acquisition_data.neurodata_type
    
    if series_idx in replace_series_idx: ## replace with the donor series
        print(f'Series #{series_idx} {series_name} is corrupted')
        # TODO: extract corresponding data from the donor and save to acquisition data
        
        # StimData = Donor_nwbfile.stimulus.get('index__00')
    else:
        print(f'Series #{series_idx} {series_name} is correct, just copy')
        # TODO: extract corresponding data from the original file and save to acquisition data
        
    output_acquisition = channel_copy_functions[NeuroData_type](nwbfile, acquisition_data, series_name, electrode)
    nwbfile.add_acquisition(output_Acquisition)
     
##export ##############################################################

io30 = NWBHDF5IO(Output_Modified_NWB_file, 'w')
io30.write(nwbfile, link_data=False)
io30.close()

with NWBHDF5IO(Output_Modified_NWB_file, 'w') as io3:
    io3.write(nwbfile,link_data=False)
    

from pynwb import NWBFile, NWBHDF5IO, get_manager
manager = get_manager()
with NWBHDF5IO(Output_Modified_NWB_file, mode='w', manager=manager) as io4:
    io4.write(nwbfile, link_data=False)



###################### TESTING SEGMENT ###############################################################

acquisition_data = donor_file.stimulus.get('index_01')
NeuroData_type = acquisition_data.neurodata_type
series_name = 'index_01'

output_acquisition = channel_copy_functions[NeuroData_type](nwbfile, acquisition_data, series_name, electrode)







output_Acquisition = copy_VoltageClampSeries(nwbfile, Acquisition_data, 'index_000')
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