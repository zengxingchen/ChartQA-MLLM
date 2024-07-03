
import matplotlib.pyplot as plt

# Data to plot
activities = ['Fashion Shows', 'Makeup Tutorials', 'Runway Practice', 'Photo Shoots', 'Fashion Design', 'Networking Events', 'Styling', 'Market Research']
hours = [4, 6, 3, 7, 5, 2, 4, 5]
colors = ['#FF1493', '#8A2BE2', '#FFD700', '#FF4500', '#2E8B57', '#FF6347', '#4682B4', '#7B68EE']

# Create pie chart
plt.figure(figsize=(12, 8))
plt.pie(hours, labels=activities, colors=colors, autopct='%1.1f%%', startangle=140)

# Draw a circle at the center of pie to make it look like a donut
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Time Allocation in Fashion & Beauty Industry', pad=20)
plt.show()