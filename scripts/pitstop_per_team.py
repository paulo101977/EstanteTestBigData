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
        .groupby(['name_y','year', 'raceId','name_x'])
        .agg({'milliseconds': np.min})
        #.reset_index()
        .drop_duplicates()
        .reset_index()
)


df = df.sort_values('year', ascending=False)

df = df[['name_y' , 'year', 'milliseconds', 'name_x']]


df = df.rename(
    columns={
        'name_y': 'Equipe:',
        'milliseconds': 'Pit stop mili:',
        'year': 'Temporada:',
        'name_x': 'Circuito:'
    }
)

#print(df)

writer = pd.ExcelWriter('pitstop_per_team.xlsx')
df.to_excel(writer,'Sheet1')
writer.save()
