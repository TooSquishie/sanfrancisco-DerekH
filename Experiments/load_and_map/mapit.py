# The purpose of this script is to test loading 
# a CSV, mild pre-processing, mapping, and then clustering.

import pandas as pd
import folium
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("D:\\VSCODEPYTHON\\DataMining\\SFCityFacilities.csv")

print("DF head ---------------------------")
print(df.head())

print("DF info ---------------------------")
print(df.info())

# print("DF num nulls ---------------------------")
# print(df.isnull().sum)

# Remove some points outside of the SF area.
# I was considering just removing them if they aren't in the SF are by lat and long
# but since I wanted to experiment I used the inner quartile range as bounds
Q1_long = df['longitude'].quantile(0.25)
Q3_long = df['longitude'].quantile(0.75)
IQR_long = Q3_long - Q1_long

lower_bound_long = Q1_long - 1.5 * IQR_long
upper_bound_long = Q3_long + 1.5 * IQR_long

df_filtered = df[(df['longitude'] >= lower_bound_long) & (df['longitude'] <= upper_bound_long)]

Q1_lat = df['latitude'].quantile(0.25)
Q3_lat = df['latitude'].quantile(0.75)
IQR_lat = Q3_lat - Q1_lat

lower_bound_lat = Q1_lat - 1.5 * IQR_lat
upper_bound_lat = Q3_lat + 1.5 * IQR_lat

df_filtered = df[(df['latitude'] >= lower_bound_lat) & (df['latitude'] <= upper_bound_lat)]

map = folium.Map(location=[37.7749, -122.4194], zoom_start=12)

for index, row in df_filtered.iterrows():
    folium.Marker([row['latitude'], row['longitude']], popup=row['common_name'], icon=folium.Icon(color="green")).add_to(map)

# Open this file to view an interactive map of all the locations (besides outliers)    
map.save("sf_parks_map.html")

coords = df_filtered[['latitude', 'longitude']].dropna()

# Use K means clustering for the locations
kmeans = KMeans(n_clusters=5, random_state=42)
coords['cluster'] = kmeans.fit_predict(coords)

# Plot clusters
plt.figure(figsize=(10, 6))
sns.scatterplot(x=coords['longitude'], y=coords['latitude'], hue=coords['cluster'], palette='viridis')
plt.title("Clustering of SF Parks")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()