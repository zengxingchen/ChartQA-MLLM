
import matplotlib.pyplot as plt
import pandas as pd
import squarify

data = {
    'Continent': ['Asia', 'Asia', 'Asia', 'Asia', 'Asia', 
                  'Europe', 'Europe', 'Europe', 'Europe',
                  'Africa', 'Africa', 'Africa',
                  'North America', 'North America', 'North America',
                  'South America', 'South America', 'South America',
                  'Oceania', 'Oceania', 'Oceania'],
    'Country': ['China', 'India', 'Japan', 'South Korea', 'Indonesia', 
                'Germany', 'United Kingdom', 'France', 'Russia', 
                'Nigeria', 'South Africa', 'Egypt',
                'United States', 'Canada', 'Mexico', 
                'Brazil', 'Argentina', 'Colombia',
                'Australia', 'New Zealand', 'Papua New Guinea'],
    'Technology_Investment': [32000, 22000, 15000, 14000, 5000, 
                              25000, 20000, 18000, 10000, 
                              800, 1500, 1200,
                              45000, 20000, 3000, 
                              6000, 2500, 2000,
                              8000, 3500, 700]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 12))
colors = ['#FF5733', '#C70039', '#900C3F', '#581845', '#1A5276', '#1ABC9C',
          '#27AE60', '#D4AC0D', '#F39C12', '#E74C3C', '#8E44AD', '#2980B9',
          '#2ECC71', '#E67E22', '#16A085', '#34495E', '#7D3C98', '#BDC3C7',
          '#F4D03F', '#1F618D', '#A569BD']
squarify.plot(sizes=df['Technology_Investment'], label=df['Country'], color=colors, alpha=0.8)
plt.title('Investment in Future Technologies by Country', fontsize=18, fontweight='bold')
plt.axis('off')

plt.show()