
import matplotlib.pyplot as plt

# Data for plotting
months = ["January", "February", "March", "April", "May", "June", 
          "July", "August", "September", "October", "November", "December"]
temperatures = [32, 35, 45, 55, 65, 75, 83, 82, 75, 64, 50, 37]

fig, ax = plt.subplots(figsize=(14, 8))

# Create a horizontal bar chart with custom colors and bar heights
bars = ax.barh(months, temperatures, height=0.6,
               color=['#003f5c', '#2f4b7c', '#665191', '#a05195', '#d45087', '#f95d6a',
                      '#ff7c43', '#ffa600', '#488f31', '#6ba292', '#75bba7', '#ace8d3'])

# Set the chart title and labels
ax.set_title('Average Monthly Temperatures (°F)', fontsize=18)
ax.set_xlabel('Temperature (°F)', fontsize=14)
ax.set_ylabel('Month', fontsize=14)

# Customize the ticks on both axes
ax.xaxis.set_tick_params(labelsize=12)
ax.yaxis.set_tick_params(labelsize=12)

# Add value labels to each bar
for bar in bars:
    width = bar.get_width()
    label_x_pos = width + 1  # Some padding to the right
    ax.text(label_x_pos, bar.get_y() + bar.get_height()/2, f'{width}°F',
            va='center', ha='left', fontsize=12)

plt.tight_layout()
plt.show()