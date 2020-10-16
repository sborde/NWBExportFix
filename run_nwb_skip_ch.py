import json

from helper_functions import load_file, save_file, clone_with_general_data
from channel_create_functions import acquisition_copy_functions, stimulus_copy_functions, create_mock_electrode

base_dir = 'E:\spyder_projects\\'

input_filename = '1903292fs-8.nwb'
output_filename = 'output_test_file.nwb'

delete_series_idx = set(range(32, 43))

input_file, i_io, _ = load_file(base_dir + input_filename)

acq_names = input_file.acquisition.keys()
stim_names = list(input_file.stimulus.keys())
stim_ind = 0

nwbfile = clone_with_general_data(input_file)
electrode = create_mock_electrode(nwbfile)

for acq_i, acq_name in enumerate(acq_names):
    
    if acq_i in delete_series_idx:
        continue
    
    acquisition_data = input_file.acquisition.get(acq_name)
    acquisition_type = acquisition_data.neurodata_type
    
    series_name = stim_names[stim_ind]
    stimulus_data = input_file.stimulus.get(series_name)
    
    acq_copy_func = acquisition_copy_functions[acquisition_type]
    stim_copy_func = stimulus_copy_functions[acquisition_type]
    
    output_acq = acq_copy_func(nwbfile, acquisition_data, series_name, electrode)
    output_stim = stim_copy_func(nwbfile, acquisition_data, stimulus_data, series_name, electrode)
    
    nwbfile.add_acquisition(output_acq)
    nwbfile.add_stimulus(output_stim)
    
    stim_ind += 1


save_file(base_dir + output_filename, nwbfile)
i_io.close()


## Print data of the new file for testing purposes
for acq_name, stim_name in zip(nwbfile.acquisition.keys(), nwbfile.stimulus.keys()):
    print(f'{acq_name} {stim_name}')
    acq_desc = json.loads(nwbfile.acquisition[acq_name].description)
    stim_desc = json.loads(nwbfile.stimulus[stim_name].description)
    
    for key in acq_desc.keys():
        print(f'{acq_desc[key]} {stim_desc[key]}')
    