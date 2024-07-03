
import matplotlib.pyplot as plt

# Data to plot
labels = ['Watching TV', 'Reading Books', 'Playing Sports', 'Listening to Music', 
          'Traveling', 'Socializing', 'Gaming', 'Exercising']
sizes = [10, 7, 5, 8, 4, 6, 3, 2]
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', 
          '#FFC300', '#DAF7A6', '#FF33F6', '#33FFF0']

# Create pie chart
plt.figure(figsize=(10, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%',
        startangle=140)

# Title
plt.title('Weekly Leisure Activities', y=1.08)

# Display the chart
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()