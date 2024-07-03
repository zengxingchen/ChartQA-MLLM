
import matplotlib.pyplot as plt

# Data for plotting
categories = ["AI Research", "Quantum Computing", "Blockchain", "IoT", "Biotechnology",
              "Cybersecurity", "Augmented Reality", "5G Technology", "Nanotechnology",
              "Renewable Energy", "Autonomous Vehicles", "Robotics", "Space Exploration",
              "Gene Editing", "VR Gaming", "Wearable Tech"]
values = [95000, 120000, 85000, 65000, 105000, 98000, 72000, 115000, 99000, 135000, 87000, 110000, 145000, 130000, 78000, 91000]

fig, ax = plt.subplots(figsize=(12, 10))

# Create a vertical bar chart with custom colors and bar widths
bars = ax.bar(categories, values, width=0.5,
              color=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6',
                     '#c4e17f', '#76d7c4', '#f7b7a3', '#c9daf8', '#e1a6f7', '#ffd700',
                     '#8a2be2', '#7fffd4', '#d2691e', '#ff4500'])

# Set the chart title and labels
ax.set_title('Investment in Future Technologies (in $)', fontsize=18)
ax.set_ylabel('Budget (in $)', fontsize=14)
ax.set_xlabel('Technologies', fontsize=14)

# Customize the ticks on both axes
ax.xaxis.set_tick_params(labelsize=12)
ax.yaxis.set_tick_params(labelsize=12)

# Set y-axis limits to truncate
ax.set_ylim(60000, 160000)

# Add value labels to each bar
for bar in bars:
    height = bar.get_height()
    label_y_pos = height + 3000  # Some padding above the bar
    ax.text(bar.get_x() + bar.get_width()/2, label_y_pos, f'${height}',
            va='center', ha='center', fontsize=12)

plt.xticks(rotation=90)
plt.tight_layout()
plt.show()