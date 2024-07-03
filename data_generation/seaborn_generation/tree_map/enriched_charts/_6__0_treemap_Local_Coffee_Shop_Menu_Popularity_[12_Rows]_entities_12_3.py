
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Data
data = {
    'Category': ['Streaming Services', 'Concerts', 'Music Instruments', 'Albums Sold', 'Digital Downloads',
                 'Music Licensing', 'Music Merchandise', 'Music Publishing', 'Music Production', 'Music Education'],
    'Amount': [120.5, 85.3, 75.2, 55.6, 50.1, 30.7, 25.4, 20.9, 15.6, 10.8]
}

df = pd.DataFrame(data)

# Color scheme picked to be distinct and visually appealing
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#6A5ACD', 
          '#FF69B4', '#8A2BE2', '#20B2AA', '#FF7F50', '#00CED1']

# Plotting the Treemap
plt.figure(figsize=(18, 10))  # Adjusted width and height
squarify.plot(sizes=df['Amount'], label=df['Category'], color=colors, alpha=0.8)
plt.title('Revenue Distribution in the Music Industry (in Millions USD)', fontsize=16)
plt.axis('off')
plt.show()