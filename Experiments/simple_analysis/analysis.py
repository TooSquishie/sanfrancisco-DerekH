import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("D:\\VSCODEPYTHON\\DataMining\\Assn1\\SFCityFacilities.csv")

ownership_counts = df['owned_leased'].value_counts()

ownership_counts.plot(kind='bar', title="Leased vs City-Owned Parks", color=['blue', 'orange'])
plt.xlabel("Ownership Type")
plt.ylabel("Count")
plt.show()

leased_facilities = df[df['owned_leased'] == 'Lease']

print(leased_facilities)