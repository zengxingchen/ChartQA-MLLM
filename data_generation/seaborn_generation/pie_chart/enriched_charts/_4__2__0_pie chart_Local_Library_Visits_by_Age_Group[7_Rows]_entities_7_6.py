
import matplotlib.pyplot as plt

# Data to plot
labels = ['Pop Music', 'Classical Music', 'Rock Music', 'Jazz Music', 'Hip Hop', 'Country Music', 'Electronic Music', 'Folk Music']
sizes = [25, 15, 20, 10, 8, 7, 6, 9]
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFF0', '#F033FF', '#FF8C33', '#33FFA6']

# Create pie chart
plt.figure(figsize=(12, 10))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

# Title
plt.title('Popular Music Genres', y=1.05)

# Display the chart
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()