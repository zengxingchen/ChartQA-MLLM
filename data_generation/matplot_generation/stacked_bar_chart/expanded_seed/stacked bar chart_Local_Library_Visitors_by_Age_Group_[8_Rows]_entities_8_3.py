
import matplotlib.pyplot as plt

# Given data
data = [
    {'Week': 'Week 1', 'Children (0-12)': 240, 'Teens (13-18)': 150, 'Adults (19-64)': 500, 'Seniors (65+)': 200},
    {'Week': 'Week 2', 'Children (0-12)': 215, 'Teens (13-18)': 170, 'Adults (19-64)': 485, 'Seniors (65+)': 210},
    {'Week': 'Week 3', 'Children (0-12)': 180, 'Teens (13-18)': 160, 'Adults (19-64)': 510, 'Seniors (65+)': 220},
    {'Week': 'Week 4', 'Children (0-12)': 205, 'Teens (13-18)': 130, 'Adults (19-64)': 500, 'Seniors (65+)': 205},
    {'Week': 'Week 5', 'Children (0-12)': 220, 'Teens (13-18)': 145, 'Adults (19-64)': 515, 'Seniors (65+)': 195},
    {'Week': 'Week 6', 'Children (0-12)': 210, 'Teens (13-18)': 155, 'Adults (19-64)': 490, 'Seniors (65+)': 180},
    {'Week': 'Week 7', 'Children (0-12)': 225, 'Teens (13-18)': 140, 'Adults (19-64)': 505, 'Seniors (65+)': 210},
    {'Week': 'Week 8', 'Children (0-12)': 230, 'Teens (13-18)': 150, 'Adults (19-64)': 520, 'Seniors (65+)': 202}
]

# Data preparation
weeks = [d['Week'] for d in data]
children = [d['Children (0-12)'] for d in data]
teens = [d['Teens (13-18)'] for d in data]
adults = [d['Adults (19-64)'] for d in data]
seniors = [d['Seniors (65+)'] for d in data]

# Stacked bar chart setup
bar_width = 0.5  # Set the width of each bar
indices = range(len(weeks))  # Set the positions of the bars

# Plotting
plt.figure(figsize=(10, 7))

# Each "bottom" parameter ensures that the bars stack on top of each other
plt.bar(indices, children, bar_width, label='Children (0-12)', color='skyblue')
plt.bar(indices, teens, bar_width, bottom=children, label='Teens (13-18)', color='orange')
plt.bar(indices, adults, bar_width, bottom=[i+j for i,j in zip(children, teens)], label='Adults (19-64)', color='green')
plt.bar(indices, seniors, bar_width, bottom=[i+j+k for i,j,k in zip(children, teens, adults)], label='Seniors (65+)', color='purple')

# Adding features to the plot
plt.xlabel('Weeks')
plt.ylabel('Number of Visitors')
plt.title('Visitors by Age Group')
plt.xticks(indices, weeks)  # Set the x-axis to show the weeks
plt.legend()

# Display the plot
plt.tight_layout()
plt.show()