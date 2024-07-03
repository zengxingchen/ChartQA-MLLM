
import matplotlib.pyplot as plt

# Data to plot
labels = ['Reading', 'Exercising', 'Watching TV', 'Gaming', 'Cooking', 'Social Media', 'Working', 'Sleeping', 'Hobbies', 'Family Time']
sizes = [12, 8, 14, 10, 9, 11, 15, 7, 6, 8]
colors = ['#ff6347','#4682b4','#32cd32','#ff8c00','#8a2be2','#00ced1','#d2691e','#ffb6c1','#6495ed','#dda0dd']

# Plot
fig1, ax1 = plt.subplots(figsize=(12, 8))
ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

# Draw circle for donut chart
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
ax1.axis('equal')

plt.title('Daily Time Allocation by Activity', y=1.08)
plt.show()