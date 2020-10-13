import pynwb.icephys as icph

def copy_VoltageClampSeries(nwbfile, input_acquisition, time_series_name, electrode):
    
    rawdata = input_acquisition.data[:]    
    

    output_acquisition = icph.VoltageClampSeries(
            name = time_series_name,
            data = rawdata,
            capacitance_fast = input_acquisition.capacitance_fast,
            capacitance_slow = input_acquisition.capacitance_slow,
            comments =  input_acquisition.comments,
            conversion = input_acquisition.conversion,
            description = input_acquisition.description,
            electrode = electrode,
            gain = input_acquisition.gain,
            rate = input_acquisition.rate,
            resistance_comp_bandwidth = input_acquisition.resistance_comp_bandwidth,
            resistance_comp_correction = input_acquisition.resistance_comp_correction,
            resistance_comp_prediction = input_acquisition.resistance_comp_prediction,
            resolution = input_acquisition.resolution,
            starting_time = input_acquisition.starting_time,
            # starting_time_unit = Acquisition_data.starting_time_unit,
            stimulus_description = input_acquisition.stimulus_description,
            sweep_number = input_acquisition.sweep_number,
            unit = input_acquisition.unit,
            whole_cell_capacitance_comp = input_acquisition.whole_cell_capacitance_comp,
            whole_cell_series_resistance_comp = input_acquisition.whole_cell_series_resistance_comp
        )
    
    return output_acquisition



def copy_VoltageClampStimulusSeries(nwbfile, input_Stimulus_data, TimeSeries_name, electrode):

    rawdata = input_Stimulus_data.data[:]
    
    
    output_Stimulus = icph.VoltageClampStimulusSeries(
            name = TimeSeries_name,
            data = rawdata,
            description = input_Stimulus_data.description,
            comments =  input_Stimulus_data.comments,
            conversion = input_Stimulus_data.conversion,
            electrode = elec,
            gain = input_Stimulus_data.gain,
            rate = input_Stimulus_data.rate,
            resolution = input_Stimulus_data.resolution,
            starting_time = input_Stimulus_data.starting_time,
            # starting_time_unit = Acquisition_data.starting_time_unit,
            stimulus_description = input_Stimulus_data.stimulus_description,
            sweep_number = input_Stimulus_data.sweep_number,
            unit = input_Stimulus_data.unit,
        )
    return output_Stimulus


def create_mock_electrode(nwbfile):
    device = nwbfile.create_device(name='Heka ITC-1600')
    electrode = nwbfile.create_icephys_electrode(
                    name="elec0",
                    description='a mock intracellular electrode',
                    device=device)
    return electrode

channel_copy_functions = {
    'VoltageClampSeries': copy_VoltageClampSeries}