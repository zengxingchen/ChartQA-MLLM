
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Data
data = {
    'Country': ['France', 'Spain', 'United States', 'China', 'Italy', 
                'Turkey', 'Mexico', 'Germany', 'Thailand', 'United Kingdom', 
                'Japan', 'Australia', 'Greece', 'Malaysia', 'Russia', 
                'Canada', 'Saudi Arabia', 'Netherlands', 'Switzerland', 'South Korea',
                'Brazil', 'Austria', 'Singapore', 'India', 'Portugal'],
    'Arrivals (Millions)': [89.4, 82.8, 79.6, 65.7, 62.1, 
                            51.2, 45.0, 38.9, 38.2, 36.3, 
                            31.8, 31.3, 30.1, 27.7, 24.4, 
                            22.1, 20.3, 19.0, 17.4, 17.2,
                            16.6, 15.1, 14.7, 14.4, 13.7]
}

df = pd.DataFrame(data)

# Color scheme
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#8A2BE2',
          '#FF4500', '#ADFF2F', '#DA70D6', '#7FFFD4', '#D2691E',
          '#00FA9A', '#8B4513', '#6495ED', '#DC143C', '#00CED1',
          '#FF69B4', '#A52A2A', '#5F9EA0', '#9932CC', '#FFB6C1',
          '#FF8C00', '#20B2AA', '#FF00FF', '#7CFC00', '#FF1493']

# Plotting the Treemap
plt.figure(figsize=(18, 10))  # Change width and height reasonably
squarify.plot(sizes=df['Arrivals (Millions)'], label=df['Country'], color=colors, alpha=0.8)
plt.title('International Tourist Arrivals by Country - 2021 (Millions)', fontsize=18, fontweight='bold')
plt.axis('off')
plt.show()