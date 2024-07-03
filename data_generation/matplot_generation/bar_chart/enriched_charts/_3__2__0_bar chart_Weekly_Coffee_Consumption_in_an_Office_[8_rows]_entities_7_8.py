
import matplotlib.pyplot as plt

# Data for plotting
categories = ["AI Research", "Quantum Computing", "Blockchain", "IoT", "Biotechnology",
              "Cybersecurity", "Augmented Reality", "5G Technology", "Nanotechnology",
              "Renewable Energy", "Autonomous Vehicles", "Robotics"]
values = [95000, 120000, 85000, 65000, 105000, 98000, 72000, 115000, 99000, 135000, 87000, 110000]

fig, ax = plt.subplots(figsize=(14, 8))

# Create a horizontal bar chart with custom colors and bar widths
bars = ax.barh(categories, values, height=0.6,
               color=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6',
                      '#c4e17f', '#76d7c4', '#f7b7a3', '#c9daf8', '#e1a6f7', '#ffd700'])

# Set the chart title and labels
ax.set_title('Budgets for Future Technologies (in $)', fontsize=18)
ax.set_xlabel('Budget (in $)', fontsize=14)
ax.set_ylabel('Technologies', fontsize=14)

# Customize the ticks on both axes
ax.xaxis.set_tick_params(labelsize=12)
ax.yaxis.set_tick_params(labelsize=12)

# Add value labels to each bar
for bar in bars:
    width = bar.get_width()
    label_x_pos = width + 3000  # Some padding to the right
    ax.text(label_x_pos, bar.get_y() + bar.get_height()/2, f'${width}',
            va='center', ha='center', fontsize=12)

plt.tight_layout()
plt.show()