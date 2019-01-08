from netCDF4 import Dataset
import numpy as np
import datetime
import matplotlib.pyplot as plt
import xarray

## hiwat
# nc_file_path = "/home/sherry/Downloads/hiwat/output/nepal_highres/m3_riv_bas_hiwat_hiwat_grid_1hr_20180620to20180624.nc"
# nc_file_path = "/home/sherry/Downloads/hiwat/output/nepal_highres/Qout_hiwat_hiwat_grid_1hr_20180715to20180717.nc"

## lis
# nc_file_path = "/home/sherry/Downloads/lis/output/nepal_highres/Qout_nasa_lis_24hr_2017060100to2017060700.nc"

## cosmo
nc_file_path = "/home/sherry/Downloads/COSMO/output/LP_rapid/Qout_COSMO_cosmo_grid_1hr_20180624to20180701.nc"
# nc_file_path = "/home/sherry/Downloads/COSMO/output/LP_rapid/m3_riv_bas_COSMO_cosmo_grid_1hr_20180615to20180622.nc"

## era
#nc_file_path = "/home/sherry/Downloads/ecmwf/output/nepal_highres/Qout_erai_t511_24hr_2014040100to2014043000.nc"

f = Dataset(nc_file_path, "r")

t = f.variables["time"][:]
t_datetime = [datetime.datetime.utcfromtimestamp(e) for e in t]
rivid = f.variables["rivid"][:]


for n in np.arange(1, 200, 40):
    # plt.plot(t_datetime, f.variables["m3_riv"][:, n])
    plt.plot(t_datetime, f.variables["Qout"][:, n])

# plt.plot(t,s)
plt.xlabel('time (s)')
plt.ylabel('outflow(m3/s)')
plt.show()

# with xarray.open_dataset(nc_file_path) as qds:
#     streamflow_values = qds.isel(time=-1).Qout.values
#     rivid = qds.rivid.values
#
# for n in np.arange(1, 9950, 1):
#     print (rivid[n],streamflow_values[n])

# print np.isnan(ts)
# ts[np.isnan(ts)]= -9999

f.close()

