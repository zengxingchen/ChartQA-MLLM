
import matplotlib.pyplot as plt

# Data
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
calories = [500, 600, 450, 700, 800, 750, 600]

# Create figure and axis objects
fig, ax = plt.subplots(figsize=(10, 6))  # Changed figure size

# Plotting the bar chart
ax.bar(days, calories, color=['#ff5733', '#33ff57', '#3357ff', '#ff33a6', '#a633ff', '#ffa633', '#33ffa6'], width=0.5)  # Changed colors and bar width

# Customizing the plot (labels, title, etc.)
ax.set_ylabel('Calories Burned')
ax.set_title('Weekly Calorie Burn Data')
ax.set_ylim([0, 1000])  # Adjusted to accommodate the maximum data point

# Display the plot
plt.tight_layout()
plt.show()