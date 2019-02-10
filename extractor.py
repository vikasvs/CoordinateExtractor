from geopy.geocoders import Nominatim
import pandas as pd
import sys

#replace csv_file with your own file
csv_file = 'city_list.csv'
df = pd.read_csv(csv_file)
geolocator = Nominatim()

df['Address'] = df['CITY']+', '+df['PROVINCE'] 
df['Coordinates'] = df['Address'].apply(geolocator.geocode)

df['Latitude'] = df['Coordinates'].apply(lambda x: x.latitude if x != None else None)
df['Longitude'] = df['Coordinates'].apply(lambda x: x.longitude if x != None else None)

dfnew  = df[['CITY', 'PROVINCE','Latitude','Longitude']]
print(dfnew)