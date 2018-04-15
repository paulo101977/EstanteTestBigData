import numpy as np
import pandas as pd

# read the Dataframe from races.csv
races = pd.read_csv('races.csv')

# read constructor info
constructor = pd.read_csv('constructors.csv')
cons_result = pd.read_csv('constructorResults.csv')
constructor = pd.merge(constructor, cons_result, on='constructorId')

# read driver info
drivers = pd.read_csv('drivers.csv', encoding="latin1")


pitstop = pd.read_csv('pitStops.csv')


#merge with constructor info
pitstop = pd.merge(pitstop, constructor, on='raceId')


#print(pitstop)

# get race info
df = pd.merge(races, pitstop, on='raceId')

#print(df)


df = (
    df
        .groupby([ 'milliseconds'])
        .min()
        .groupby('year')
        .head(1)[['name_x', 'year', 'driverId', 'name_y']]
        .reset_index()
)


# get racers info (name)
df = pd.merge(df, drivers , on='driverId')

# pilot name
df['pilot'] = df.apply(lambda x : x['forename'] + ' ' + x['surname'], axis=1)

#print(df)

df = df.sort_values('year', ascending=False)

df = df[['year', 'milliseconds', 'name_x', 'pilot', 'name_y']]



#rename columns
df = df.rename(
    columns={
        'year': 'Temporada:',
        'milliseconds': 'Pit stop mili:',
        'name_x': 'Corrida:',
        'pilot': 'Piloto:',
        'name_y': 'Equipe:'
    }
)

writer = pd.ExcelWriter('pitstop_season.xlsx')
df.to_excel(writer,'Sheet1')
writer.save()
