
import matplotlib.pyplot as plt
import pandas as pd
import squarify  # you might need to install squarify with pip

# Provided data
chart_data = [
    {'Platform': 'TikTok', 'Percentage of Teen Users': 25},
    {'Platform': 'Instagram', 'Percentage of Teen Users': 22},
    {'Platform': 'Snapchat', 'Percentage of Teen Users': 20},
    {'Platform': 'YouTube', 'Percentage of Teen Users': 14},
    {'Platform': 'Facebook', 'Percentage of Teen Users': 6},
    {'Platform': 'Twitter', 'Percentage of Teen Users': 4},
    {'Platform': 'Pinterest', 'Percentage of Teen Users': 3},
    {'Platform': 'Reddit', 'Percentage of Teen Users': 2},
    {'Platform': 'WhatsApp', 'Percentage of Teen Users': 1}
]

# Create a DataFrame
df = pd.DataFrame(chart_data)

# Create sizes for the treemap
sizes = df['Percentage of Teen Users'].values.tolist()
labels = df.apply(lambda x: f"{x['Platform']} ({x['Percentage of Teen Users']}%)", axis=1)

# Create a color palette
cmap = plt.cm.Spectral
mini=min(sizes)
maxi=max(sizes)
norm = plt.Normalize(vmin=mini, vmax=maxi)
colors = [cmap(norm(value)) for value in sizes]

# Create a figure
plt.figure(figsize=(12, 8))

# Create a treemap
squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.6)

# Remove axis
plt.axis('off')

# Add title
plt.title('Percentage of Teen Users by Platform')

# Show plot
plt.show()