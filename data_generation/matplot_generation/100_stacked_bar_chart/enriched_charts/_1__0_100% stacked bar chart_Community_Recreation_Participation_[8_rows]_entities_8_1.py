
import matplotlib.pyplot as plt
import numpy as np

# Data
activities = ["Sleeping", "Working", "Exercising", "Eating", "Socializing", "Relaxing"]
very_positive = np.array([25, 10, 40, 30, 20, 35])
positive = np.array([50, 30, 35, 40, 30, 35])
neutral = np.array([15, 25, 15, 20, 25, 20])
negative = np.array([5, 20, 5, 5, 15, 5])
very_negative = np.array([5, 15, 5, 5, 10, 5])

# Stack data for percentage stacked bar chart
totals = very_positive + positive + neutral + negative + very_negative
very_positive_perc = very_positive / totals * 100
positive_perc = positive / totals * 100
neutral_perc = neutral / totals * 100
negative_perc = negative / totals * 100
very_negative_perc = very_negative / totals * 100

bar_width = 0.85

# Plotting
fig, ax = plt.subplots(figsize=(14, 7))

# Horizontal bar chart
bars1 = ax.barh(activities, very_positive_perc, color='#1f77b4', edgecolor='white', height=bar_width, label='Very Positive')
bars2 = ax.barh(activities, positive_perc, left=very_positive_perc, color='#ff7f0e', edgecolor='white', height=bar_width, label='Positive')
bars3 = ax.barh(activities, neutral_perc, left=very_positive_perc + positive_perc, color='#2ca02c', edgecolor='white', height=bar_width, label='Neutral')
bars4 = ax.barh(activities, negative_perc, left=very_positive_perc + positive_perc + neutral_perc, color='#d62728', edgecolor='white', height=bar_width, label='Negative')
bars5 = ax.barh(activities, very_negative_perc, left=very_positive_perc + positive_perc + neutral_perc + negative_perc, color='#9467bd', edgecolor='white', height=bar_width, label='Very Negative')

# Title and labels
plt.title('Impact of Daily Activities on Mental Well-being', pad=20)
ax.set_xlabel('Percentage')
ax.set_ylabel('Activity')

# Legend
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

# Show plot
plt.tight_layout()
plt.show()