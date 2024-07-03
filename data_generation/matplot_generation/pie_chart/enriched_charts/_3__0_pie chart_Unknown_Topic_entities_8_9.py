
import matplotlib.pyplot as plt

# Data points
categories = ['Physics', 'Chemistry', 'Biology', 'Mathematics', 'Computer Science', 'Geology', 'Astronomy', 'Others']
percentages = [15.0, 18.0, 12.0, 10.0, 14.0, 8.0, 6.0, 17.0]
colors = ['#4B0082', '#FF4500', '#32CD32', '#FFD700', '#1E90FF', '#FF69B4', '#8A2BE2', '#FF6347']

# Create a pie chart
plt.figure(figsize=(12, 9))  # Modify the width and height of the chart
plt.pie(percentages, labels=categories, colors=colors, autopct='%1.1f%%', startangle=140)

# Chart title
plt.title('Distribution of Scientific Research Fields in 2023', pad=20)

# Display the chart
plt.show()