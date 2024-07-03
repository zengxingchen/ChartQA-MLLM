
import matplotlib.pyplot as plt
import pandas as pd
import squarify

data = {
    'Continent': ['Asia', 'Asia', 'Asia', 'Europe', 'Europe', 'Europe', 'Africa', 'Africa', 'Africa',
                  'North America', 'North America', 'North America', 'South America', 'South America',
                  'South America', 'Oceania', 'Oceania', 'Oceania'],
    'Country': ['China', 'India', 'Indonesia', 'Russia', 'Germany', 'United Kingdom', 'Nigeria',
                'Ethiopia', 'Egypt', 'United States', 'Mexico', 'Canada', 'Brazil', 'Colombia',
                'Argentina', 'Australia', 'Papua New Guinea', 'New Zealand'],
    'Mental_Health_Expenditure': [21000, 15000, 3000, 8000, 12000, 14000, 500,
                                  300, 700, 35000, 2500, 11000, 4000, 2000,
                                  2500, 7000, 200, 5000]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 10))
colors = ['#FF5733', '#C70039', '#900C3F', '#581845', '#1A5276', '#1ABC9C',
          '#27AE60', '#D4AC0D', '#F39C12', '#E74C3C', '#8E44AD', '#2980B9',
          '#2ECC71', '#E67E22', '#16A085', '#34495E', '#7D3C98', '#BDC3C7']
squarify.plot(sizes=df['Mental_Health_Expenditure'], label=df['Country'], color=colors, alpha=0.8)
plt.title('Mental Health Expenditure by Country', fontsize=18, fontweight='bold')
plt.axis('off')

plt.show()