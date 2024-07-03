
import matplotlib.pyplot as plt

# Data
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
calories_burned = [250, 300, 200, 350, 500, 450, 275]

# Create figure and axis objects
fig, ax = plt.subplots(figsize=(10, 6))  # Changed figure size

# Plotting the bar chart
ax.bar(days, calories_burned, color=['#ff5733', '#33ff57', '#3357ff', '#ff33a1', '#33fff5', '#ffb833', '#b833ff'], width=0.5)  # Changed colors and bar width

# Customizing the plot (labels, title, etc.)
ax.set_ylabel('Calories Burned')
ax.set_title('Weekly Calories Burned Data', pad=20)  # Changed title and added padding

# Adjusting the limit to better fit the data
ax.set_ylim([150, 550])  # Truncated y-axis to start from a specific value

# Display the plot
plt.tight_layout()
plt.show()