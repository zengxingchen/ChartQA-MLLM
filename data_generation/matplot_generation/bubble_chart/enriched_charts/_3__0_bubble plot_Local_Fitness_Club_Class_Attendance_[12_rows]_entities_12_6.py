
import matplotlib.pyplot as plt

# Data
categories = ['Reading', 'Music', 'Exercise', 'Cooking', 'Gaming', 'Traveling', 'Socializing', 'Movies', 'Gardening', 'Photography', 'Dancing', 'Writing']
hours_per_week = [5.5, 7.0, 3.5, 4.0, 6.0, 2.5, 8.0, 5.0, 3.0, 4.5, 6.5, 4.0]
population = [1600, 2500, 2200, 1800, 2100, 1700, 2600, 2400, 1500, 2000, 2300, 1900]
colors = ['#FF5733', '#FFC300', '#7ED957', '#5797ED', '#B457ED', '#ED579E', '#57EDE3', '#FF5733', '#FFC300', '#7ED957', '#5797ED', '#B457ED']
sizes = [i / 10 for i in population]

fig, ax = plt.subplots(figsize=(12, 8))

# Bubble chart
for i in range(len(categories)):
    ax.scatter(categories[i], hours_per_week[i], s=sizes[i], alpha=0.6, color=colors[i])

# Title and labels
ax.set_title('Average Weekly Hours Spent on Leisure Activities', pad=20)
ax.set_xlabel('Activity')
ax.set_ylabel('Hours per Week')

plt.show()