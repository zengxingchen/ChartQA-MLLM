
import matplotlib.pyplot as plt

# Data to plot
categories = ['Reading', 'Traveling', 'Gardening', 'Cooking', 'Sports', 'Music', 'Gaming', 'Photography']
values = [15, 10, 7, 8, 12, 9, 11, 6]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c266ff','#ffb3e6', '#ffcc66', '#c2c2f0']

# Create pie chart
plt.figure(figsize=(10, 6))
plt.pie(values, labels=categories, colors=colors, autopct='%1.1f%%', startangle=140)

# Draw a circle at the center of pie to make it look like a donut
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Community Favorite Hobbies', pad=20)
plt.show()