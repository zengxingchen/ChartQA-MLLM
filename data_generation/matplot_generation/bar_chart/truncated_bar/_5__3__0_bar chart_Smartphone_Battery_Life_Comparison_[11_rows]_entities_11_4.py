
import matplotlib.pyplot as plt

# Data for the chart
activities = [
    "Reading", "Writing", "Exercising", "Sleeping", "Working", 
    "Cooking", "Eating", "Socializing", "Watching TV", "Commuting", 
    "Meditating", "Gaming"
]
hours = [2, 1.5, 1, 8, 7, 1.5, 1.5, 2, 2.5, 1.2, 0.8, 2.3]

# Modified color scheme
colors = [
    '#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0',
    '#ffb3e6','#c4e17f','#ff6666','#c7e9c0','#b3b3cc',
    '#ff8c66','#8c66ff'
]

# Create horizontal bar chart
plt.figure(figsize=(10, 8))  # Width and height of the chart
plt.barh(activities, hours, color=colors, height=0.6)  # Bar color and bar height

# Set the title and labels
plt.title('Daily Time Allocation on Various Activities', pad=20)
plt.xlabel('Hours')
plt.ylabel('Activity')

# Set y-axis limits to truncate the chart
plt.xlim(0.5, 8.5)

# Display the bar chart
plt.show()