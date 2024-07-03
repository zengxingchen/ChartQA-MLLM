
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
    'Concerts Attended Per Year': [25, 18, 22, 30, 16, 28, 21, 26, 15, 12, 29, 
                            19, 14, 10, 8, 23, 20, 24, 17, 11, 13, 9, 27, 
                            31, 32, 34, 7, 6, 5, 4]
}
df = pd.DataFrame(data)

# Create a color palette, mapped to these values
colors = ['#1E90FF', '#00FA9A', '#FFD700', '#FF4500', '#8A2BE2', 
          '#DC143C', '#00CED1', '#FF6347', '#20B2AA', '#4682B4', 
          '#D2691E', '#B0C4DE', '#8FBC8F', '#DA70D6', '#FF1493',
          '#FFD700', '#ADFF2F', '#8A2BE2', '#5F9EA0', '#FF4500', 
          '#98FB98', '#8A2BE2', '#FF00FF', '#00FA9A', '#DDA0DD', 
          '#FFB6C1', '#87CEFA', '#7FFF00', '#8B008B', '#00FF7F']

# Plot
plt.figure(figsize=(24, 12))
squarify.plot(sizes=df['Concerts Attended Per Year'], label=df['Country'], color=colors, alpha=0.8)
plt.title('Concerts Attended Per Year by Country', fontsize=24, fontweight='bold')
plt.axis('off')  # Removes the axes to create a treemap
plt.show()