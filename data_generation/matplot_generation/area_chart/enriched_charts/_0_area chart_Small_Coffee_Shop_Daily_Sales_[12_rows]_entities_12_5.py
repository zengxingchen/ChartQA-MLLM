
import matplotlib.pyplot as plt
import numpy as np

# Sample data representing average daily temperature by month
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
temperature = [4, 5, 9, 14, 18, 22, 25, 24, 20, 15, 9, 5]

# Convert month strings to numbers for plotting
month_numbers = np.arange(len(months)) + 1

fig, ax = plt.subplots(figsize=(12, 6))  # Change the size of the chart

# Plot area chart
ax.fill_between(month_numbers, temperature, color="#3498db")

# Customize the ticks and labels
ax.set_xticks(month_numbers)
ax.set_xticklabels(months, rotation=45)  # Rotate month labels for better readability
ax.set_yticks(range(0, max(temperature) + 5, 5))
ax.set_yticklabels([f"{temp}°C" for temp in range(0, max(temperature) + 5, 5)])

# Set the title and labels
ax.set_title('Average Daily Temperature by Month', fontsize=16)
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Average Temperature (°C)', fontsize=12)

# Show grid
ax.grid(True, linestyle='--', which='both', color='grey', alpha=0.7)

plt.tight_layout()
plt.show()