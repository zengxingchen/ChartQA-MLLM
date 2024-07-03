
import matplotlib.pyplot as plt
import numpy as np

# Data extracted from the table
users = ['Anna', 'Ben', 'Cody', 'Diana', 'Evan', 'Fiona', 'Gina', 'Hank', 'Ivy', 'Jack', 'Karl', 'Lia']
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Convert table data to a structured format
data = {
    'Anna': [4.1, 3.7, 4.0, 3.5, 5.2, 6.8, 7.1],
    'Ben': [2.5, 2.0, 2.7, 3.1, 3.5, 4.0, 4.5],
    'Cody': [1.2, 1.5, 1.4, 1.3, 1.7, 2.2, 2.0],
    'Diana': [3.8, 3.9, 4.3, 4.0, 5.0, 5.5, 6.0],
    'Evan': [5.5, 5.0, 5.7, 5.5, 6.2, 7.0, 7.5],
    'Fiona': [3.2, 2.8, 3.0, 3.3, 3.6, 4.1, 4.3],
    'Gina': [4.0, 4.2, 4.1, 4.1, 4.8, 5.3, 5.5],
    'Hank': [1.5, 1.7, 2.0, 2.2, 2.4, 2.6, 2.5],
    'Ivy': [6.0, 5.8, 6.2, 6.1, 7.3, 8.2, 8.5],
    'Jack': [2.3, 2.1, 2.2, 2.5, 2.7, 3.1, 3.3],
    'Karl': [3.7, 3.5, 3.9, 3.8, 4.4, 5.0, 5.2],
    'Lia': [7.1, 6.8, 7.0, 6.9, 8.0, 9.1, 9.4]
}

num_users = len(users)
num_days = len(days_of_week)

# Assign a unique color to each user
colors = plt.cm.viridis(np.linspace(0, 1, num_users))

# Setting up the bar width and positions
bar_width = 0.1
indices = np.arange(num_days)

# Create a bar for each user
for i, user in enumerate(users):
    plt.bar(indices + i * bar_width, data[user], bar_width, label=user, color=colors[i])

# Adding labels and title
plt.xlabel('Day of the Week')
plt.ylabel('Values')
plt.title('Values by User and Day of the Week')
plt.xticks(indices + bar_width * (num_users / 2 - 0.5), days_of_week)
plt.legend()

# Adding value labels above bars
for i, user in enumerate(users):
    for index, value in enumerate(data[user]):
        plt.text(index + i * bar_width, value + 0.05, f"{value:.1f}", ha='center')

# Display the plot
plt.show()