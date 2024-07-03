
import matplotlib.pyplot as plt

# Data points for hours spent on online learning vs course completion rate
hours_spent = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
completion_rate = [10, 20, 30, 35, 45, 50, 55, 60, 70, 75, 80, 85, 90, 92, 94, 96, 98, 100, 100, 100]

# Creating the scatter plot
plt.figure(figsize=(14, 8))  # Modify width and height of the chart
plt.scatter(hours_spent, completion_rate, color='#4B0082')  # Change to an RGB color code

# Adding chart labels and title
plt.title('Impact of Online Learning Hours on Course Completion Rate', pad=20)
plt.xlabel('Hours Spent on Online Learning')
plt.ylabel('Course Completion Rate (%)')

# Adding a grid for better readability
plt.grid(True, linestyle='--', alpha=0.7)

# Show the figure
plt.show()