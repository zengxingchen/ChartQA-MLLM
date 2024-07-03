
import matplotlib.pyplot as plt

# Data for plotting
manufacturers = ['Samsung', 'Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Other']
market_shares = [20.5, 18.2, 15.6, 12.7, 8.8, 7.4, 16.8]
units_sold = [300, 270, 230, 190, 130, 110, 250]
average_prices = [250, 750, 200, 150, 220, 240, 180]

# Create a figure with specified width and height
fig, ax = plt.subplots(figsize=(12, 8))

# Bubble sizes (optional: scale sizes to not overlap much)
sizes = [units * 10 for units in units_sold]

# Bubble colors with specific hex color codes
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#A633FF', '#FF8833', '#33FFD5']

# Plot each data point
for (manufacturer, share, units, price, size, color) in zip(manufacturers, market_shares, units_sold, average_prices, sizes, colors):
    ax.scatter(share, price, s=size, label=manufacturer, alpha=0.6, edgecolors='w', color=color)

# Titles and labels
plt.title('Global Smartphone Market Share by Manufacturer')
plt.xlabel('Market Share (%)')
plt.ylabel('Average Price ($)')

# Legend
# Optional: sort legend labels by order of appearance
handles, labels = ax.get_legend_handles_labels()
hl = sorted(zip(handles, labels), key=lambda x: x[1])
handles2, labels2 = zip(*hl)
ax.legend(handles2, labels2, loc="upper right", title="Manufacturers")

# Show plot
plt.show()