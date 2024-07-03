
import matplotlib.pyplot as plt

# Data to plot
labels = ['Biology', 'Chemistry', 'Physics', 'Mathematics', 'Computer Science', 'Engineering', 'Environmental Science', 'Statistics']
sizes = [22, 18, 20, 15, 10, 8, 5, 2]
colors = ['#FF4500', '#1E90FF', '#32CD32', '#FFD700', '#FF69B4', '#8A2BE2', '#FF6347', '#2E8B57']

# Create pie chart
plt.figure(figsize=(12, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

# Title
plt.title('Popular Fields of Study in STEM', y=1.05)

# Display the chart
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()