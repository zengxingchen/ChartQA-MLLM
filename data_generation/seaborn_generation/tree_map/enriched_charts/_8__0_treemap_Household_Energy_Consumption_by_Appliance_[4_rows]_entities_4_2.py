
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Data from the CSV format above
data = {
    "Sector": ["Gaming", "Gaming", "Gaming", "Streaming", "Streaming", 
               "Streaming", "Music", "Music", "Music", "Movies", "Movies", "Movies"],
    "Entity": ["Nintendo", "Sony Interactive", "Microsoft Xbox", "Netflix", "Disney+", 
               "Amazon Prime Video", "Spotify", "Apple Music", "Amazon Music", 
               "Warner Bros.", "Universal Pictures", "Paramount Pictures"],
    "MarketCap": [75000, 110000, 95000, 250000, 170000, 
                  300000, 55000, 120000, 75000, 85000, 95000, 60000]
}

df = pd.DataFrame(data)

# Create a color palette, mapped to Sector
color_mapper = {
    'Gaming': '#1f77b4',        # Blue
    'Streaming': '#ff7f0e',     # Orange
    'Music': '#2ca02c',         # Green
    'Movies': '#d62728',        # Red
}

colors = [color_mapper[sector] for sector in df['Sector']]

# Create the figure
fig, ax = plt.subplots(1, figsize=(14, 10))

# Create the treemap
squarify.plot(sizes=df['MarketCap'], label=df['Entity'], color=colors, alpha=0.8, text_kwargs={'fontsize':9})

plt.title('Market Capitalization in Entertainment & Leisure', fontsize=16)
plt.axis('off')
plt.show()