
import matplotlib.pyplot as plt

# Data
seasons = ['Winter', 'Spring', 'Summer', 'Autumn']
average_rainfall = [85, 110, 200, 130]

# Create vertical bar chart
fig, ax = plt.subplots(figsize=(10, 6))

bars = ax.bar(seasons, average_rainfall, width=0.4, color=['#1E90FF', '#32CD32', '#FFD700', '#FF4500'])

# Customizing the plot
ax.set_title('Seasonal Average Rainfall', fontsize=18)
ax.set_ylabel('Average Rainfall (mm)', fontsize=14)
ax.set_xlabel('Season', fontsize=14)

# Set bar labels to show the rainfall values
for bar in bars:
    height = bar.get_height()
    label_y_pos = height if height > 0 else height + 10  # Adjust label position
    ax.text(bar.get_x() + bar.get_width()/2, label_y_pos, f'{height} mm', ha='center', va='bottom')

# Show the plot
plt.tight_layout()
plt.show()