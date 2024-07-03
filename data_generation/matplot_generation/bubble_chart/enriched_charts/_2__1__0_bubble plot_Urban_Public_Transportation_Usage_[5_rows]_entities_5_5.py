
import matplotlib.pyplot as plt
import numpy as np

categories = [
    'Soccer', 'Basketball', 'Cricket', 'Tennis', 'Baseball', 'Rugby', 
    'Golf', 'Formula 1', 'Boxing', 'MMA', 'Athletics', 'Cycling', 
    'Swimming', 'Gymnastics', 'Esports'
]
viewers = np.array([330, 300, 275, 200, 150, 120, 100, 180, 160, 140, 110, 90, 130, 85, 210])
time_spent = np.array([15, 12, 13, 10, 8, 7, 5, 9, 8, 6, 4, 5, 6, 3, 11])
popularity_score = np.array([95, 90, 85, 80, 70, 65, 60, 75, 72, 68, 55, 50, 62, 45, 77])

sizes = viewers * 2

colors = [
    '#1f78b4', '#33a02c', '#e31a1c', '#ff7f00', '#6a3d9a', '#b15928', 
    '#a6cee3', '#b2df8a', '#fb9a99', '#fdbf6f', '#cab2d6', '#ffff99', 
    '#ff9896', '#8dd3c7', '#bc80bd'
]

plt.figure(figsize=(18, 10))

scatter = plt.scatter(time_spent, viewers, s=sizes, c=colors, alpha=0.6, edgecolors="w", linewidth=2)

plt.title('Popularity and Engagement in Sports by Category', pad=20)
plt.xlabel('Time Spent (Hours per Week)')
plt.ylabel('Viewers (Million)')

for i, category in enumerate(categories):
    plt.annotate(category, (time_spent[i], viewers[i]), textcoords="offset points", xytext=(0,10), ha='center')

plt.tight_layout()
plt.show()