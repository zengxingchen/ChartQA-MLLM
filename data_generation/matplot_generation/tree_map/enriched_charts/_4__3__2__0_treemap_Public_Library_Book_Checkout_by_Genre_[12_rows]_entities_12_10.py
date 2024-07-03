
import matplotlib.pyplot as plt
import pandas as pd
import squarify

data = {
    'Continent': ['Asia', 'Asia', 'Asia', 'Asia', 'Europe', 'Europe', 'Europe', 'Europe',
                  'Africa', 'Africa', 'Africa', 'North America', 'North America', 'North America',
                  'South America', 'South America', 'South America', 'Oceania', 'Oceania', 'Oceania',
                  'Asia', 'Europe', 'Europe', 'Africa', 'North America', 'South America', 'Oceania',
                  'Asia', 'Europe', 'Africa', 'North America', 'South America', 'Oceania'],
    'Country': ['China', 'India', 'Japan', 'South Korea', 'Germany', 'United Kingdom', 'France', 'Italy',
                'Nigeria', 'South Africa', 'Kenya', 'United States', 'Canada', 'Mexico',
                'Brazil', 'Argentina', 'Chile', 'Australia', 'New Zealand', 'Fiji',
                'Thailand', 'Spain', 'Netherlands', 'Egypt', 'Jamaica', 'Colombia', 'Papua New Guinea',
                'Malaysia', 'Norway', 'Ethiopia', 'Panama', 'Peru', 'Samoa'],
    'Fitness_Expenditure': [30000, 25000, 20000, 15000, 28000, 26000, 23000, 21000,
                            8000, 10000, 7000, 50000, 30000, 20000,
                            15000, 12000, 10000, 25000, 18000, 9000,
                            12000, 22000, 20000, 9000, 7000, 11000, 8000,
                            16000, 24000, 6000, 5000, 9000, 6000]
}

df = pd.DataFrame(data)

plt.figure(figsize=(18, 14))
colors = ['#1E90FF', '#00CED1', '#FFD700', '#FF4500', '#FF6347', '#FF69B4', 
          '#BA55D3', '#8A2BE2', '#7B68EE', '#6A5ACD', '#483D8B', '#2E8B57', 
          '#3CB371', '#20B2AA', '#4682B4', '#5F9EA0', '#6495ED', '#DC143C', 
          '#FF8C00', '#FF1493', '#FF7F50', '#FF6347', '#DDA0DD', '#DA70D6', 
          '#8B0000', '#9932CC', '#FF4500', '#FF69B4', '#BA55D3', '#8A2BE2', 
          '#7B68EE', '#6A5ACD', '#483D8B']
squarify.plot(sizes=df['Fitness_Expenditure'], label=df['Country'], color=colors, alpha=0.8)
plt.title('Fitness Expenditure by Country', fontsize=24, fontweight='bold')
plt.axis('off')

plt.show()