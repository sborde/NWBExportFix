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
            # starting_time_unit = input_acquisition.starting_time_unit,
            stimulus_description = input_acquisition.stimulus_description,
            sweep_number = input_acquisition.sweep_number,
            unit = input_acquisition.unit,
            whole_cell_capacitance_comp = input_acquisition.whole_cell_capacitance_comp,
            whole_cell_series_resistance_comp = input_acquisition.whole_cell_series_resistance_comp
        )
    return output_acquisition



def copy_VoltageClampStimulusSeries(nwbfile, input_stimulus, TimeSeries_name, electrode):

    rawdata = input_stimulus.data[:]
    
    output_Stimulus = icph.VoltageClampStimulusSeries(
            name = TimeSeries_name,
            data = rawdata,
            description = input_stimulus.description,
            comments =  input_stimulus.comments,
            conversion = input_stimulus.conversion,
            electrode = electrode,
            gain = input_stimulus.gain,
            rate = input_stimulus.rate,
            resolution = input_stimulus.resolution,
            starting_time = input_stimulus.starting_time,
            # starting_time_unit = input_stimulus.starting_time_unit,
            stimulus_description = input_stimulus.stimulus_description,
            sweep_number = input_stimulus.sweep_number,
            unit = input_stimulus.unit,
        )
    return output_Stimulus



def copy_CurrentClampSeries(nwbfile, input_acquisition, TimeSeries_name, electrode):
    
    rawdata = input_acquisition.data[:] 
     
    output_Acquisition = icph.CurrentClampSeries(
            name = TimeSeries_name,
            data = rawdata,
            bias_current = input_acquisition.bias_current,
            bridge_balance = input_acquisition.bridge_balance,
            capacitance_compensation = input_acquisition.capacitance_compensation,
            comments =  input_acquisition.comments,
            conversion = input_acquisition.conversion,
            description = input_acquisition.description,
            electrode = electrode,
            gain = input_acquisition.gain,
            rate = input_acquisition.rate,
            resolution = input_acquisition.resolution,
            starting_time = input_acquisition.starting_time,
            # starting_time_unit = input_acquisition.starting_time_unit,
            stimulus_description = input_acquisition.stimulus_description,
            sweep_number = input_acquisition.sweep_number,
            unit = input_acquisition.unit,
        )
    return output_Acquisition


def copy_CurrentClampStimulusSeries(nwbfile, input_stimulus, TimeSeries_name, electrode):
    
     rawdata = input_stimulus.data[:] 
     
     output_Acquisition = icph.CurrentClampStimulusSeries(
            name = TimeSeries_name,
            data = rawdata,
            comments =  input_stimulus.comments,
            conversion = input_stimulus.conversion,
            description = input_stimulus.description,
            electrode = electrode,
            gain = input_stimulus.gain,
            rate = input_stimulus.rate,
            resolution = input_stimulus.resolution,
            starting_time = input_stimulus.starting_time,
            # starting_time_unit = input_stimulus.starting_time_unit,
            stimulus_description = input_stimulus.stimulus_description,
            sweep_number = input_stimulus.sweep_number,
            unit = input_stimulus.unit,
         )
     return output_Acquisition


def create_mock_electrode(nwbfile):
    device = nwbfile.create_device(name='Heka ITC-1600')
    electrode = nwbfile.create_icephys_electrode(
                    name="elec0",
                    description='a mock intracellular electrode',
                    device=device)
    return electrode

acquisition_copy_functions = {
    'VoltageClampSeries': copy_VoltageClampSeries,
    'CurrentClampSeries': copy_CurrentClampSeries
    }

stimulus_copy_functions = {
    'VoltageClampSeries': copy_VoltageClampStimulusSeries,
    'CurrentClampSeries': copy_CurrentClampStimulusSeries    
    }
