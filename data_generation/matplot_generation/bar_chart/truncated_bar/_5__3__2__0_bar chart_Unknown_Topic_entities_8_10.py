
import matplotlib.pyplot as plt

# Data
categories = [
    'Soccer', 'Basketball', 'Yoga', 'Martial Arts', 'Tennis', 'Running', 
    'Swimming', 'Cycling', 'Weightlifting', 'Climbing', 'Golf', 'Boxing', 
    'Cricket', 'Hiking', 'Rowing', 'Badminton', 'Rugby', 'Gymnastics', 
    'Skiing', 'Surfing', 'Triathlon', 'Table Tennis', 'Fencing', 'Kayaking'
]
interest_level = [
    80, 85, 95, 90, 75, 85, 80, 90, 70, 95, 65, 75, 80, 85, 70, 75, 80, 
    85, 70, 75, 80, 90, 85, 75
]

# Plotting the bar chart
plt.figure(figsize=(12, 8))
plt.bar(categories, interest_level, width=0.6, color=[
    '#ff6347', '#4682b4', '#3cb371', '#ffa07a', '#6a5acd', '#ffb6c1', 
    '#20b2aa', '#ff4500', '#b0c4de', '#8a2be2', '#ff8c00', '#daa520', 
    '#9acd32', '#ee82ee', '#ff6347', '#4682b4', '#3cb371', '#ffa07a', 
    '#6a5acd', '#ffb6c1', '#20b2aa', '#ff4500', '#b0c4de', '#8a2be2'
])

# Customizing the plot
plt.ylabel('Interest Level')
plt.title('Interest Levels in Various Sports & Fitness Activities')
plt.ylim(60, 100)

# Show the plot
plt.show()