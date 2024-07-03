
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
average_temperature = [-2, 1, 5, 10, 15, 21, 23, 22, 18, 11, 4, -1]

# Create vertical bar chart
fig, ax = plt.subplots(figsize=(10, 6))  # Change width and height of the chart
bars = ax.bar(months, average_temperature, width=0.5, color=['#4682B4', '#1E90FF', '#00BFFF', '#87CEEB', '#32CD32', '#00FA9A', '#00FF7F', '#3CB371', '#2E8B57', '#6B8E23', '#808000', '#BDB76B'])

# Customizing the plot
ax.set_title('Average Monthly Temperatures', fontsize=16)  # Change topic and headline
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Average Temperature (°C)', fontsize=14)

# Set bar labels to show the temperature values
for bar in bars:
    height = bar.get_height()
    label_y_pos = height if height > 0 else height - 2  # Adjust label position based on positive or negative values
    ax.text(bar.get_x() + bar.get_width()/2, label_y_pos, f'{height} °C', ha='center', va='bottom' if height > 0 else 'top')

# Show the plot
plt.tight_layout()
plt.show()