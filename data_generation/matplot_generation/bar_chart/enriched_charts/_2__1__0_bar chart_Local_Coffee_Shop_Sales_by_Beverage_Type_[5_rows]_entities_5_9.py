
import matplotlib.pyplot as plt

# Data
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
reading_time = [30, 45, 20, 50, 35, 60, 40]

# Create figure and axis objects
fig, ax = plt.subplots(figsize=(12, 8))  # Changed figure size

# Plotting the bar chart
ax.barh(days, reading_time, color=['#4A90E2', '#50E3C2', '#B8E986', '#F5A623', '#F8E71C', '#D0021B', '#9013FE'], height=0.5)  # Changed colors and bar height

# Customizing the plot (labels, title, etc.)
ax.set_xlabel('Reading Time (minutes)')
ax.set_title('Daily Reading Time')
ax.set_xlim([0, 70])  # Adjusted to accommodate the maximum data point

# Display the plot
plt.tight_layout()
plt.show()