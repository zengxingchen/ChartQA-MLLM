
import matplotlib.pyplot as plt

# Data
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
screen_time = [90, 120, 45, 150, 75, 180, 100]

# Create figure and axis objects
fig, ax = plt.subplots(figsize=(10, 6))  # Changed figure size

# Plotting the bar chart
ax.bar(days, screen_time, color=['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#FF8F33', '#33FFF3', '#8F33FF'], width=0.6)  # Changed colors and bar width

# Customizing the plot (labels, title, etc.)
ax.set_ylabel('Screen Time (minutes)')
ax.set_title('Daily Screen Time')
ax.set_ylim([40, 190])  # Truncated y-axis

# Display the plot
plt.tight_layout()
plt.show()