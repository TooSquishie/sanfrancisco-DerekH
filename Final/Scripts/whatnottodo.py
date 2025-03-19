# Script to map all centroid points of a road segment for the SF Speed Limit Complace Data.
# This is obsolete and take about 10 minutes to run to due to ineffiently going through the tree data for every road.
# O(N * M) N = num roads (~600) and M = num trees (~700k).

import pandas as pd
from shapely.geometry import LineString
from shapely.wkt import loads
import folium
from geopy.distance import geodesic

trees_df = pd.read_csv("D:\\VSCODEPYTHON\\DataMining\\Assn1\\Submission\\Street_Tree_List.csv")
roads_df_uncleaned = pd.read_csv("D:\\VSCODEPYTHON\\DataMining\\Assn1\\Submission\\San_Francisco_Speed_Limit_Compliance.csv")

trees_df["PlantDate"] = pd.to_datetime(trees_df["PlantDate"], format="%m/%d/%Y %I:%M:%S %p", errors='coerce')
trees_df = trees_df[trees_df["PlantDate"] < "2008-01-01"]

roads_df = roads_df_uncleaned.drop_duplicates(subset=['SpeedLimit', 'STREETNAME', 'Speed_avg'], keep='first')

map = folium.Map(location=[37.7749, -122.4194], zoom_start=12)

SEARCH_RADIUS = 50

for index, row in roads_df.iterrows():
    try:
        print(index)
        linestring = loads(row["the_geom"])
        centroid = linestring.centroid
        
        centroid_lat = centroid.y
        centroid_long = centroid.x
        
        popup_text = f"""
        <b>Street:</b> {row['STREETNAME']}<br>
        <b>Speed Limit:</b> {row['SpeedLimit']} mph<br>
        <b>Avg Speed:</b> {row['Speed_avg']} mph<br>
        <b>Over Speed %:</b> {row['Over_pct']}%
        """
        
        folium.Marker([centroid_lat, centroid_long], popup=popup_text, icon=folium.Icon(color="red")).add_to(map)
        
        for _, tree in trees_df.iterrows():
            tree_lat, tree_long = tree["Latitude"], tree["Longitude"]
            if pd.notna(tree_lat) and pd.notna(tree_long):
                distance = geodesic((centroid_lat, centroid_long), (tree_lat, tree_long)).meters
                
                if distance <= SEARCH_RADIUS:
                    tree_popup = f"""
                    <b>Species:</b> {tree['qSpecies']}<br>
                    <b>Planted:</b> {tree['PlantDate'].date()}<br>
                    <b>DBH (Diameter):</b> {tree['DBH']} inches
                    """
                    folium.CircleMarker(
                        location=[tree_lat, tree_long],
                        radius=4, color="blue", fill=True, fill_color="green",
                        fill_opacity=0.6, popup=folium.Popup(tree_popup, max_width=250)
                    ).add_to(map)
    except Exception as e:
        print(f"Error processing row {index}: {e}")   
        
map.save("road_centroid_test.html") 