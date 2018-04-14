import numpy as np
import pandas as pd


# read driver info
driversInfo = pd.read_csv('driverStandings.csv')
drivers = pd.read_csv('drivers.csv', encoding="latin1")


results = pd.read_csv('results.csv', encoding="latin1")

# select all podiums
hasPodium = pd.unique(results[results['position'] < 4  ]['driverId'])

hasNotPodium = results[~results['driverId'].isin(hasPodium)]


# get racer points
hasNotPodium = pd.merge(hasNotPodium, driversInfo, on='driverId')


# sum the points and get the higher
hasNotPodium = (
    hasNotPodium
        .groupby(['driverId'])['points_x']
        .sum()
        .reset_index()
        .sort_values('points_x', ascending = False)
        .head(1)
)


# get  the driver info
hasNotPodium = pd.merge(hasNotPodium, drivers, on='driverId')

# create the column Nome
hasNotPodium['name'] = hasNotPodium.apply(
    lambda x: x['forename'] + ' '+ x['surname'].replace('_', '').replace('Ì', 'i'),
    axis = 1
)


# select columns
hasNotPodium = hasNotPodium[['nationality', 'name', 'dob', 'points_x']]

#df = {df.columns[0]:'nationality', df.columns[1]: 'name', df.columns[2]:'dob', df.columns[3]: 'points_x'}

# rename columns
hasNotPodium.columns=['Nacionalidade:' , 'Nome:', 'Nascimento:', 'Total de pontos:']

# save the xlsx file
writer = pd.ExcelWriter('nerver_podium.xlsx')
hasNotPodium.to_excel(writer,'Sheet1')
writer.save()
