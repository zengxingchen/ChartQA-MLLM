
import matplotlib.pyplot as plt
import squarify

# Dataset
sports = ['Soccer', 'Badminton', 'Field Hockey', 'Volleyball', 'Basketball', 'Tennis', 'Cricket', 'Table Tennis', 'Baseball', 'Golf', 'Running', 'Swimming', 'Cycling', 'Boxing', 'Rugby', 'Wrestling']
participation = [4000000000, 2200000000, 2000000000, 900000000, 825000000, 750000000, 450000000, 300000000, 500000000, 390000000, 500000000, 300000000, 1300000000, 250000000, 50000000, 30000000]

# Color Scheme
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#393b79', '#637939', '#8c6d31', '#843c39', '#ad494a', '#d6616b']

plt.figure(figsize=(14, 10))

# Creating the treemap
squarify.plot(sizes=participation, label=sports, color=colors, alpha=0.8)

# Adding a title
plt.title('Global Sports Participation (Number of Participants)', fontsize=16, weight='bold')

# Removing the axes
plt.axis('off')

# Display the plot
plt.show()