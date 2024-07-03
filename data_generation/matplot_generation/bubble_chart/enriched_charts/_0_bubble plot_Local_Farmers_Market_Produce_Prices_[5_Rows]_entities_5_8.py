
import matplotlib.pyplot as plt

# Provided data for the chart
age_groups = ['18-24', '25-34', '35-44', '45-54', '55-64', '65+']
reading = [0.5, 0.8, 0.6, 0.7, 0.9, 1.1]
watching_tv = [2.8, 2.5, 3.0, 4.0, 4.5, 5.0]
exercising = [0.9, 1.1, 1.0, 0.8, 0.6, 0.4]
playing_video_games = [2.5, 1.5, 0.7, 0.4, 0.2, 0.1]

# Bubble sizes, arbitrary values for visualization purposes
bubble_sizes = [size * 80 for size in reading + watching_tv + exercising + playing_video_games]

# Define colors for each activity
colors = [
    # Reading color codes
    '#FF7F0E', '#FFBB78', '#FF7F0E', '#FFBB78', '#FF7F0E', '#FFBB78',
    # Watching TV color codes
    '#1F77B4', '#AEC7E8', '#1F77B4', '#AEC7E8', '#1F77B4', '#AEC7E8',
    # Exercising color codes
    '#2CA02C', '#98DF8A', '#2CA02C', '#98DF8A', '#2CA02C', '#98DF8A',
    # Playing Video Games color codes
    '#D62728', '#FF9896', '#D62728', '#FF9896', '#D62728', '#FF9896'
]

# Bubble chart
plt.figure(figsize=(10, 6))
plt.scatter(age_groups * 4, reading + watching_tv + exercising + playing_video_games, s=bubble_sizes, c=colors, alpha=0.6)

# Title and labels
plt.title('Average Leisure Hours per Day by Activity and Age Group')
plt.xlabel('Age Group')
plt.ylabel('Average Hours per Day')

# Show grid
plt.grid(True)

# Show the figure
plt.show()