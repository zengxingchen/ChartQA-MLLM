
import matplotlib.pyplot as plt

# Data to plot
labels = ['Books', 'Movies', 'Music', 'Video Games', 'Concerts', 'Theater', 'Podcasts', 'Other']
sizes = [25, 20, 15, 10, 8, 7, 10, 5]
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#8A2BE2', '#FF7F50', '#00CED1', '#A52A2A']

# Create pie chart
plt.figure(figsize=(12, 10))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

# Title
plt.title('Popular Entertainment Categories', y=1.05)

# Display the chart
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()