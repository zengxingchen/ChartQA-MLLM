
import matplotlib.pyplot as plt
import matplotlib as mpl
import squarify

# Table data
data = [
    {'Park Section': 'North Garden', 'Activity': 'Yoga Classes', 'Monthly Visitors': 120},
    {'Park Section': 'North Garden', 'Activity': 'Tai Chi', 'Monthly Visitors': 90},
    {'Park Section': 'Central Grounds', 'Activity': 'Jogging', 'Monthly Visitors': 400},
    {'Park Section': 'Central Grounds', 'Activity': 'Cycling', 'Monthly Visitors': 250},
    {'Park Section': 'East Meadow', 'Activity': 'Picnics', 'Monthly Visitors': 300},
    {'Park Section': 'East Meadow', 'Activity': 'Kite Flying', 'Monthly Visitors': 150},
    {'Park Section': 'West Field', 'Activity': 'Soccer Games', 'Monthly Visitors': 220},
    {'Park Section': 'West Field', 'Activity': 'Ultimate Frisbee', 'Monthly Visitors': 180},
    {'Park Section': 'Playground Area', 'Activity': 'Children Playtime', 'Monthly Visitors': 500},
    {'Park Section': 'Playground Area', 'Activity': 'Outdoor Concerts', 'Monthly Visitors': 350},
    {'Park Section': 'Lake Side', 'Activity': 'Fishing', 'Monthly Visitors': 80},
    {'Park Section': 'Lake Side', 'Activity': 'Boat Rentals', 'Monthly Visitors': 120}
]

# Extract 'Monthly Visitors' as sizes and Activities as labels
sizes = [item['Monthly Visitors'] for item in data]
labels = [f"{item['Activity']} ({item['Monthly Visitors']})" for item in data]
colors = [plt.cm.Spectral(i / float(len(labels))) for i in range(len(labels))]  # Diversify colors

# Create a figure
plt.figure(figsize=(12, 8))

# Create a treemap with squarify
ax = squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.8)

# Remove the axes
plt.axis('off')

# Set the title of the treemap
plt.title('Park Activities Treemap', fontsize=18)

# Colorbar creation
# Create a color map for the colorbar
cmap = mpl.cm.Spectral
# Create a mappable object with the same colormap as the data
norm = mpl.colors.Normalize(vmin=min(sizes), vmax=max(sizes))
# Create the colorbar
cbar = plt.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=cmap), orientation='vertical', pad=0.02)
cbar.set_label('Number of Monthly Visitors')

# Display the plot
plt.show()