
import matplotlib.pyplot as plt
import pandas as pd
import squarify

data = {
    'Continent': ['Asia', 'Asia', 'Asia', 'Asia', 'Europe', 'Europe', 'Europe', 'Europe', 
                  'Africa', 'Africa', 'Africa', 'North America', 'North America', 'North America', 
                  'South America', 'South America', 'South America', 'Oceania', 'Oceania', 'Oceania'],
    'Country': ['China', 'India', 'Japan', 'South Korea', 'Germany', 'United Kingdom', 'France', 'Italy', 
                'Nigeria', 'South Africa', 'Kenya', 'United States', 'Canada', 'Mexico', 
                'Brazil', 'Argentina', 'Chile', 'Australia', 'New Zealand', 'Fiji'],
    'Education_Expenditure': [25000, 18000, 15000, 10000, 22000, 20000, 18000, 16000, 
                              5000, 7000, 4000, 40000, 25000, 15000, 12000, 8000, 7000, 
                              20000, 12000, 5000]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 12))
colors = ['#4B0082', '#800080', '#FF00FF', '#EE82EE', '#DDA0DD', '#BA55D3', 
          '#8A2BE2', '#9400D3', '#9932CC', '#8B008B', '#6A5ACD', '#483D8B', 
          '#7B68EE', '#9370DB', '#8FBC8F', '#66CDAA', '#48D1CC', '#20B2AA', 
          '#5F9EA0', '#008B8B']
squarify.plot(sizes=df['Education_Expenditure'], label=df['Country'], color=colors, alpha=0.8)
plt.title('Education Expenditure by Country', fontsize=20, fontweight='bold')
plt.axis('off')

plt.show()