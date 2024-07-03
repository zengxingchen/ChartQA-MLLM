
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Prepare the data
data = {
    'Continent': ['Asia', 'Asia', 'Asia', 'Europe', 'Europe', 'Europe', 'Africa', 'Africa', 'Africa',
                  'North America', 'North America', 'North America', 'South America', 'South America',
                  'South America', 'Oceania', 'Oceania', 'Oceania'],
    'Country': ['China', 'India', 'Indonesia', 'Russia', 'Germany', 'United Kingdom', 'Nigeria',
                'Ethiopia', 'Egypt', 'United States', 'Mexico', 'Canada', 'Brazil', 'Colombia',
                'Argentina', 'Australia', 'Papua New Guinea', 'New Zealand'],
    'Population': [1444216107, 1393409038, 276361783, 145912025, 83883596, 68207114, 211400708,
                   120812698, 104258327, 334805269, 130262216, 38388465, 214042665, 51516526,
                   45937624, 25925668, 9264775, 5129293]
}

df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(12, 8))
colors = ['#FFD700', '#FFA500', '#FF8C00', '#F08080', '#CD5C5C', '#DC143C',
          '#9ACD32', '#556B2F', '#006400', '#4682B4', '#4169E1', '#0000FF',
          '#9400D3', '#8A2BE2', '#8B008B', '#C71585', '#DB7093', '#FFC0CB']
squarify.plot(sizes=df['Population'], label=df['Country'], color=colors, alpha=0.7)
plt.title('World Population Distribution by Country and Continent')
plt.axis('off')

plt.show()