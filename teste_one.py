from pathlib import Path
import pandas as pd
cct = pd.read_csv('circuits.csv', encoding='latin1')
drivers = pd.read_csv('drivers.csv', encoding='latin1')
dStands = pd.read_csv('driverStandings.csv', encoding='latin1')
group = dStands[['driverId','points']].groupby('driverId',sort=True).mean()
print(group)
res = group[['points']].apply(lambda x: x.order(ascending=False).head(3))
print(res)
