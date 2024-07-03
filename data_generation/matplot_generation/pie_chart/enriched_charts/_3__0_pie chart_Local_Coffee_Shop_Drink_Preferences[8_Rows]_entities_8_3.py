
import matplotlib.pyplot as plt

# Data
subjects = [
    'Reading', 'Writing', 'Mathematics', 'Science', 'Social Studies', 
    'Physical Education', 'Art', 'Music', 'Computer Science', 
    'Foreign Language', 'Health Education', 'Extracurricular Activities'
]
hours_per_week = [12, 8, 10, 7, 6, 5, 4, 3, 5, 6, 2, 8]
colors = [
    '#FF6347', '#4682B4', '#FFD700', '#32CD32', '#FF69B4', 
    '#8A2BE2', '#FF4500', '#1E90FF', '#40E0D0', '#A52A2A', 
    '#D2691E', '#C71585'
]

# Create a pie chart
plt.figure(figsize=(12, 9))  # Adjusting the size of the pie chart
plt.pie(hours_per_week, labels=subjects, colors=colors, startangle=140, autopct='%1.1f%%')

# Title of the pie chart
plt.title('Weekly Time Allocation for School Subjects', pad=20)

plt.show()