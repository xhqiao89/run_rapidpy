# -*- coding: utf-8 -*-
from spt_compute import run_ecmwf_forecast_process
#------------------------------------------------------------------------------
#main process
#------------------------------------------------------------------------------
if __name__ == "__main__":
    run_ecmwf_forecast_process(
        rapid_executable_location='/home/sherry/rapid/run/rapid',
        rapid_io_files_location='/home/sherry/Downloads/ECMWF/rapid-io',
        ecmwf_forecast_location ="/home/sherry/Downloads/ECMWF/ecmwf",
        # era_interim_data_location="/home/sherry/Downloads/ECMWF/era_interim_watershed",
        subprocess_log_directory='/home/sherry/Downloads/ECMWF/subprocess_logs',
        main_log_directory='/home/sherry/Downloads/ECMWF/logs',
        data_store_url='',
        data_store_api_key='',
        data_store_owner_org='',
        app_instance_id='',
        sync_rapid_input_with_ckan=False,
        download_ecmwf=True,
        ftp_host="ftp.ecmwf.int",
        ftp_login="safer",
        ftp_passwd="neo2008",
        ftp_directory="runofftest2",
        date_string="20181015.00",
        region="S.america",
        upload_output_to_ckan=False,
        initialize_flows=False,
        create_warning_points=False,
        # warning_flow_threshold=60,
        delete_output_when_done=False,
        mp_mode='multiprocess',
        mp_execute_directory='/home/sherry/Downloads/ECMWF/mp_execute',
    )