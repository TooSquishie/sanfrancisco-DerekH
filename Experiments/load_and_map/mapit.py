import pandas as pd
import folium

df = pd.read_csv("D:\\VSCODEPYTHON\\DataMining\\SFCityFacilities.csv")

print("DF head ---------------------------")
print(df.head())

print("DF info ---------------------------")
print(df.info())

print("DF num nulls ---------------------------")
print(df.isnull().sum)


map = folium.Map(location=[37.7749, -122.4194], zoom_start=12)

for index, row in df.iterrows():
    folium.Marker([row['latitude'], row['longitude']], popup=row['common_name'], icon=folium.Icon(color="green")).add_to(map)
    
map.save("sf_parks_map.html")