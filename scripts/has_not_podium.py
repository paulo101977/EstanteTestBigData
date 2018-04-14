import numpy as np
import pandas as pd

# read the Dataframe from races.csv
#races = pd.read_csv('races.csv')

# read constructor info
#constructor = pd.read_csv('constructors.csv')
#cons_result = pd.read_csv('constructorResults.csv')
#constructor = pd.merge(constructor, cons_result, on='constructorId')


# read driver info
driversInfo = pd.read_csv('driverStandings.csv')
drivers = pd.read_csv('drivers.csv', encoding="latin1")


results = pd.read_csv('results.csv', encoding="latin1")

# select all podiums
hasPodium = pd.unique(results[results['rank'] < 4  ].groupby('driverId')['driverId'].head())

hasNotPodium = results[~results['driverId'].isin(hasPodium)]


#drop
print(hasNotPodium)


# get racer points
hasNotPodium = pd.merge(hasNotPodium, driversInfo, on='driverId')


hasNotPodium = ( 
    hasNotPodium
        .groupby(['driverId'])
        .sum()
        .reset_index()
        .sort_values('points', ascending = False) 
        .head(1)
)



print(hasNotPodium)
#hasNotPodium = pb.merge(driver)

hasNotPodium = pd.merge(hasNotPodium, drivers, on='driverId')

print(hasNotPodium)
