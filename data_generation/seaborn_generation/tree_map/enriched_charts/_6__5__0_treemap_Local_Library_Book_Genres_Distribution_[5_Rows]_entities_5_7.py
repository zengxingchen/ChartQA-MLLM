
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
    'Books Read Per Year': [12.1, 10.3, 8.7, 15.2, 7.8, 11.4, 9.9, 14.1, 6.3, 5.7, 13.0, 
                            9.5, 8.3, 4.9, 3.7, 10.8, 7.5, 12.4, 11.1, 10.6, 6.0, 5.4, 8.9, 
                            11.8, 13.7, 9.1, 7.3, 4.5, 6.7, 5.0]
}
df = pd.DataFrame(data)

# Create a color palette, mapped to these values
colors = ['#FF6347', '#FFA07A', '#20B2AA', '#778899', '#4682B4', 
          '#D2691E', '#B0C4DE', '#8FBC8F', '#00CED1', '#DA70D6',
          '#FF1493', '#FFD700', '#ADFF2F', '#8A2BE2', '#5F9EA0',
          '#FF4500', '#98FB98', '#8A2BE2', '#FF00FF', '#00FA9A', 
          '#DDA0DD', '#FFB6C1', '#87CEFA', '#7FFF00', '#8B008B',
          '#00FF7F', '#DC143C', '#FFDEAD', '#6495ED', '#A0522D']

# Plot
plt.figure(figsize=(28, 14))
squarify.plot(sizes=df['Books Read Per Year'], label=df['Country'], color=colors, alpha=0.8)
plt.title('Books Read Per Year by Country', fontsize=22, fontweight='bold')
plt.axis('off')  # Removes the axes to create a treemap
plt.show()