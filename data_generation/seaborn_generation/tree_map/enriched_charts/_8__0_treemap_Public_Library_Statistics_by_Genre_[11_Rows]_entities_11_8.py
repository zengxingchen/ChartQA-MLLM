
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import squarify

# Create a data frame with updated data
df = pd.DataFrame({
    'region': ['Asia', 'Asia', 'Asia', 'Asia', 'Europe', 'Europe', 'Europe', 'Europe', 'North America', 'North America', 'North America', 'South America', 'South America', 'South America', 'Africa', 'Africa', 'Africa', 'Oceania', 'Oceania', 'Oceania'],
    'sub_region': ['Japan', 'China', 'Thailand', 'India', 'France', 'Italy', 'Germany', 'Spain', 'USA', 'Canada', 'Mexico', 'Brazil', 'Argentina', 'Chile', 'South Africa', 'Egypt', 'Kenya', 'Australia', 'New Zealand', 'Fiji'],
    'value': [1500, 1300, 900, 1100, 1200, 1400, 1000, 900, 1600, 1100, 1000, 800, 700, 600, 500, 400, 450, 1300, 900, 400]
})

# Create a new color list
colors = ['#FF6347', '#FFD700', '#ADFF2F', '#20B2AA', '#FF69B4', '#8A2BE2', '#5F9EA0', '#D2691E', '#FF7F50', '#6495ED', '#DC143C', '#00FFFF', '#008B8B', '#B8860B', '#A9A9A9', '#006400', '#8B008B', '#556B2F', '#FF8C00', '#9932CC']

# Plot
plt.figure(figsize=(22, 12))
squarify.plot(sizes=df['value'], label=df['sub_region'], color=colors, alpha=.8)
plt.title('Popular Travel Destinations by Region', fontsize=25)
plt.axis('off')
plt.show()