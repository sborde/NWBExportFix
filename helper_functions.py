from pynwb import NWBHDF5IO
from pynwb import NWBFile

def load_file(input_path):
    """
    Loads an NWB file on the given path.

    Parameters
    ----------
    input_path : string
        path to the NWB file

    Returns
    -------
    input_file : NWBFile
        the loaded NWB file
    series_list : list[str]
        list of series found in the NWB file

    """
    io = NWBHDF5IO(input_path, 'r+')
    input_file = io.read()
    series_list = list(input_file.acquisition.keys())
    
    return input_file, series_list

def save_file(output_path, nwbfile):
    io = NWBHDF5IO(output_path, 'w')
    io.write(nwbfile, link_data=False)
    io.close()

def clone_with_general_data(input_file):
    
    session_start_time = input_file.session_start_time
    identifier = input_file.identifier
    session_description = input_file.session_description
    timestamps_reference_time = input_file.timestamps_reference_time
    
    nwbfile = NWBFile(
                session_description = session_description,  # required
                identifier = identifier,  # required
                session_start_time = session_start_time,  # required
                timestamps_reference_time = timestamps_reference_time)  # optional
    
    return nwbfile
