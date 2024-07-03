
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
average_temperature = [-2, 0, 4, 11, 16, 20, 22, 21, 17, 10, 5, -1]

# Create vertical bar chart
fig, ax = plt.subplots(figsize=(10, 6))  # Change width and height of the chart
bars = ax.bar(months, average_temperature, width=0.5, color=['#FF5733', '#FF6F61', '#FF9E80', '#FFD180', '#FFF59D', '#C8E6C9', '#A5D6A7', '#81C784', '#66BB6A', '#4CAF50', '#388E3C', '#2E7D32'])

# Customizing the plot
ax.set_title('Average Monthly Temperatures', fontsize=16, pad=20)  # Change topic and headline
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Average Temperature (°C)', fontsize=14)

# Set y-axis limits to truncate the chart
ax.set_ylim(-5, 25)

# Set bar labels to show the temperature values
for bar in bars:
    height = bar.get_height()
    label_y_pos = height if height > 0 else height - 2  # Adjust label position based on positive or negative values
    ax.text(bar.get_x() + bar.get_width()/2, label_y_pos, f'{height} °C', ha='center', va='bottom' if height > 0 else 'top')

# Show the plot
plt.tight_layout()
plt.show()