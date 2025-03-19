# Improved version of whatnottodo.py to find the number trees around each road point the export the csv to work on.
# O(N + M) N = num roads (~600) and M = num trees (~700k).

import pandas as pd
from shapely.wkt import loads
import folium
from scipy.spatial import cKDTree
import numpy as np

# Read tree and roads SF data
trees_df = pd.read_csv("D:\\VSCODEPYTHON\\DataMining\\Assn1\\Submission\\Street_Tree_List.csv")
roads_df_uncleaned = pd.read_csv("D:\\VSCODEPYTHON\\DataMining\\Assn1\\Submission\\San_Francisco_Speed_Limit_Compliance.csv")

# Remove any trees from before 2008 since the speeding data is from 2004-2009 and trees planted after 2008 wouldn't exist or be big enough
trees_df["PlantDate"] = pd.to_datetime(trees_df["PlantDate"], format="%m/%d/%Y %I:%M:%S %p", errors='coerce')
trees_df = trees_df[trees_df["PlantDate"] < "2008-01-01"]

# Check for duplicates
roads_df = roads_df_uncleaned.drop_duplicates(subset=['SpeedLimit', 'STREETNAME', 'Speed_avg'], keep='first').copy()

trees_df = trees_df.dropna(subset=["Latitude", "Longitude"])
tree_coords = trees_df[["Latitude", "Longitude"]].to_numpy()

# Map for viewing
map = folium.Map(location=[37.7749, -122.4194], zoom_start=12)

# For nearest group lookup
tree_kdtree = cKDTree(tree_coords)

# 70 meter search radius converted to degrees
SEARCH_RADIUS = 70 / 111_000

road_coords = []
road_indices = []

# Get the center for every road segment
# *Sometime curves make the center go off the road!
for index, row in roads_df.iterrows():
    try:
        print(index)
        linestring = loads(row["the_geom"])
        centroid = linestring.centroid
        
        centroid_lat = centroid.y
        centroid_long = centroid.x
        
        road_coords.append([centroid_lat, centroid_long])
        road_indices.append(index)
        
        popup_text = f"""
        <b>Street:</b> {row['STREETNAME']}<br>
        <b>Speed Limit:</b> {row['SpeedLimit']} mph<br>
        <b>Avg Speed:</b> {row['Speed_avg']} mph<br>
        <b>Over Speed %:</b> {row['Over_pct']}%
        """
        # Add marker for the center
        folium.Marker([centroid_lat, centroid_long], popup=folium.Popup(popup_text, max_width=300), icon=folium.Icon(color="red")).add_to(map)
    except Exception as e:
        print(f"Error processing row {index}: {e}")   
        
        
road_coords = np.array(road_coords)

# https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.KDTree.query_ball_point.html
nearby_tree_indices = tree_kdtree.query_ball_point(road_coords, SEARCH_RADIUS)

# Mark all the nearby trees
for road_idx, tree_idxs in zip(road_indices, nearby_tree_indices):
    for tree_idx in tree_idxs:
        tree = trees_df.iloc[tree_idx]
        tree_lat = tree["Latitude"]
        tree_long = tree["Longitude"]
        
        tree_popup = f"""
                    <b>Species:</b> {tree['qSpecies']}<br>
                    <b>Planted:</b> {tree['PlantDate'].date()}<br>
                    <b>DBH (Diameter):</b> {tree['DBH']} inches
                    """
        
        folium.CircleMarker(
            location=[tree_lat, tree_long],
            radius=4, color="blue", fill=True, fill_color="blue",
            fill_opacity=0.6, popup=folium.Popup(tree_popup, max_width=250)
        ).add_to(map)
                    
map.save("road_centroid_test_quick.html") 

tree_counts = [len(tree_idxs) for tree_idxs in nearby_tree_indices]

# Add tree count to 
roads_df.loc[road_indices, "Nearby_Trees"] = tree_counts

roads_df.to_csv("sf_roads_with_tree_counts.csv", index=False)