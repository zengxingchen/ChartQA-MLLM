
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Data
data = {
    'Category': ['Streaming Services', 'Concerts', 'Music Instruments', 'Albums Sold', 'Digital Downloads',
                 'Music Licensing', 'Music Merchandise', 'Music Publishing', 'Music Production', 'Music Education',
                 'Fitness Equipment', 'Gym Memberships', 'Personal Training', 'Sports Events', 'Sports Apparel',
                 'Supplements', 'Sports Coaching', 'Outdoor Activities', 'Fitness Apps', 'Healthy Food'],
    'Amount': [120.5, 85.3, 75.2, 55.6, 50.1, 30.7, 25.4, 20.9, 15.6, 10.8,
               90.2, 75.4, 60.3, 45.7, 40.2, 35.9, 28.4, 22.6, 18.1, 12.3]
}

df = pd.DataFrame(data)

# Color scheme picked to be distinct and visually appealing
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#6A5ACD', 
          '#FF69B4', '#8A2BE2', '#20B2AA', '#FF7F50', '#00CED1',
          '#FF4500', '#1E90FF', '#3CB371', '#FFD700', '#7B68EE',
          '#DB7093', '#9370DB', '#40E0D0', '#FF6347', '#00CED1']

# Plotting the Treemap
plt.figure(figsize=(20, 12))  # Adjusted width and height
squarify.plot(sizes=df['Amount'], label=df['Category'], color=colors, alpha=0.8)
plt.title('Revenue Distribution in the Fitness Industry (in Millions USD)', fontsize=18)
plt.axis('off')
plt.show()