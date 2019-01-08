import numpy as np
from netCDF4 import Dataset


# u8_arr = np.array([[1, 0], [5, 6], [10, 12]])
#
# a0 = u8_arr[0]
# print a0
#
# a=np.diff(u8_arr, axis=0)
# a_new = np.insert(a,0,a0,axis=0)
# print a_new


def netcdf_diff(nc_input_path):

    with Dataset(nc_input_path, "a") as f:
        inflow = f.variables["m3_riv"][:]
        inflow_0 = inflow[0]
        print inflow_0

        inflow_diff = np.diff(inflow, axis=0)
        inflow_diff_new = np.insert(inflow_diff,0,inflow_0,axis=0)
        f.variables["m3_riv"][:] = inflow_diff_new


nc_input_path = "/home/sherry/Downloads/COSMO/output/LP_rapid/m3_riv_bas_COSMO_cosmo_grid_1hr_20180615to20180622.nc"
netcdf_diff(nc_input_path)