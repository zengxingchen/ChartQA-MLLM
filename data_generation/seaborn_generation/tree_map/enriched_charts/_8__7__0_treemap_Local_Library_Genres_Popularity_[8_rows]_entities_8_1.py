
import pandas as pd
import matplotlib.pyplot as plt
import squarify

data = {
    'Country': ['France', 'Spain', 'United States', 'China', 'Italy', 'Turkey', 'Mexico', 'Germany', 'Thailand', 'United Kingdom', 'Japan', 'Australia', 'Canada', 'Greece', 'Russia', 'Portugal', 'Netherlands', 'Malaysia', 'Brazil', 'India', 'South Korea', 'Indonesia', 'South Africa', 'New Zealand', 'Vietnam', 'Switzerland', 'Saudi Arabia', 'Argentina', 'Sweden', 'United Arab Emirates'],
    'Annual Tourists (Millions)': [89.4, 83.7, 79.3, 65.7, 62.1, 51.2, 45.0, 39.6, 38.2, 36.3, 31.9, 29.5, 28.9, 27.2, 25.7, 22.8, 20.2, 19.4, 18.1, 17.2, 16.3, 15.1, 14.7, 14.3, 13.5, 12.9, 12.2, 11.4, 10.8, 10.4]
}

df = pd.DataFrame(data)

plt.figure(figsize=(20, 12))
colors = [
    "#FF5733", "#33FF57", "#3357FF", "#FF33A6", "#A633FF", "#33FFA6", "#FFA633", "#5733FF", "#FF5733", "#33FF57", 
    "#3357FF", "#FF33A6", "#A633FF", "#33FFA6", "#FFA633", "#5733FF", "#FF5733", "#33FF57", "#3357FF", "#FF33A6",
    "#A633FF", "#33FFA6", "#FFA633", "#5733FF", "#FF5733", "#33FF57", "#3357FF", "#FF33A6", "#A633FF", "#33FFA6"
]

squarify.plot(sizes=df['Annual Tourists (Millions)'], label=df['Country'], color=colors, alpha=0.8)
plt.title('Annual Tourist Arrivals by Country (Millions)', fontsize=24, pad=20)
plt.axis('off')
plt.show()