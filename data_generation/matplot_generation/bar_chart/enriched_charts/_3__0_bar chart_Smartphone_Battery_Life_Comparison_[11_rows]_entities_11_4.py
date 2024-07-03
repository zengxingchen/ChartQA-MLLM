
import matplotlib.pyplot as plt

# Time spent on daily activities
activities = [
    "Reading", "Writing", "Exercising", "Sleeping", "Working", 
    "Cooking", "Eating", "Socializing", "Watching TV", "Commuting"
]
hours = [2, 1.5, 1, 8, 7, 1, 1.5, 2, 2, 1]

# Color scheme using specific color codes for each activity
colors = [
    '#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0',
    '#ffb3e6','#c4e17f','#ff6666','#c7e9c0','#b3b3cc'
]

# Create vertical bar chart
plt.figure(figsize=(12, 6))  # Width and height of the chart
plt.bar(activities, hours, color=colors, width=0.6)  # Bar color and band width

# Set the title and labels
plt.title('Daily Time Allocation')
plt.ylabel('Hours')
plt.xlabel('Activity')

# Display the bar chart
plt.show()