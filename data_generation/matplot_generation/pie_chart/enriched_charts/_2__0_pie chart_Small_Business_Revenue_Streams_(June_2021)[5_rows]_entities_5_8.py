
import matplotlib.pyplot as plt

# Data to plot
labels = ['Books', 'Art Supplies', 'Concert Tickets', 'Fitness Classes', 'Music', 'Electronics', 'Groceries', 'Clothing', 'Home & Kitchen', 'Travel']
sizes = [12, 8, 10, 9, 6, 15, 16, 10, 8, 6]
colors = ['#ff6666','#66b2ff','#99cc66','#ff9966','#c266ff','#ff66cc','#c2ccff','#66ff66','#ff9999','#66ffcc']

# Plot
fig1, ax1 = plt.subplots(figsize=(12, 8))
ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

# Draw circle for donut chart
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
ax1.axis('equal')

plt.title('Leisure and Lifestyle Expenses Distribution', pad=20)
plt.show()