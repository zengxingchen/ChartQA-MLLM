
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
average_sleep_hours = [7.5, 7.3, 7.2, 7.1, 7.0, 6.8, 6.5, 6.7, 6.9, 7.0, 7.3, 7.6]

# Create vertical bar chart
fig, ax = plt.subplots(figsize=(10, 6))  # Change width and height of the chart
bars = ax.bar(months, average_sleep_hours, width=0.5, color=['#1E90FF', '#00BFFF', '#87CEFA', '#4682B4', '#5F9EA0', '#00CED1', '#20B2AA', '#3CB371', '#2E8B57', '#006400', '#008000', '#32CD32'])

# Customizing the plot
ax.set_title('Average Monthly Sleep Hours', fontsize=18, pad=20)  # Change topic and headline
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Average Sleep Hours', fontsize=14)
ax.set_ylim(6, 8)  # Set y-axis limits

# Set bar labels to show the sleep hours values
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, height + 0.05, f'{height} hrs', ha='center', va='bottom')

# Show the plot
plt.tight_layout()
plt.show()