
import matplotlib.pyplot as plt

# Data to plot
labels = ['Cardio Exercises', 'Strength Training', 'Yoga', 'Meditation', 'Healthy Eating', 'Hydration', 'Sleep', 'Work-Life Balance', 'Hygiene', 'Mental Wellness']
sizes = [15, 10, 8, 5, 12, 6, 25, 7, 5, 7]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6','#c4e17f','#ffb347','#8dd3c7','#80b1d3']

# Plot
fig1, ax1 = plt.subplots(figsize=(10, 7))
ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

# Draw circle for donut chart
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
ax1.axis('equal')

plt.title('Daily Health and Wellness Activities', y=1.08)
plt.show()