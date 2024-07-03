
import matplotlib.pyplot as plt
import numpy as np

data = {
    'Topic': ['Pop', 'Rock', 'Jazz', 'Classical', 'Hip-Hop', 'Country', 'Electronic', 'Blues', 'Reggae', 'Latin', 'Folk', 'Opera'],
    'Segment A': [12, 20, 25, 15, 30, 18, 22, 17, 20, 25, 30, 15],
    'Segment B': [30, 35, 40, 25, 20, 32, 28, 33, 35, 30, 20, 25],
    'Segment C': [58, 45, 35, 60, 50, 50, 50, 50, 45, 45, 50, 60]
}

topics = data['Topic']
segments = ['Segment A', 'Segment B', 'Segment C']
values = np.array([data[segment] for segment in segments])

fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.7

bottom = np.zeros(len(topics))

colors = ['#1e90ff', '#ff1493', '#32cd32']

for i, segment in enumerate(segments):
    ax.bar(topics, values[i], bottom=bottom, width=bar_width, label=segment, color=colors[i])
    bottom += values[i]

ax.set_ylabel('Percentage')
ax.set_title('Music Genre Popularity Distribution')
ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1))

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()