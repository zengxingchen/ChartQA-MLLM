
import matplotlib.pyplot as plt

# Data
categories = [
    'Cardio Exercise', 'Strength Training', 'Flexibility Workouts', 'Balance Training', 'Aerobic Classes', 
    'Pilates', 'Yoga', 'Martial Arts', 'High-Intensity Interval Training (HIIT)', 'Dance Workouts', 
    'Water Aerobics', 'Team Sports', 'Cycling', 'Running'
]
counts = [80, 65, 50, 40, 30, 25, 20, 15, 10, 5, 8, 7, 9, 12]
colors = [
    '#FF6347', '#4682B4', '#FFD700', '#8A2BE2', '#32CD32', 
    '#A52A2A', '#FF4500', '#2E8B57', '#D2691E', '#E6E6FA', 
    '#800080', '#FFFF54', '#40E0D0', '#C71585'
]

# Create a pie chart
plt.figure(figsize=(12, 9))  # Adjusting the size of the pie chart
plt.pie(counts, labels=categories, colors=colors, startangle=140, autopct='%1.1f%%')

# Title of the pie chart
plt.title('Fitness Activity Distribution', pad=20)

plt.show()