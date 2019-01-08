import xarray
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt

seasonal_data_file= '/home/sherry/Downloads/cosmoapp/brazil-highres/seasonal_averages_erai_t511_24hr_19800101to20141231.nc'

with xarray.open_dataset(seasonal_data_file) as seasonal_nc:
    seasonal_data = seasonal_nc.sel(rivid=180906)
    print("1111111111111111111111111111111111")
    print(seasonal_data)
    base_date = dt.datetime(2017, 1, 1)
    day_of_year = [base_date + dt.timedelta(days=ii)
                   for ii in range(seasonal_data.dims['day_of_year'])]
    print("222222222222222222222222222222222222")
    print(day_of_year)
    season_avg = seasonal_data.average_flow.values
    season_std = seasonal_data.std_dev_flow.values

    season_avg[season_avg < 0] = 0

    avg_plus_std = season_avg + season_std
    avg_min_std = season_avg - season_std

    avg_plus_std[avg_plus_std < 0] = 0
    avg_min_std[avg_min_std < 0] = 0

    plt.plot(day_of_year, season_avg)
    plt.xlabel('time (s)')
    plt.ylabel('outflow(m3/s)')
    plt.show()