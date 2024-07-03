
import matplotlib.pyplot as plt

# Data
activities = [
    'Running', 'Swimming', 'Cycling', 'Yoga', 'Weightlifting',
    'Pilates', 'Boxing', 'Hiking', 'Tennis', 'Dancing',
    'Martial Arts', 'Climbing', 'Rowing', 'Skating'
]
counts = [80, 65, 75, 45, 55, 30, 50, 70, 40, 52, 38, 48, 28, 62]
colors = [
    '#FF6347', '#4682B4', '#32CD32', '#FFD700', '#C71585',
    '#1E90FF', '#FF69B4', '#8A2BE2', '#DC143C', '#00FA9A',
    '#FF4500', '#00CED1', '#8B0000', '#FF7F50'
]

# Create a pie chart
plt.figure(figsize=(16, 12))  # Adjusting the size of the pie chart
plt.pie(counts, labels=activities, colors=colors, startangle=100, autopct='%1.1f%%')

# Title of the pie chart
plt.title('Interest Distribution by Activity in Sports & Fitness', pad=30)

plt.show()