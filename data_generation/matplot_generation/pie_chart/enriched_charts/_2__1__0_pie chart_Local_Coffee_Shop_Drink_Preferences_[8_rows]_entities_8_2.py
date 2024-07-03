
import matplotlib.pyplot as plt

# Data to plot
labels = 'Movies', 'Music', 'Video Games', 'Reading', 'Sports'
sizes = [30, 25, 20, 10, 15]
colors = ['#ff4500', '#1e90ff', '#ff1493', '#32cd32', '#ff8c00']

# Change the size of the figure (width, height)
plt.figure(figsize=(10, 6))

# Plot
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

plt.title('Distribution of Time Spent on Entertainment Activities', pad=20)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()