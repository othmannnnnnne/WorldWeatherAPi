import pandas as pd
from wwo_hist import retrieve_hist_data
import os


frequency=24
start_date = '01-AUG-2008'
end_date = '01-FEB-2009'
api_key = '5a5a055b8f36462bb2c132317212503'
location_list = ['Casablanca']

hist_weather_data = retrieve_hist_data(api_key,
                                location_list,
                                start_date,
                                end_date,
                                frequency,
                                location_label = False,
                                export_csv = True,
                                store_df = True)
