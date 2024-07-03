
import matplotlib.pyplot as plt
import pandas as pd
import squarify

data = {
    'Continent': ['Asia', 'Asia', 'Asia', 'Europe', 'Europe', 'Europe', 'Africa', 'Africa', 'Africa',
                  'North America', 'North America', 'North America', 'South America', 'South America',
                  'South America', 'Oceania', 'Oceania', 'Oceania'],
    'Country': ['China', 'India', 'Japan', 'Germany', 'United Kingdom', 'France', 'Nigeria',
                'South Africa', 'Egypt', 'United States', 'Canada', 'Mexico', 'Brazil', 'Argentina',
                'Colombia', 'Australia', 'New Zealand', 'Fiji'],
    'GDP (in billion USD)': [14342, 2869, 5055, 3846, 2827, 2716, 448,
                             351, 302, 21433, 1647, 1260, 2055, 449,
                             323, 1393, 211, 5]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 10))
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b',
          '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#aec7e8', '#ffbb78',
          '#98df8a', '#ff9896', '#c5b0d5', '#c49c94', '#f7b6d2', '#c7c7c7']
squarify.plot(sizes=df['GDP (in billion USD)'], label=df['Country'], color=colors, alpha=0.7)
plt.title('Global GDP Distribution by Country and Continent')
plt.axis('off')

plt.show()