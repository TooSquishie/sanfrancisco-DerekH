# Use a correlation heat map and a scatter plot to find any correlations between nearby trees and speed stats

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

roads_trees_df = pd.read_csv("D:\\VSCODEPYTHON\\sf_roads_with_tree_counts.csv")

# Check for missing values
print(roads_trees_df.isnull().sum())

# View basic stats
print(roads_trees_df.describe())

# Unnecessary Columns
roads_trees_df = roads_trees_df.drop(columns=["the_geom", "CNN", "STREETNAME"])

# This caused some issues when trying to change the speed limits that were 0, some speed limits were 0.002 or something like that
roads_trees_df["SpeedLimit"] = roads_trees_df["SpeedLimit"].round().astype(int)

# Change speed limit from 0 to 20 for residential, I did this for speed avg at or above 20
roads_trees_df.loc[(roads_trees_df["SpeedLimit"] == 0) & (roads_trees_df["Speed_avg"] >= 20), "SpeedLimit"] = 25
# Change speed limit from 0 to 15 for narrow alleys, I did this for speed avg below 20
roads_trees_df.loc[(roads_trees_df["SpeedLimit"] == 0) & (roads_trees_df["Speed_avg"] < 15), "SpeedLimit"] = 15

print(roads_trees_df.info())

# Min Max Scaling
scaler = MinMaxScaler()
RD_df_scaled = pd.DataFrame(scaler.fit_transform(roads_trees_df), columns = roads_trees_df.columns)

print(RD_df_scaled.describe())

# Find correlations
correlation_matrix = RD_df_scaled.corr()
print(correlation_matrix["Nearby_Trees"])

# Plot Correlation Matrix
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix")
plt.show()

# Scatterplot of percent of drivers going over the spee limit to the number of nearby trees
plt.figure(figsize=(8, 5))
sns.scatterplot(x=RD_df_scaled["Nearby_Trees"], y=RD_df_scaled["Over_pct"])
plt.xlabel("Number of Nearby Trees")
plt.ylabel("Percentage of Speeding")
plt.title("Nearby Trees vs. Speeding Percentage")
plt.show()

