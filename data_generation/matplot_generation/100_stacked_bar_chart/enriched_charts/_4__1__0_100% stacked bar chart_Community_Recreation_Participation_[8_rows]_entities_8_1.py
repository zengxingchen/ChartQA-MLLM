
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ["Walking", "Reading", "Gardening", "Cooking", "Meditation", "Painting"]
very_positive = np.array([20, 30, 25, 15, 35, 25])
positive = np.array([40, 35, 35, 40, 30, 25])
neutral = np.array([20, 15, 20, 25, 20, 25])
negative = np.array([10, 10, 15, 10, 10, 15])
very_negative = np.array([10, 10, 5, 10, 5, 10])

# Stack data for percentage stacked bar chart
totals = very_positive + positive + neutral + negative + very_negative
very_positive_perc = very_positive / totals * 100
positive_perc = positive / totals * 100
neutral_perc = neutral / totals * 100
negative_perc = negative / totals * 100
very_negative_perc = very_negative / totals * 100

bar_width = 0.65

# Plotting
fig, ax = plt.subplots(figsize=(10, 12))

# Vertical bar chart
bars1 = ax.bar(categories, very_positive_perc, color='#1f77b4', edgecolor='white', width=bar_width, label='Very Positive')
bars2 = ax.bar(categories, positive_perc, bottom=very_positive_perc, color='#ff7f0e', edgecolor='white', width=bar_width, label='Positive')
bars3 = ax.bar(categories, neutral_perc, bottom=very_positive_perc + positive_perc, color='#2ca02c', edgecolor='white', width=bar_width, label='Neutral')
bars4 = ax.bar(categories, negative_perc, bottom=very_positive_perc + positive_perc + neutral_perc, color='#d62728', edgecolor='white', width=bar_width, label='Negative')
bars5 = ax.bar(categories, very_negative_perc, bottom=very_positive_perc + positive_perc + neutral_perc + negative_perc, color='#9467bd', edgecolor='white', width=bar_width, label='Very Negative')

# Title and labels
plt.title('Impact of Various Activities on Emotional Well-being', pad=20)
ax.set_ylabel('Percentage')
ax.set_xlabel('Activity')

# Legend
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

# Show plot
plt.tight_layout()
plt.show()