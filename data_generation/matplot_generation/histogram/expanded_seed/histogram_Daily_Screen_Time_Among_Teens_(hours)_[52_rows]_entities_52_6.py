
import matplotlib.pyplot as plt

# Data given
data = [
    {'Age': 13, ' Screen Time (hours)': 4.5},
    {'Age': 13, ' Screen Time (hours)': 5.2},
    {'Age': 13, ' Screen Time (hours)': 3.8},
    {'Age': 13, ' Screen Time (hours)': 5.0},
    {'Age': 13, ' Screen Time (hours)': 6.1},
    {'Age': 14, ' Screen Time (hours)': 5.5},
    {'Age': 14, ' Screen Time (hours)': 6.0},
    {'Age': 14, ' Screen Time (hours)': 4.3},
    {'Age': 14, ' Screen Time (hours)': 5.2},
    {'Age': 14, ' Screen Time (hours)': 6.6},
    {'Age': 15, ' Screen Time (hours)': 7.0},
    {'Age': 15, ' Screen Time (hours)': 6.5},
    {'Age': 15, ' Screen Time (hours)': 5.5},
    {'Age': 15, ' Screen Time (hours)': 7.2},
    {'Age': 15, ' Screen Time (hours)': 6.8}
]

# Organizing the data
screen_times = {13: [], 14: [], 15: []}
for entry in data:
    age = entry['Age']
    screen_time = entry[' Screen Time (hours)']
    screen_times[age].append(screen_time)

# Colors (could use any colormap or specific colors you want)
colors = ['blue', 'orange', 'green']
labels = ['Age 13', 'Age 14', 'Age 15']
bins = [3, 4, 5, 6, 7, 8]  # Define bins for histogram

# Create the histogram
fig, ax = plt.subplots()

for i, (age, times) in enumerate(screen_times.items()):
    ax.hist(times, bins=bins, color=colors[i], label=labels[i], alpha=0.7)

# Add labels and title
ax.set_xlabel('Screen Time (hours)')
ax.set_ylabel('Frequency')
ax.set_title('Histogram of Screen Time by Age')

# Add legend to distinguish age groups
ax.legend()

# Show the plot
plt.show()