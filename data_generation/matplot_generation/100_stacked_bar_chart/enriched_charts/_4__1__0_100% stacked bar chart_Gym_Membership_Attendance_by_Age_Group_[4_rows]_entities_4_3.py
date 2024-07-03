
import matplotlib.pyplot as plt
import numpy as np

age_groups = ['18-24', '25-34', '35-44', '45-54', '55-64', '65+']
social_media = [20, 15, 10, 5, 5, 5]
streaming_services = [25, 30, 35, 30, 25, 20]
video_games = [30, 25, 20, 15, 10, 5]
reading_books = [15, 20, 25, 30, 35, 40]
outdoor_activities = [10, 10, 10, 20, 25, 30]

data = np.array([social_media, streaming_services, video_games, reading_books, outdoor_activities])
data_cum = data.cumsum(axis=0)

colors = ['#6A5ACD', '#FF69B4', '#4682B4', '#9ACD32', '#FF4500']

bar_height = 0.75

fig, ax = plt.subplots(figsize=(8, 12))

for i, (colname, color) in enumerate(zip(['Social Media', 'Streaming Services', 'Video Games', 'Reading Books', 'Outdoor Activities'], colors)):
    widths = data[i]
    starts = data_cum[i] - widths
    ax.barh(age_groups, widths, left=starts, height=bar_height, label=colname, color=color)

ax.set_xlabel('Percentage (%)')
ax.set_title('Leisure Activities Across Age Groups', pad=20)
ax.legend(loc='upper right')

plt.tight_layout()
plt.show()