
import matplotlib.pyplot as plt

# Data to plot
activities = ['Exercise', 'Meditation', 'Reading', 'Socializing', 'Hobbies', 'Therapy', 'Sleep', 'Nature Walks']
hours = [6, 4, 5, 7, 3, 2, 8, 5]
colors = ['#FF6347', '#4682B4', '#FFD700', '#8A2BE2', '#20B2AA', '#FF69B4', '#ADFF2F', '#7B68EE']

# Create pie chart
plt.figure(figsize=(10, 7))
plt.pie(hours, labels=activities, colors=colors, autopct='%1.1f%%', startangle=140)

# Draw a circle at the center of pie to make it look like a donut
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Weekly Activities for Mental Wellness', pad=20)
plt.show()