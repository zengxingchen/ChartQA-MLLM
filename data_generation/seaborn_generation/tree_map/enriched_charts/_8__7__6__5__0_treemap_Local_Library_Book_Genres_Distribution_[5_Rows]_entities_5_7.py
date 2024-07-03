
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Prepare the data
data = {
    'Country': ['USA', 'Canada', 'UK', 'Germany', 'France', 'Japan', 'Australia', 'China', 
                'India', 'Brazil', 'South Africa', 'Mexico', 'South Korea', 'Italy', 'Spain', 
                'Netherlands', 'Sweden', 'Norway', 'Denmark', 'Finland', 'Austria', 'Switzerland', 
                'Belgium', 'New Zealand', 'Chile', 'Argentina', 'Portugal', 'Greece', 'Turkey', 'Russia'],
    'Average Annual Mental Health Expenditure (USD)': [5000, 4200, 3900, 4700, 3800, 3500, 4100, 2500, 1200, 
                                                       1800, 1600, 1400, 3200, 3000, 2700, 4400, 4500, 4600, 
                                                       4300, 4100, 3600, 4800, 3400, 4000, 2200, 2000, 3100, 
                                                       2800, 2300, 1900]
}
df = pd.DataFrame(data)

# Create a color palette, mapped to these values
colors = ['#4B0082', '#9400D3', '#8A2BE2', '#FF00FF', '#FF69B4', 
          '#DB7093', '#C71585', '#FF1493', '#FF6347', '#DC143C',
          '#FF4500', '#FF8C00', '#FFA500', '#FFD700', '#FFFF00',
          '#ADFF2F', '#98FB98', '#32CD32', '#7FFF00', '#00FA9A',
          '#20B2AA', '#00CED1', '#6495ED', '#5F9EA0', '#4682B4',
          '#00BFFF', '#87CEFA', '#1E90FF', '#6A5ACD', '#4B0082']

# Plot
plt.figure(figsize=(28, 18))
squarify.plot(sizes=df['Average Annual Mental Health Expenditure (USD)'], label=df['Country'], color=colors, alpha=0.8)
plt.title('Average Annual Mental Health Expenditure by Country (USD)', fontsize=26, fontweight='bold', pad=20)
plt.axis('off')  # Removes the axes to create a treemap
plt.show()