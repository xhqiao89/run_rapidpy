from datetime import datetime, timedelta
from RAPIDpy.inflow import run_lsm_rapid_process
#------------------------------------------------------------------------------
#main process
#------------------------------------------------------------------------------
if __name__ == "__main__":
    run_lsm_rapid_process(
        rapid_executable_location='/home/sherry/rapid/run/rapid',
        rapid_io_files_location='/home/sherry/Downloads/hiwat/',
        #lsm_data_location='/home/sherry/Downloads/hiwat/mod_files', #path to folder with LSM data
        lsm_data_location='/home/sherry/Downloads/hiwat/data/merged',
        # model_run_datetime=datetime(2017, 8, 5, 18), # YYYY, MM, DD, HH
        # simulation_start_datetime=timedelta(hours=1),
        # simulation_end_datetime=timedelta(hours=72),
        use_all_processors=False,
        num_processors=1,
	#file_datetime_re_pattern = r'\d{12}',
	#file_datetime_pattern = "%Y%m%d%H%M",
	#file_datetime_re_pattern = r'\d{6}',
        #file_datetime_pattern = "%Y%m",
	#expected_time_step = "3600",
	#convert_one_hour_to_three=False
    )
