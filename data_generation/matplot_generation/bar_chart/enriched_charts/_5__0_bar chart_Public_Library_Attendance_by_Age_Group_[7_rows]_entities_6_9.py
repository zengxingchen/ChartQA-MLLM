
import matplotlib.pyplot as plt

# Data
days = [
    '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', 
    '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', 
    '24', '25', '26', '27', '28', '29', '30'
]
calories_burned = [
    200, 210, 250, 180, 300, 220, 190, 260, 240, 270, 310, 230, 280, 
    260, 250, 300, 210, 270, 260, 240, 290, 200, 230, 250, 270, 280, 
    240, 220, 260, 250
]

# Colors for each bar
colors = [
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', 
    '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#393b79', '#637939', 
    '#8c6d31', '#843c39', '#6b6ecf', '#d6616b', '#e7ba52', '#e7969c', 
    '#31a354', '#636363', '#e6550d', '#fdae6b', '#74c476', '#fd8d3c', 
    '#756bb1', '#dadaeb', '#9e9ac8', '#6a51a3', '#d94801', '#f16913'
]

# Create a vertical bar chart
plt.figure(figsize=(12, 6))  # Change the figure size (width x height)
bar_width = 0.8  # Change the bar width
plt.bar(days, calories_burned, color=colors, width=bar_width)

# Setting the title and labels
plt.title('Daily Calories Burned During Workout', pad=20)
plt.xlabel('Day of the Month')
plt.ylabel('Calories Burned')

# Adjust the limits if necessary
plt.ylim([150, max(calories_burned) + 50])

# Display the chart
plt.tight_layout()
plt.show()