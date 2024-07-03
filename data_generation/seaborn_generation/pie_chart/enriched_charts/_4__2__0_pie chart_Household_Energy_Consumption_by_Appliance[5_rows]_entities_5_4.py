
import matplotlib.pyplot as plt

# Data to plot
labels = 'Basketball', 'Soccer', 'Tennis', 'Swimming', 'Running'
sizes = [25.0, 20.0, 15.0, 10.0, 30.0]
colors = ['#FF6347', '#4682B4', '#9ACD32', '#FFD700', '#FF69B4']

# Create pie chart
plt.figure(figsize=(10, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

plt.title('Popularity of Sports in 2023', pad=20)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()