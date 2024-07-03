
import matplotlib.pyplot as plt
import pandas as pd
import squarify

data = {
    'Continent': ['North America', 'North America', 'North America', 'Europe', 'Europe', 'Europe', 
                  'Asia', 'Asia', 'Asia', 'South America', 'South America', 'Africa', 
                  'Africa', 'Oceania', 'Oceania', 'Asia', 'Europe', 'Asia', 
                  'North America', 'South America', 'Europe', 'Africa'],
    'Country': ['United States', 'Canada', 'Mexico', 'Germany', 'France', 'United Kingdom', 
                'China', 'Japan', 'India', 'Brazil', 'Argentina', 'Nigeria', 
                'South Africa', 'Australia', 'New Zealand', 'South Korea', 'Italy', 'Indonesia', 
                'Cuba', 'Chile', 'Spain', 'Kenya'],
    'Investment': [2100000, 1500000, 950000, 1750000, 1200000, 1450000, 
                   2500000, 2000000, 1800000, 1100000, 800000, 500000, 
                   650000, 950000, 400000, 1200000, 1100000, 900000, 
                   300000, 400000, 950000, 450000]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 10))
colors = ['#FF6347', '#FF4500', '#FFD700', '#ADFF2F', '#32CD32', '#00FA9A', 
          '#40E0D0', '#1E90FF', '#4169E1', '#8A2BE2', '#9400D3', '#FF69B4', 
          '#FF1493', '#FFB6C1', '#FFA07A', '#CD5C5C', '#DC143C', '#B22222',
          '#DAA520', '#8B4513', '#2F4F4F', '#808080']

squarify.plot(sizes=df['Investment'], label=df['Country'], color=colors, alpha=0.8)
plt.title('Global Investment Distribution by Country and Continent', fontsize=16)
plt.axis('off')

plt.show()