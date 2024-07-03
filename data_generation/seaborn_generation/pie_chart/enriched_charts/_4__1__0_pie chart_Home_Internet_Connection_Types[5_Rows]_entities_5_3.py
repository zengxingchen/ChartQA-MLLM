
import matplotlib.pyplot as plt

# Data
categories = ['Running', 'Swimming', 'Cycling', 'Hiking', 'Yoga', 'Gym Workouts', 'Dance', 'Martial Arts', 'Other']
percentages = [25.00, 15.00, 20.00, 10.00, 5.00, 10.00, 8.00, 2.00, 5.00]
colors = ['#FF6347', '#4682B4', '#FFD700', '#ADFF2F', '#FF69B4', '#8A2BE2', '#00FA9A', '#FF4500', '#1E90FF']

# Create a pie chart
plt.figure(figsize=(14, 10))
plt.pie(percentages, labels=categories, autopct='%1.1f%%', startangle=140, colors=colors)

# Title
plt.title('Popular Hobbies in 2023', fontsize=16)

# Display the chart
plt.show()