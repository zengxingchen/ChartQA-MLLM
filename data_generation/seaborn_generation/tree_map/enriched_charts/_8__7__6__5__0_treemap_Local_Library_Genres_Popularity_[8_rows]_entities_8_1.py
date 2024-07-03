
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import squarify

data = {
    'Region': ['North America', 'North America', 'North America', 'South America', 'South America', 
               'Europe', 'Europe', 'Europe', 'Europe', 'Europe', 'Europe', 'Europe', 
               'Asia', 'Asia', 'Asia', 'Asia', 'Asia', 
               'Africa', 'Africa', 'Africa', 'Africa', 
               'Oceania', 'Oceania', 'Oceania', 'Oceania'],
    'Country': ['United States', 'Canada', 'Mexico', 'Brazil', 'Argentina', 
                'Germany', 'United Kingdom', 'France', 'Italy', 'Spain', 'Sweden', 'Netherlands', 
                'China', 'India', 'Japan', 'South Korea', 'Indonesia', 
                'Nigeria', 'South Africa', 'Kenya', 'Egypt', 
                'Australia', 'New Zealand', 'Fiji', 'Papua New Guinea'],
    'Healthcare_Spending': [380000, 200000, 120000, 180000, 90000, 
                            220000, 200000, 180000, 150000, 130000, 110000, 120000, 
                            300000, 150000, 250000, 170000, 100000, 
                            80000, 70000, 50000, 40000, 
                            150000, 80000, 30000, 20000]
}

df = pd.DataFrame(data)

plt.figure(figsize=(28, 16))
colors = ["#FF6347", "#FFD700", "#4682B4", "#8A2BE2", "#5F9EA0", "#D2691E",
          "#FF7F50", "#6495ED", "#DC143C", "#00FFFF", "#00008B", "#B8860B",
          "#A9A9A9", "#006400", "#BDB76B", "#556B2F", "#FF8C00", "#9932CC",
          "#8B0000", "#E9967A", "#8FBC8F", "#483D8B", "#2F4F4F", "#00CED1"]

squarify.plot(sizes=df['Healthcare_Spending'], label=df['Country'], color=colors, alpha=0.8)
plt.title('Healthcare Spending by Country and Region', fontsize=28, y=1.05)
plt.axis('off')
plt.show()