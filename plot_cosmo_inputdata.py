
import xarray
from netCDF4 import Dataset
import numpy as np
import datetime
import matplotlib.pyplot as plt

## cosmo
nc_files_path = "/home/sherry/Downloads/COSMO/data/2018081312/*.nc"

nc = xarray.open_mfdataset(nc_files_path)

# values = nc.RUNOFF_G[:,267,227].values
# print values

t = nc.time.values
print t

# value0 = values[0]

# values_new = np.diff(values)
#
# values_new_new = np.insert(values_new,0,0.00)
#
# print values_new



plt.plot(t)

# plt.plot(t,s)
plt.xlabel('time')
plt.ylabel('RUNOFF_G(mm)')
plt.show()

# print np.isnan(ts)
# ts[np.isnan(ts)]= -9999

nc.close()

pass
