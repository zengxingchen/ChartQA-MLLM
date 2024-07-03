
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
average_temperature = [2.1, 3.3, 6.8, 10.9, 15.2, 20.0, 22.4, 21.8, 17.3, 12.2, 7.1, 3.8]

# Create horizontal bar chart
fig, ax = plt.subplots(figsize=(12, 8))

bars = ax.barh(months, average_temperature, height=0.5, color=['#FF5733', '#FF8D1A', '#FFC300', '#DAF7A6', '#33FF57', '#1AFF8D', '#33FFF6', '#1ACBFF', '#335CFF', '#8333FF', '#FF33C1', '#FF336A'])

# Customizing the plot
ax.set_title('Monthly Average Temperature', fontsize=20, pad=20)
ax.set_xlabel('Average Temperature (°C)', fontsize=16)
ax.set_ylabel('Month', fontsize=16)
ax.set_xlim(0, 25)

# Set bar labels to show the temperature values
for bar in bars:
    width = bar.get_width()
    label_x_pos = width if width > 0 else width + 1  # Adjust label position
    ax.text(label_x_pos, bar.get_y() + bar.get_height()/2, f'{width}°C', ha='left', va='center')

# Show the plot
plt.tight_layout()
plt.show()