
import matplotlib.pyplot as plt

# Data to plot
categories = ['Classical', 'Jazz', 'Rock', 'Pop', 'Hip-Hop', 'Country', 'Electronic', 'Reggae']
values = [100, 90, 130, 110, 70, 60, 80, 50]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f']

# Create pie chart
plt.figure(figsize=(14, 10))
plt.pie(values, labels=categories, colors=colors, autopct='%1.1f%%', startangle=140)

# Draw a circle at the center of pie to make it look like a donut
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Music Genres Popularity in 2023', pad=20)
plt.show()