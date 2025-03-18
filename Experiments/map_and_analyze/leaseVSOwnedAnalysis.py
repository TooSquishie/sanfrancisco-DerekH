# Combine both experiments to create a sample task

import pandas as pd
import folium
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("D:\\VSCODEPYTHON\\DataMining\\Assn1\\SFCityFacilities.csv")

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

# only 4 non-nulls
df_filtered.drop(columns=["city_tenants"])

print(df.describe())
print(df['owned_leased'].value_counts())

map = folium.Map(location=[37.7749, -122.4194], zoom_start=12)

for index, row in df_filtered.iterrows():
    folium.Marker([row['latitude'], row['longitude']],
    popup=row['common_name'],
    icon=folium.Icon(color="blue" if row['owned_leased'] == "Own" else "red")
    ).add_to(map)

# Open this file to view an interactive map of all the locations (besides outliers)    
map.save("sf_parks_map_OL.html")

sns.countplot(data=df_filtered, x="owned_leased", palette="pastel")
plt.title("Owned vs Leased Facilities in SF")
plt.show()

# For outlier removed data
coords = df_filtered[['latitude', 'longitude']].dropna()

# Use K means clustering for the locations with removed outliers
kmeans = KMeans(n_clusters=5, random_state=42)
coords['cluster'] = kmeans.fit_predict(coords)

# Plot clusters after outlier removal
plt.figure(figsize=(10, 6))
sns.scatterplot(x=coords['longitude'], y=coords['latitude'], hue=coords['cluster'], palette='viridis')
plt.title("Clustering of SF Parks")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()