import numpy as np
import pandas as pd

# read the Dataframe from races.csv
races = pd.read_csv('races.csv')

# read the Dataframe from seasons.csv
seasons = pd.read_csv('seasons.csv')

drivers = pd.read_csv('drivers.csv', encoding="latin1")


#read the drivers info
driverStd = pd.read_csv('driverStandings.csv')

# get the last ten years
years = (
    seasons[['year']]
    .sort_values(by='year', ascending=False)
    .head(10)
)


# merge from the designed years
racesFromYears = pd.merge(races, years, on=['year'])

#merge to get the drivers info per race
drivers = pd.merge(driverStd, drivers, on=['driverId']) #[['raceId', 'driverId', 'points']]

drivers['name'] = drivers.apply(lambda x : x['forename'] + ' ' +  x['surname'], axis=1)


# merge drivers and races, sort and get the mean of points
racesFromYears = (
    pd.merge(
        racesFromYears,
        drivers ,
        on=['raceId']
    )
    .groupby(['year','name_y'], as_index=False) ['points']
    .mean()
    .groupby('points')
    .head(20)
    .sort_values(['year', 'points'], ascending=False)
)

#rename columns
racesFromYears = racesFromYears.rename(columns={'year': 'Temporada:', 'points': 'Pontos:', 'name_y': 'Nome:'})


writer = pd.ExcelWriter('racesmedia.xlsx')
racesFromYears.to_excel(writer,'Sheet1')
writer.save()
