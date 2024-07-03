
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data points
data = {
    'Activity': ['Soccer', 'Basketball', 'Running', 'Swimming', 'Cycling', 'Yoga', 'Weightlifting'],
    'TimeSpent': [2, 1.5, 3, 2.5, 4, 1, 1.5]
}
df = pd.DataFrame(data)

# Setting the color codes for clarity
colors = ['#2e8b57', '#8a2be2', '#ff4500', '#ffd700', '#6495ed', '#ff69b4', '#7fff00']

# Initialize the matplotlib figure size
f, ax = plt.subplots(figsize=(8, 10))

# Create the vertical bar chart
sns.barplot(x='Activity', y='TimeSpent', data=df, palette=colors)

# Setting the bar width
for container in ax.containers:
    plt.setp(container, width=0.6)

# Customize the chart
plt.title('Average Time Spent on Various Sports Activities')
plt.xlabel('Activity')
plt.ylabel('Average Time Spent (Hours)')

# Display the chart
plt.show()