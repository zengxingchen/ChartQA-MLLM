
import matplotlib.pyplot as plt

# Data
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
avg_daily_steps = [
    7500, 7600, 8000, 8200, 8500, 9000, 9500, 9400, 8800, 8400, 8000, 7600
]

# Create the plot
plt.figure(figsize=(14, 7))  # Change the size of the chart
plt.plot(months, avg_daily_steps, marker='s', color="#4CAF50", linewidth=2)  # Change color and add square markers

# Annotations
for i, steps in enumerate(avg_daily_steps):
    plt.annotate(steps, (months[i], steps), textcoords="offset points", xytext=(0, 5),
                 ha='center', color="#E91E63")

# Improve the visual appeal with labels, title, and grid
plt.xlabel('Month')
plt.ylabel('Average Daily Steps')
plt.title('Average Daily Steps Over a Year', pad=20)
plt.grid(True)

# Show the plot
plt.show()