
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import squarify

data = {
    'Continent': ['Asia', 'Asia', 'Asia', 'Asia', 'Asia', 'Europe', 'Europe', 'Europe', 'Europe', 'Europe',
                  'Africa', 'Africa', 'Africa', 'Africa', 'Africa', 'Americas', 'Americas', 'Americas', 'Americas',
                  'Americas', 'Oceania', 'Oceania', 'Oceania', 'Oceania', 'Oceania'],
    'Country': ['China', 'India', 'Japan', 'South Korea', 'Indonesia', 'Germany', 'United Kingdom',
                'France', 'Italy', 'Russia', 'Nigeria', 'South Africa', 'Egypt', 'Algeria', 'Morocco',
                'United States', 'Brazil', 'Canada', 'Mexico', 'Argentina', 'Australia', 'New Zealand',
                'Papua New Guinea', 'Fiji', 'Samoa'],
    'Literature Sales (Million USD)': [5432, 3210, 4789, 1987, 1102, 2785, 2598, 2310, 1903, 1289,
                                       678, 540, 490, 310, 250, 7890, 3010, 2230, 1890, 765,
                                       890, 710, 45, 23, 12]
}

df = pd.DataFrame(data)

plt.figure(figsize=(28, 16))
colors = ["#FF6347", "#4682B4", "#32CD32", "#FFD700", "#FF69B4", "#8A2BE2",
          "#DC143C", "#00CED1", "#7FFF00", "#FF4500", "#2E8B57", "#9400D3",
          "#FF1493", "#6495ED", "#B8860B", "#00FA9A", "#FF7F50", "#FFB6C1",
          "#20B2AA", "#8B0000", "#00FF7F", "#D2691E", "#A52A2A", "#40E0D0", "#BA55D3"]

squarify.plot(sizes=df['Literature Sales (Million USD)'], label=df['Country'], color=colors, alpha=0.8)
plt.title('Global Literature Sales by Country (Million USD)', fontsize=24, y=1.05)
plt.axis('off')
plt.show()