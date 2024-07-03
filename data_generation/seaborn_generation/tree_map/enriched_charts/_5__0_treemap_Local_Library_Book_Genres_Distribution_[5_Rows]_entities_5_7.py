
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Prepare the data
data = {
    'Country': ['USA', 'India', 'China', 'Germany', 'Brazil', 'UK', 'France', 'Japan', 
                'Russia', 'Italy', 'Canada', 'Australia', 'Spain', 'Mexico', 'South Africa'],
    'Physical Activity Level (%)': [40.1, 35.4, 30.2, 25.8, 20.5, 18.7, 15.9, 14.3, 
                                    12.6, 10.4, 8.5, 7.2, 6.8, 5.4, 3.9]
}
df = pd.DataFrame(data)

# Create a color palette, mapped to these values
colors = ['#FF6347', '#FFA07A', '#20B2AA', '#778899', '#4682B4', 
          '#D2691E', '#B0C4DE', '#8FBC8F', '#00CED1', '#DA70D6',
          '#FF1493', '#FFD700', '#ADFF2F', '#8A2BE2', '#5F9EA0']

# Plot
plt.figure(figsize=(24, 12))
squarify.plot(sizes=df['Physical Activity Level (%)'], label=df['Country'], color=colors, alpha=0.8)
plt.title('Global Physical Activity Levels by Country', fontsize=22, fontweight='bold')
plt.axis('off')  # Removes the axes to create a treemap
plt.show()