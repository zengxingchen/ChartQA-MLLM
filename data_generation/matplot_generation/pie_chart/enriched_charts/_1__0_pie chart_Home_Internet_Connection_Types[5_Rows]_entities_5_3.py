
import matplotlib.pyplot as plt

# Data
categories = ['Running', 'Swimming', 'Cycling', 'Hiking', 'Yoga', 'Gym Workouts', 'Dance', 'Martial Arts', 'Other']
percentages = [30.00, 20.00, 15.00, 10.00, 8.00, 7.00, 5.00, 5.00, 10.00]
colors = ['#FF5733', '#33FFBD', '#3375FF', '#FF33A8', '#85FF33', '#FFC300', '#8D33FF', '#FF3380', '#33FFF9']

# Create a pie chart
plt.figure(figsize=(12, 8))
plt.pie(percentages, labels=categories, autopct='%1.1f%%', startangle=140, colors=colors)

# Title
plt.title('Popular Fitness Activities in 2023', fontsize=16)

# Display the chart
plt.show()