
import matplotlib.pyplot as plt

# Data for plotting
sports = ['Soccer', 'Basketball', 'Tennis', 'Cricket', 'Baseball', 'Rugby', 'Athletics', 'Golf']
popularity = [40.0, 20.0, 10.0, 15.0, 5.0, 3.0, 7.0, 4.0]
global_participants = [3500, 2200, 1500, 2500, 500, 400, 800, 450]
average_viewership = [4000, 2500, 1000, 2800, 900, 450, 750, 500]

# Create a figure with specified width and height
fig, ax = plt.subplots(figsize=(14, 10))

# Bubble sizes
sizes = [participants / 10 for participants in global_participants]

# Bubble colors with specific hex color codes
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f']

# Plot each data point
for (sport, pop, participants, viewership, size, color) in zip(sports, popularity, global_participants, average_viewership, sizes, colors):
    ax.scatter(pop, viewership, s=size, label=sport, alpha=0.6, edgecolors='w', color=color)

# Titles and labels
plt.title('Popularity and Viewership of Various Sports')
plt.xlabel('Popularity (%)')
plt.ylabel('Average Viewership (millions)')

# Legend
handles, labels = ax.get_legend_handles_labels()
hl = sorted(zip(handles, labels), key=lambda x: x[1])
handles2, labels2 = zip(*hl)
ax.legend(handles2, labels2, loc="upper left", title="Sports")

# Show plot
plt.show()