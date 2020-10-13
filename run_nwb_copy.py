from helper_functions import load_file, save_file, clone_with_general_data
from channel_create_functions import acquisition_copy_functions, stimulus_copy_functions, create_mock_electrode

base_dir = 'E:\spyder_projects\\'

input_filename = '1806203fs-3.nwb'
donor_filename = '1805102mg-2.nwb'
output_filename = 'output_test_file.nwb'

donor_series_idx = [1, 2, 3, 26, 27]
replace_series_idx = [1, 2, 3, 40, 53]

input_file, input_series = load_file(base_dir + input_filename)
donor_file, donor_series = load_file(base_dir + donor_filename)

nwbfile = clone_with_general_data(input_file)
electrode = create_mock_electrode(nwbfile)

correct_stim_idx, donor_stim_idx = 0, 0
for series_idx, series_name in enumerate(input_series):
    
    acquisition_data = input_file.acquisition.get(series_name)
    acquisition_type = acquisition_data.neurodata_type
    
    if (series_idx+1) in replace_series_idx:
        print(f'Series #{series_idx} {series_name} is corrupted')
        
        donor_stim_series_name = donor_series[donor_series_idx[donor_stim_idx] - 1]
        stimulus_data = donor_file.stimulus.get(donor_stim_series_name)
        donor_stim_idx += 1
        
    else:
        print(f'Series #{series_idx} {series_name} is correct, just copy')
        
        original_stim_series_name = input_series[correct_stim_idx];
        stimulus_data = input_file.stimulus.get(original_stim_series_name)
        correct_stim_idx += 1
        
    output_acquisition = acquisition_copy_functions[acquisition_type](nwbfile, acquisition_data, series_name, electrode)
    sweep_number = output_acquisition.sweep_number
    starting_time = output_acquisition.starting_time
    output_stimulus = stimulus_copy_functions[acquisition_type](nwbfile, stimulus_data, series_name, electrode, sweep_number, starting_time)
    
    nwbfile.add_acquisition(output_acquisition)
    nwbfile.add_stimulus(output_stimulus)
    
save_file(base_dir + output_filename, nwbfile)