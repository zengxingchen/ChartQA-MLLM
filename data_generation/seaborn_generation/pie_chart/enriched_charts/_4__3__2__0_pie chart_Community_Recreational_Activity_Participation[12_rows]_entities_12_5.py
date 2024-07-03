
import matplotlib.pyplot as plt

# Data points
activities = ['Running', 'Cycling', 'Swimming', 'Gym Workouts', 'Yoga', 'Team Sports', 'Hiking', 'Others']
percentage_share = [20.0, 15.0, 10.0, 25.0, 10.0, 10.0, 5.0, 5.0]

# Colors using hexadecimal color codes
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A133FF', '#FFD133', '#33FFD1', '#FF5733']

# Plotting the pie chart
plt.figure(figsize=(12, 9))  # Width and height of the chart
plt.pie(percentage_share, labels=activities, colors=colors, autopct='%1.1f%%', startangle=140)

# Title of the chart
plt.title('Distribution of Physical Activities in 2023', pad=30)

# Display the chart
plt.show()