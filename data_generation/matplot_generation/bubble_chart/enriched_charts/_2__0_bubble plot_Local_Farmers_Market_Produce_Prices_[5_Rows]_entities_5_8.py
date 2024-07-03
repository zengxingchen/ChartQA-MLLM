
import matplotlib.pyplot as plt

# Provided data for the chart
age_groups = ['18-24', '25-34', '35-44', '45-54', '55-64', '65+']
reading = [0.7, 0.6, 0.9, 0.8, 1.0, 1.3]
watching_tv = [3.2, 2.7, 3.3, 4.1, 4.6, 5.1]
exercising = [1.0, 1.2, 1.1, 0.9, 0.7, 0.5]
playing_video_games = [2.0, 1.8, 1.0, 0.6, 0.3, 0.2]

# Bubble sizes, arbitrary values for visualization purposes
bubble_sizes = [size * 80 for size in reading + watching_tv + exercising + playing_video_games]

# Define colors for each activity
colors = [
    '#FF4500', '#FF6347', '#FF4500', '#FF6347', '#FF4500', '#FF6347',
    '#1E90FF', '#00BFFF', '#1E90FF', '#00BFFF', '#1E90FF', '#00BFFF',
    '#32CD32', '#7CFC00', '#32CD32', '#7CFC00', '#32CD32', '#7CFC00',
    '#8A2BE2', '#9370DB', '#8A2BE2', '#9370DB', '#8A2BE2', '#9370DB'
]

# Bubble chart
plt.figure(figsize=(12, 7))
plt.scatter(age_groups * 4, reading + watching_tv + exercising + playing_video_games, s=bubble_sizes, c=colors, alpha=0.6)

# Title and labels
plt.title('Average Leisure Activities per Day by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Average Hours per Day')

# Show grid
plt.grid(True)

# Show the figure
plt.show()