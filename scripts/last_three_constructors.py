import numpy as np
import pandas as pd

# read the Dataframe from races.csv
races = pd.read_csv('races.csv')

# read constructor info
constructors = pd.read_csv('constructorResults.csv')

# merge and group into
df = pd.merge(races, constructors, on=['raceId']).groupby(['raceId', 'points']).head()

df['count'] = df[df['points'] > 0 ].groupby(['raceId'])['points'].count()

df = df[df['count'] == 3]

df = df[['name', 'year', 'date', 'count']]

df = df.drop_duplicates(subset=['name', 'year'])

df = df.rename(columns={'name': 'Pista/Corrida:', 'year': 'Ano:', 'date': 'Data:', 'count': 'Quantidade de pontuantes:'})

# write to file
writer = pd.ExcelWriter('count_constructor_limit_3.xlsx')

df.to_excel(writer,'Sheet1')

writer.save()
