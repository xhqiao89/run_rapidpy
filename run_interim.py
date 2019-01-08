from datetime import datetime
from RAPIDpy.inflow import run_lsm_rapid_process
#------------------------------------------------------------------------------
#main process
#------------------------------------------------------------------------------
if __name__ == "__main__":
    run_lsm_rapid_process(
        rapid_executable_location='/home/sherry/rapid/run/rapid',
        rapid_io_files_location='/home/sherry/Downloads/ecmwf',
        lsm_data_location='/home/sherry/Downloads/ecmwf/era_temp', #path to folder with LSM data
        simulation_start_datetime=datetime(1980, 1, 1),
        simulation_end_datetime=datetime(2014, 12, 31),
        generate_rapid_namelist_file=True, #if you want to run RAPID manually later
        run_rapid_simulation=True, #if you want to run RAPID after generating inflow file
        generate_return_periods_file=True, #if you want to get return period file from RAPID simulation
	    generate_seasonal_averages_file=True,
        generate_seasonal_initialization_file=True, #if you want to get seasonal init file from RAPID simulation
        generate_initialization_file=False, #if you want to generate qinit file from end of RAPID simulation
        use_all_processors=False, #defaults to use all processors available
        um_processors=1, #you can change this number if use_all_processors=False
#        cygwin_bin_location="" #if you are using Windows with Cygwin
    )
