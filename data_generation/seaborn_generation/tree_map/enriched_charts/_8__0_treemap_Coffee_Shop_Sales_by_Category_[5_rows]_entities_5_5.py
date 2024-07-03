
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import squarify

# Create a DataFrame with the data
data = {
    'Country': ['France', 'Spain', 'USA', 'China', 'Italy', 'Turkey', 'Mexico', 'Thailand', 'Germany', 'United Kingdom', 'Japan', 'Austria', 'Greece', 'Russia', 'Australia', 'India', 'Brazil', 'South Korea', 'Netherlands', 'Switzerland', 'South Africa'],
    'Visitors': [9000, 8500, 8000, 7800, 7600, 7000, 6500, 6400, 6300, 6200, 6100, 5900, 5800, 5700, 5600, 5500, 5400, 5300, 5200, 5100, 5000],
    'Continent': ['Europe', 'Europe', 'North America', 'Asia', 'Europe', 'Europe', 'North America', 'Asia', 'Europe', 'Europe', 'Asia', 'Europe', 'Europe', 'Europe', 'Oceania', 'Asia', 'South America', 'Asia', 'Europe', 'Europe', 'Africa']
}
df = pd.DataFrame(data)

# Plot parameters
plt.figure(figsize=(14, 10))
cmap = ['#FF5733', '#33FF57', '#3357FF', '#FF33A5', '#33FFD5', '#A533FF', '#FF9633', '#57FF33', '#FF3333', '#3385FF', '#FF8C33', '#33FF9A', '#FF3378', '#FF3333', '#A8FF33', '#33FF57', '#5733FF', '#FF33F5', '#33FF8A', '#33F5FF', '#FF3333']

# Create a treemap
squarify.plot(sizes=df['Visitors'], label=df['Country'], color=cmap, alpha=0.8)

plt.title('Top Tourist Destinations by Number of Visitors', fontsize=18)
plt.axis('off')

plt.show()