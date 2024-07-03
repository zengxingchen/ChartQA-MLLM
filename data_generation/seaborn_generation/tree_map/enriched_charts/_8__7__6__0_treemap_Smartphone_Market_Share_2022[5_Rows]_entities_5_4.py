
import matplotlib.pyplot as plt
import pandas as pd
import squarify  # treemap library

# Prepare the data
data = {
    'Topic': ['Sports & Fitness'] * 30,
    'Subtopic': ['Football', 'Basketball', 'Cricket', 'Tennis', 'Swimming', 'Cycling', 'Running', 'Golf', 'Baseball', 
                 'Hockey', 'Boxing', 'Rugby', 'Martial Arts', 'Skiing', 'Surfing', 'Table Tennis', 'Volleyball', 
                 'Weightlifting', 'Skateboarding', 'Rock Climbing', 'Rowing', 'Fencing', 'Archery', 'Dance', 'Yoga', 
                 'Gymnastics', 'Pilates', 'Parkour', 'Mountaineering', 'Paragliding'],
    'Value': [9500, 9200, 8900, 8600, 8300, 8000, 7700, 7400, 7100, 6800, 6500, 6200, 5900, 5600, 5300, 5000, 4700, 
              4400, 4100, 3800, 3500, 3200, 2900, 2600, 2300, 2000, 1700, 1400, 1100, 800]
}

df = pd.DataFrame(data)

# Create a color list
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6','#c4e17f','#76d7c4','#ff6f61','#c49c94',
          '#f7b6d2','#aec6cf','#ffb6c1','#ff7f50','#d4a017','#b3b3b3','#ffbdbd','#c7eae5','#ff7373','#3f91ff',
          '#ffcc5c','#c6e2ff','#ff9933','#779ecb','#e6e6fa','#ff1493','#ff6347','#7cfc00','#ffff00','#8a2be2']

# Create a figure with a defined size
plt.figure(figsize=(24, 16))

# Plot
squarify.plot(sizes=df['Value'], label=df['Subtopic'], color=colors, alpha=0.8)
plt.title('Popular Sports and Fitness Activities', fontsize=30, y=1.05)

# Remove axes
plt.axis('off')

# Show the plot
plt.show()