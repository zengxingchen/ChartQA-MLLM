
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
average_temperature = [-2, 0, 4, 11, 16, 20, 22, 21, 17, 10, 5, -1]

# Create horizontal bar chart
fig, ax = plt.subplots(figsize=(12, 8))  # Change width and height of the chart
bars = ax.barh(months, average_temperature, height=0.6, color=['#FF6347', '#FF4500', '#FFD700', '#ADFF2F', '#7FFF00', '#7CFC00', '#00FF00', '#32CD32', '#228B22', '#008000', '#006400', '#2F4F4F'])

# Customizing the plot
ax.set_title('Average Monthly Temperatures', fontsize=16)  # Change topic and headline
ax.set_xlabel('Average Temperature (°C)', fontsize=14)
ax.set_ylabel('Month', fontsize=14)

# Set bar labels to show the temperature values
for bar in bars:
    width = bar.get_width()
    label_x_pos = width if width > 0 else width - 10  # Adjust label position based on positive or negative values
    ax.text(label_x_pos, bar.get_y() + bar.get_height()/2, f'{width} °C', va='center')

# Show the plot
plt.tight_layout()
plt.show()