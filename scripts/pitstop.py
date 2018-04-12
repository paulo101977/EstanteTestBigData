import numpy as np
import pandas as pd

# read the Dataframe from races.csv
races = pd.read_csv('races.csv')

# read constructor info
constructors = pd.read_csv('constructorResults.csv')

# read driver info
drivers = pd.read_csv('drivers.csv', encoding="latin1")

#print(constructors)

pitstop = pd.read_csv('pitStops.csv')


df = (
    pd.merge(races, pitstop, on='raceId')
        .groupby([ 'milliseconds'])
        .min()
        .groupby('name')
        .head()[['name', 'year', 'driverId']]
        .reset_index()
)


df = pd.merge(df, drivers , on='driverId')

df['pilot'] = df.apply(lambda x : x['forename'] + ' ' + x['surname'], axis=1)

df = df.sort_values('year', ascending=False)

#rename columns
df = df.rename(
    columns={
        'year': 'Temporada:',
        'milliseconds': 'Pit stop mili:',
        'name': 'Corrida:',
        'pilot': 'Piloto'
    }
)

writer = pd.ExcelWriter('pitstop.xlsx')
racesFromYears.to_excel(writer,'Sheet1')
writer.save()
