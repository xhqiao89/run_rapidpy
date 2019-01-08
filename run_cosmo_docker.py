import sys
import datetime
import os
import shutil
# Linux command for utc YYYYMMDDHHmm: date -u +%Y%m%d%H%m

datetime_format_str = "%Y%m%d%H"
forecast_timestep_size_tdelta = datetime.timedelta(hours=1)
model_run_output_timespan_tdelta = datetime.timedelta(days=7, hours=6)
model_run_interval_tdelta = datetime.timedelta(hours=12)

lsm_source_path = "/home/sherry/Downloads/COSMO/drew_test/all_in_one"
template_path = "/home/sherry/Downloads/COSMO/drew_test/"
target_path = "/home/sherry/Downloads/COSMO/drew_test/run"


def _create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        print("Folder already exists at {}".format(path))


def _copy_lsm(lsm_source_path, target_path, model_dt, symlink=False):
    print("Copying LSM....")
    fn_format = "PLATANC_{model_dt}_{forecast_dt}.nc"

    end_frst_dt = model_dt + model_run_output_timespan_tdelta - forecast_timestep_size_tdelta
    current_frst_dt = model_dt - forecast_timestep_size_tdelta
    while current_frst_dt <= end_frst_dt:
        current_frst_dt += forecast_timestep_size_tdelta
        current_frst_fn = fn_format.format(model_dt=model_dt.strftime(datetime_format_str), forecast_dt=current_frst_dt.strftime(datetime_format_str))

        source_file_path = os.path.join(lsm_source_path, current_frst_fn)
        target_file_path = os.path.join(target_path, current_frst_fn)

        # if symlink:
        #     if not (os.path.islink(target_file_path) and os.path.getsize(source_file_path) == os.path.getsize(target_file_path)):
        #         os.symlink(source_file_path, target_file_path)
        # else:
        if not(os.path.isfile(target_file_path) and os.path.getsize(source_file_path) == os.path.getsize(target_file_path)):
            shutil.copyfile(source_file_path, target_file_path)
            print("Copying to {}".format(target_file_path))
        else:
            print("File already exists at {}".format(target_file_path))


def _find_closest_model_run_dt(dt, search_future=False):
    input_dt = dt
    utc00 = datetime.datetime(year=input_dt.year, month=input_dt.month, day=input_dt.day, hour=0)
    utc12 = datetime.datetime(year=input_dt.year, month=input_dt.month, day=input_dt.day, hour=12)
    if search_future:
        if input_dt > utc12:
            return utc12 + model_run_interval_tdelta
        elif input_dt > utc00:
            return utc12
        else:
            return utc00
    else:
        if input_dt >= utc12:
            return utc12
        else:
            return utc00


def _build_dt_list(model_run_first_dt, model_run_last_dt, interval=model_run_interval_tdelta):
    model_run_dt_list = [model_run_first_dt]
    while model_run_dt_list[-1] < model_run_last_dt:
        model_run_dt_list.append(model_run_dt_list[-1]+model_run_interval_tdelta)
    model_run_dt_list.sort()
    return model_run_dt_list


def prepare_model_run(model_run_start_dt, model_run_end_dt=None):

    model_run_dt_list = []
    if model_run_end_dt:
        model_run_first_dt = _find_closest_model_run_dt(model_run_start_dt, search_future=True)
        model_run_last_dt = _find_closest_model_run_dt(model_run_end_dt)
        model_run_dt_list = _build_dt_list(model_run_first_dt, model_run_last_dt)
    else:
        model_run_dt_list=[_find_closest_model_run_dt(model_run_start_dt)]

    print("Preparing {} runs: {}".format(len(model_run_dt_list), model_run_dt_list))

    for i in range(len(model_run_dt_list)):
        model_run_dt = model_run_dt_list[i]
        print("Preparing Run No{}: {}".format(i, model_run_dt))
        if i == 0:
            previous_model_run_dt = None
        else:
            previous_model_run_dt = model_run_dt_list[i-1]

        # create a parent folder for this run YYYYMMDDHH
        run_folder_name = model_run_dt.strftime(datetime_format_str)
        run_folder_path = os.path.join(target_path, run_folder_name)
        _create_folder(run_folder_path)
        # create "data" folder
        data_folder_path = os.path.join(run_folder_path, "data")
        _create_folder(data_folder_path)
        # create lsm folder
        lsm_folder_name = run_folder_name
        lsm_folder_path = os.path.join(data_folder_path, lsm_folder_name)
        _create_folder(lsm_folder_path)
        # copy lsm
        _copy_lsm(lsm_source_path, lsm_folder_path, model_run_dt)

        # copy input folder
        input_source_path = os.path.join(template_path, "input")
        input_folder_path = os.path.join(run_folder_path, "input")
        if os.path.isdir(input_folder_path):
            import uuid
            os.rename(input_folder_path, input_folder_path + "_" + str(uuid.uuid4())[:6])
        shutil.copytree(input_source_path, input_folder_path)

    return model_run_dt_list


def main():
    #current_utc_dt_str = sys.argv[1]
    #print (current_utc_dt_str)
    #current_utc_dt = datetime.datetime.strptime(current_utc_dt_str, "%Y%m%d%H%M")

    #start_utc_dt = datetime.datetime.utcnow()
    #end_utc_dt = None

    start_utc_dt = datetime.datetime(year=2018, month=8, day=8, hour=0)
    end_utc_dt = datetime.datetime(year=2018, month=8, day=9, hour=0)

    model_run_dt_list = prepare_model_run(start_utc_dt, end_utc_dt)

    from RAPIDpy.inflow import run_lsm_rapid_process

    for model_run_dt in model_run_dt_list:

        model_run_dt_str = model_run_dt.strftime("%Y%m%d%H")
        model_run_root = os.path.join(target_path, model_run_dt_str)
        previous_model_run_dt = model_run_dt - datetime.timedelta(hours=12)

        previous_model_run_dt_str = previous_model_run_dt.strftime("%Y%m%d%H")
        previous_model_run_root = os.path.join(target_path, previous_model_run_dt_str)

        # Run Cosmo
        run_lsm_rapid_process(
            rapid_executable_location='/home/sherry/rapid/run/rapid',
            rapid_io_files_location=model_run_root,
            lsm_data_location=os.path.join(model_run_root, "data", model_run_dt_str),
            use_all_processors=False,  # defaults to use all processors available
            num_processors=1,  # you can change this number if use_all_processors=False
            generate_initialization_file=True,
            timedelta_between_simulations=datetime.timedelta(hours=12),
            initial_flows_file=os.path.join(previous_model_run_root, "qinit.csv"),
            # path to folder with LSM data
            # simulation_start_datetime=datetime(1980, 1, 1),
            # simulation_end_datetime=datetime(2017, 1, 1),
            # file_datetime_re_pattern = r'\d{12}',
            # file_datetime_pattern = "%Y%m%d%H%M",
            # file_datetime_re_pattern = r'\d{6}',
            # file_datetime_pattern = "%Y%m",
            # expected_time_step = "86400",
            # convert_one_hour_to_three=False
        )


    pass


if __name__ == "__main__":

    main()

