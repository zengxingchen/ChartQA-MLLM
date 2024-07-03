
import matplotlib.pyplot as plt
import pandas as pd
import squarify  # treemap library

# Prepare the data
data = {
    'Category': ['Sports', 'Sports', 'Sports', 'Sports', 'Sports', 
                 'Fitness', 'Fitness', 'Fitness', 'Fitness', 'Fitness',
                 'Art', 'Art', 'Art', 'Art', 'Art',
                 'Music', 'Music', 'Music', 'Music', 'Music',
                 'Education', 'Education', 'Education', 'Education', 'Education',
                 'Health', 'Health', 'Health', 'Health', 'Health'],
    'Subcategory': ['Football', 'Basketball', 'Tennis', 'Golf', 'Swimming',
                    'Gym', 'Yoga', 'Pilates', 'CrossFit', 'Running',
                    'Painting', 'Sculpture', 'Digital Art', 'Photography', 'Crafts',
                    'Classical', 'Rock', 'Jazz', 'Pop', 'Hip-hop',
                    'Primary', 'Secondary', 'Tertiary', 'Vocational', 'Online',
                    'Mental Health', 'Physical Health', 'Nutrition', 'Fitness', 'Wellness'],
    'Value': [1800, 1700, 900, 950, 850, 
              1200, 1100, 950, 800, 850,
              1300, 1150, 1050, 1100, 950,
              1000, 900, 800, 850, 750,
              700, 650, 600, 550, 500,
              1400, 1350, 1200, 1150, 1100]
}

df = pd.DataFrame(data)

# Create a color list
colors = ['#FF6347', '#FFD700', '#ADFF2F', '#20B2AA', '#FF69B4', 
          '#BA55D3', '#87CEEB', '#4682B4', '#32CD32', '#FFDAB9', 
          '#9370DB', '#8A2BE2', '#5F9EA0', '#7FFF00', '#00CED1', 
          '#FF4500', '#DA70D6', '#EEE8AA', '#98FB98', '#AFEEEE',
          '#DB7093', '#FF1493', '#7B68EE', '#00BFFF', '#8FBC8F',
          '#E9967A', '#DDA0DD', '#F08080', '#48D1CC', '#C71585']

# Create a figure with a defined size
plt.figure(figsize=(16, 12))

# Plot
squarify.plot(sizes=df['Value'], label=df['Subcategory'], color=colors, alpha=0.8)
plt.title('Value by Subcategory in Sports, Fitness, Art, Music, Education, and Health', fontsize=20, pad=20)

# Remove axes
plt.axis('off')

# Show the plot
plt.show()