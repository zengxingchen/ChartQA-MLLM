
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Prepare the data
data = {
    'Country': ['USA', 'India', 'China', 'Germany', 'Brazil', 'UK', 'France', 'Japan', 
                'Russia', 'Italy', 'Canada', 'Australia', 'Spain', 'Mexico', 'South Africa',
                'South Korea', 'Netherlands', 'Sweden', 'Norway', 'Denmark', 'Argentina', 
                'Chile', 'New Zealand', 'Switzerland', 'Finland', 'Austria', 'Belgium', 
                'Greece', 'Portugal', 'Turkey'],
    'Average Monthly Clear Nights Per Year': [20.1, 15.7, 18.3, 13.5, 22.4, 9.8, 16.2, 19.7, 14.3, 11.6, 18.9, 
                                               23.1, 17.8, 24.4, 25.2, 12.3, 10.4, 12.9, 14.1, 11.7, 21.0, 23.5, 
                                               22.7, 13.8, 11.2, 12.6, 10.7, 16.8, 17.1, 20.5]
}
df = pd.DataFrame(data)

# Create a color palette, mapped to these values
colors = ['#1E90FF', '#87CEFA', '#00BFFF', '#4682B4', '#5F9EA0', 
          '#6495ED', '#00CED1', '#20B2AA', '#00FA9A', '#7FFF00',
          '#32CD32', '#98FB98', '#ADFF2F', '#FFFF00', '#FFD700',
          '#FFA500', '#FF8C00', '#FF4500', '#DC143C', '#FF6347', 
          '#FF69B4', '#FF1493', '#C71585', '#DB7093', '#FFB6C1',
          '#FF00FF', '#8A2BE2', '#9400D3', '#4B0082', '#6A5ACD']

# Plot
plt.figure(figsize=(30, 16))
squarify.plot(sizes=df['Average Monthly Clear Nights Per Year'], label=df['Country'], color=colors, alpha=0.8)
plt.title('Average Monthly Clear Nights Per Year by Country', fontsize=24, fontweight='bold', pad=20)
plt.axis('off')  # Removes the axes to create a treemap
plt.show()