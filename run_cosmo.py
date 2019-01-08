from datetime import datetime,timedelta
from RAPIDpy.inflow import run_lsm_rapid_process

#------------------------------------------------------------------------------
#main process
#------------------------------------------------------------------------------
if __name__ == "__main__":
    start_date = datetime(2018, 8, 8)
    end_date = datetime(2018, 8, 8)
    days = (end_date - start_date).days
    for day in range(days+1):
        current_date = start_date + timedelta(days=day)
        date_str00 = current_date.strftime("%Y%m%d") + "00"
        date_str12 = current_date.strftime("%Y%m%d") + "12"
        date_str = [date_str00, date_str12]
        for i in range(2):
            print "Running for date:"+date_str[i]
            run_lsm_rapid_process(
                rapid_executable_location='/home/sherry/rapid/run/rapid',
                rapid_io_files_location='/home/sherry/Downloads/COSMO',
                lsm_data_location='/home/sherry/Downloads/COSMO/data/{date_str}'.format(date_str=date_str[i]),
                use_all_processors=False,  # defaults to use all processors available
                num_processors=1,  # you can change this number if use_all_processors=False
                generate_initialization_file=True,
                timedelta_between_simulations=timedelta(hours=12),
                # initial_flows_file='/home/sherry/Downloads/COSMO/input/LP_rapid/qinit_cosmo.csv',
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
