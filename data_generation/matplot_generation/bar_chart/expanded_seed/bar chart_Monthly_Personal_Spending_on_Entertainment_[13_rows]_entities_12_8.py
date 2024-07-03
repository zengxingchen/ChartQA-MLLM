
import matplotlib.pyplot as plt
import numpy as np

# Provided dataset
data = [
    {'Month': 'January', 'Books': 40, 'Video Games': 60, 'Movies': 50, 'Concerts': 90, 'Sports Events': 30},
    {'Month': 'February', 'Books': 35, 'Video Games': 65, 'Movies': 45, 'Concerts': 85, 'Sports Events': 35},
    # ... [rest of the data truncated for brevity]
    {'Month': 'December', 'Books': 50, 'Video Games': 90, 'Movies': 80, 'Concerts': 120, 'Sports Events': 65}
]

# Extracting data for plotting
months = [item['Month'] for item in data]
books = [item['Books'] for item in data]
video_games = [item['Video Games'] for item in data]
movies = [item['Movies'] for item in data]
concerts = [item['Concerts'] for item in data]
sports_events = [item['Sports Events'] for item in data]

# Number of groups
num_groups = len(data)

# Create a figure and a set of subplots
fig, ax = plt.subplots(figsize=(14, 8))

# Set the positions of the bars on the x-axis
index = np.arange(num_groups)
bar_width = 0.15

# Plotting the bars
rects1 = ax.bar(index, books, bar_width, label='Books', color='skyblue')
rects2 = ax.bar(index + bar_width, video_games, bar_width, label='Video Games', color='orange')
rects3 = ax.bar(index + 2*bar_width, movies, bar_width, label='Movies', color='g')
rects4 = ax.bar(index + 3*bar_width, concerts, bar_width, label='Concerts', color='red')
rects5 = ax.bar(index + 4*bar_width, sports_events, bar_width, label='Sports Events', color='purple')

# Adding labels and title
ax.set_xlabel('Month')
ax.set_ylabel('Number of Items Sold')
ax.set_title('Monthly Sales Data Comparison')
ax.set_xticks(index + 2*bar_width)
ax.set_xticklabels(months)

# Adding a legend
ax.legend()

# Display the plot
plt.xticks(rotation=45) # Rotate x-axis labels for better readability
plt.tight_layout()  # To ensure the plot is adjusted properly
plt.show()