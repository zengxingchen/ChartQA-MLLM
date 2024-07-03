
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import squarify  # pip install squarify (algorithm for treemap)

# Create the dataframe
df = pd.DataFrame({
    'Field': ['Movies', 'Music', 'Video Games', 'Books', 'TV Shows', 'Live Performances', 'Theme Parks', 
              'Streaming Services', 'Concerts', 'Museums', 'Art Exhibitions', 'Festivals', 'Amusement Parks', 
              'Zoos and Aquariums', 'Sports Events', 'Comics and Graphic Novels', 'Board Games', 'Circuses', 
              'Escape Rooms', 'Virtual Reality Experiences'],
    'Funding': [320, 280, 270, 260, 250, 240, 230, 220, 210, 200, 190, 180, 170, 160, 150, 140, 130, 120, 110, 100]
})

# Custom colors for the treemap
colors = ['#FF4500', '#FFD700', '#00FA9A', '#1E90FF', '#FF69B4', '#8A2BE2', '#00CED1', '#FF6347', '#ADFF2F', '#FF1493',
          '#7FFF00', '#7B68EE', '#FF7F50', '#4682B4', '#DDA0DD', '#32CD32', '#FF00FF', '#EE82EE', '#00FF7F', '#6A5ACD']

# Create a figure and a set of subplots
plt.figure(figsize=(20, 12))

# Using squarify to plot the treemap
squarify.plot(sizes=df['Funding'], label=df['Field'], color=colors, alpha=0.8)

plt.title("Distribution of Funding in Entertainment & Leisure", fontsize=24, fontweight='bold', y=1.05)
plt.axis('off')  # Disable the axis

plt.show()