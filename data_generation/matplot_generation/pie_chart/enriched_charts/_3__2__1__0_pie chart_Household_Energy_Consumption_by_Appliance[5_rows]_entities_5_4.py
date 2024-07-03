
import matplotlib.pyplot as plt

# Data to plot
labels = 'Researching New Technologies', 'Physical Training', 'Public Speaking', 'Innovation Workshops', 'Networking Events', 'Resting'
sizes = [35, 25, 15, 10, 15, 40]
colors = ['#ff6666', '#66ff66', '#6666ff', '#ff66ff', '#ffcc66', '#66cccc']

# Create pie chart
plt.figure(figsize=(12, 9))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

plt.title('Daily Activities of a Tech Entrepreneur', pad=20)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()