from datetime import datetime
from RAPIDpy.inflow import run_lsm_rapid_process
#------------------------------------------------------------------------------
#main process
#------------------------------------------------------------------------------
if __name__ == "__main__":
    run_lsm_rapid_process(
        rapid_executable_location='/home/sherry/rapid/run/rapid',
        rapid_io_files_location='/home/sherry/Downloads/lis',
        lsm_data_location='/home/sherry/Downloads/lis/data/201808',
        use_all_processors=False,  #  defaults to use all processors available
        num_processors=1,  # you can change this number if use_all_processors=False
        #path to folder with LSM data
        #simulation_start_datetime=datetime(1980, 1, 1),
        #simulation_end_datetime=datetime(2017, 1, 1),
	#file_datetime_re_pattern = r'\d{12}',
	#file_datetime_pattern = "%Y%m%d%H%M",
	#file_datetime_re_pattern = r'\d{6}',
        #file_datetime_pattern = "%Y%m",
	# expected_time_step = "86400",
	#convert_one_hour_to_three=False
    )
