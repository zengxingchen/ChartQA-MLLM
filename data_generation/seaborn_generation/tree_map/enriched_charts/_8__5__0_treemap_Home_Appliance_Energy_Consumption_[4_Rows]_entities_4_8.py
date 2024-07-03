
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Data for creating the treemap
data = {
    'Event': ['Soccer Match', 'Basketball Game', 'Marathon', 'Tennis Tournament', 'Gymnastics Competition',
              'Swimming Gala', 'Cycling Race', 'Boxing Match', 'MMA Fight', 'Baseball Game',
              'Golf Tournament', 'Ice Hockey Game', 'Athletics Meet', 'Rugby Game', 'Volleyball Match',
              'Cricket Match', 'Formula 1 Race', 'Skiing Competition', 'Surfing Contest', 'Horse Racing'],
    'Attendance': [55000, 45000, 30000, 25000, 20000,
                   18000, 22000, 17000, 15000, 40000,
                   10000, 28000, 35000, 32000, 26000,
                   50000, 60000, 8000, 12000, 37000]
}

# Convert the data dictionary to a pandas DataFrame
df = pd.DataFrame(data)

# Define size of the figure
plt.figure(figsize=(16,12))

# Define custom colors using specific color codes
colors = ['#a6cee3', '#1f78b4', '#b2df8a', '#33a02c', '#fb9a99',
          '#e31a1c', '#fdbf6f', '#ff7f00', '#cab2d6', '#6a3d9a',
          '#ffff99', '#b15928', '#8dd3c7', '#ffffb3', '#bebada',
          '#fb8072', '#80b1d3', '#fdb462', '#b3de69', '#fccde5']

# Create the treemap
squarify.plot(sizes=df['Attendance'], label=df['Event'], color=colors, alpha=0.8)

# Set the title of the treemap
plt.title('Event Attendance in the Sports & Fitness Sector')

# Remove the axis lines
plt.axis('off')

# Display the treemap
plt.show()