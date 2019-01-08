from datetime import datetime
from RAPIDpy.inflow import run_lsm_rapid_process
#------------------------------------------------------------------------------
#main process
#------------------------------------------------------------------------------
if __name__ == "__main__":
    run_lsm_rapid_process(
        rapid_executable_location='/home/sherry/rapid/run/rapid',
        rapid_io_files_location='/home/sherry/Downloads/ECMWF/rapid-io',
        lsm_data_location='/home/sherry/Downloads/ECMWF/ecmwf/data', #path to folder with LSM data
        generate_rapid_namelist_file=True, #if you want to run RAPID manually later
        run_rapid_simulation=True, #if you want to run RAPID after generating inflow file
        generate_return_periods_file=False, #if you want to get return period file from RAPID simulation
	    generate_seasonal_averages_file=False,
        generate_seasonal_initialization_file=False, #if you want to get seasonal init file from RAPID simulation
        generate_initialization_file=False, #if you want to generate qinit file from end of RAPID simulation
        use_all_processors=True, #defaults to use all processors available
        # num_processors=1, #you can change this number if use_all_processors=False
#        cygwin_bin_location="" #if you are using Windows with Cygwin
    )
