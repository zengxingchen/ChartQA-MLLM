
import matplotlib.pyplot as plt
import pandas as pd
import squarify

data = {
    'Continent': ['North America', 'North America', 'North America', 'Europe', 'Europe', 'Europe', 
                  'Europe', 'Asia', 'Asia', 'Asia', 'Asia', 'Asia', 'South America', 'South America', 
                  'Africa', 'Africa', 'Oceania', 'Oceania', 'North America', 'South America', 
                  'Europe', 'Africa', 'Asia', 'Asia'],
    'Country': ['United States', 'Canada', 'Mexico', 'Germany', 'France', 'United Kingdom', 
                'Italy', 'China', 'Japan', 'India', 'Thailand', 'Malaysia', 'Brazil', 'Argentina', 
                'South Africa', 'Egypt', 'Australia', 'New Zealand', 'Cuba', 'Chile', 
                'Spain', 'Kenya', 'Indonesia', 'South Korea'],
    'Visitors': [35000000, 22000000, 18000000, 27000000, 32000000, 30000000, 
                 25000000, 45000000, 30000000, 29000000, 27000000, 25000000, 
                 18000000, 12000000, 13000000, 15000000, 18000000, 9000000, 
                 5000000, 8000000, 29000000, 7000000, 25000000, 20000000]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 12))
colors = ['#FF6347', '#FF7F50', '#FFD700', '#ADFF2F', '#32CD32', '#00FA9A', 
          '#40E0D0', '#1E90FF', '#4169E1', '#8A2BE2', '#9400D3', '#FF69B4', 
          '#FF1493', '#FFB6C1', '#FFA07A', '#CD5C5C', '#DC143C', '#B22222', 
          '#DAA520', '#8B4513', '#2F4F4F', '#808080', '#4682B4', '#8B0000']

squarify.plot(sizes=df['Visitors'], label=df['Country'], color=colors, alpha=0.8)
plt.title('Top Tourist Destinations by Country and Continent', fontsize=18, pad=20)
plt.axis('off')

plt.show()