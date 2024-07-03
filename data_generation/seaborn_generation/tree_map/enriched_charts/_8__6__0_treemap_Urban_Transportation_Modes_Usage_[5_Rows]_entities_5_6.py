
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import squarify

# Create the dataframe
df = pd.DataFrame({
    'Category': ['Cinema', 'Music Streaming', 'Video Games', 'Books', 'TV Shows', 'Concerts', 'Live Sports', 'Theme Parks',
                 'eSports', 'Podcasts', 'Theater', 'Board Games', 'Art Exhibitions', 'Digital Art', 'VR Experiences',
                 'Merchandising', 'Social Media', 'Online Courses'],
    'Revenue': [500, 450, 600, 350, 400, 300, 550, 380, 320, 280, 260, 150, 220, 270, 330, 290, 310, 370]
})

# Custom colors for the treemap
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c4e17f', '#ff6666', '#ffb347', '#aec6cf',
          '#779ecb', '#ff6f61', '#ffcc5c', '#b19cd9', '#ff9671', '#c5e384', '#ffcc99', '#77dd77']

# Create a figure and a set of subplots
plt.figure(figsize=(20, 12))

# Using squarify to plot the treemap
squarify.plot(sizes=df['Revenue'], label=df['Category'], color=colors, alpha=0.8)

plt.title("Revenue Distribution in Entertainment & Leisure", fontsize=24, fontweight='bold')
plt.axis('off')  # Disable the axis

plt.show()