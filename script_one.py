import numpy as np
import pandas as pd

# read the Dataframe from races.csv
races = pd.read_csv('races.csv')

# read the Dataframe from seasons.csv
seasons = pd.read_csv('seasons.csv')


#read the drivers info
drivers = pd.read_csv('driverStandings.csv')

# get the last ten years
years = seasons[['year']].sort_values(by='year', ascending=False).head(10)

# convert to numpy array
arr = np.array(years['year'])

# search into races for the column year in years np array and find the raceId
raceIds = np.array(races.loc[races['year'].isin(arr)]['raceId'])

# print the races id
# print(raceIds)

driver_info_summarized = drivers.loc[drivers['raceId'].isin(raceIds)].groupby(['points']).mean()

print(driver_info_summarized)
