
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import squarify

data = {
    'Continent': ['Asia', 'Asia', 'Asia', 'Asia', 'Asia', 'Europe', 'Europe', 'Europe', 'Europe', 'Europe',
                  'Africa', 'Africa', 'Africa', 'Africa', 'Africa', 'Americas', 'Americas', 'Americas', 'Americas',
                  'Americas', 'Oceania', 'Oceania', 'Oceania', 'Oceania', 'Oceania', 'Asia', 'Europe', 'Africa', 'Americas', 'Oceania'],
    'Country': ['China', 'India', 'Japan', 'South Korea', 'Indonesia', 'Germany', 'United Kingdom',
                'France', 'Italy', 'Russia', 'Nigeria', 'South Africa', 'Egypt', 'Algeria', 'Morocco',
                'United States', 'Brazil', 'Canada', 'Mexico', 'Argentina', 'Australia', 'New Zealand',
                'Papua New Guinea', 'Fiji', 'Samoa', 'Saudi Arabia', 'Spain', 'Kenya', 'Chile', 'Micronesia'],
    'Research_Spending': [300000, 120000, 250000, 150000, 80000, 180000, 160000, 140000, 110000, 90000,
                          60000, 70000, 50000, 40000, 30000, 350000, 200000, 220000, 130000, 100000,
                          175000, 95000, 40000, 30000, 20000, 105000, 120000, 45000, 95000, 15000]
}

df = pd.DataFrame(data)

plt.figure(figsize=(24, 14))
colors = ["#FF6347", "#FFD700", "#4682B4", "#8A2BE2", "#5F9EA0", "#D2691E",
          "#FF7F50", "#6495ED", "#DC143C", "#00FFFF", "#00008B", "#B8860B",
          "#A9A9A9", "#006400", "#BDB76B", "#556B2F", "#FF8C00", "#9932CC",
          "#8B0000", "#E9967A", "#8FBC8F", "#483D8B", "#2F4F4F", "#00CED1",
          "#9400D3", "#FF1493", "#1E90FF", "#228B22", "#FF00FF", "#FFD700"]

squarify.plot(sizes=df['Research_Spending'], label=df['Country'], color=colors, alpha=0.8)
plt.title('Research Spending by Country and Continent', fontsize=26, y=1.02)
plt.axis('off')
plt.show()