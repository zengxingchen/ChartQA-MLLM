
import matplotlib.pyplot as plt

# Data to plot
labels = ['Renewable Energy', 'Wildlife Conservation', 'Climate Change', 'Pollution Control', 'Sustainable Agriculture', 'Green Technology', 'Water Conservation', 'Other']
sizes = [30, 20, 15, 10, 8, 7, 5, 5]
colors = ['#66CDAA', '#FF6347', '#4682B4', '#FFD700', '#8A2BE2', '#FF7F50', '#00CED1', '#A52A2A']

# Create pie chart
plt.figure(figsize=(14, 12))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

# Title
plt.title('Environmental Initiatives Breakdown', y=1.08)

# Display the chart
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()