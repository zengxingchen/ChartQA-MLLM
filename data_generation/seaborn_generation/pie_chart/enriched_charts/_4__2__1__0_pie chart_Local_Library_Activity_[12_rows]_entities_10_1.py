
import matplotlib.pyplot as plt

# Data to plot
activities = ['Exploring Ruins', 'Artifact Analysis', 'Field Surveys', 'Museum Visits', 'Documentary Research', 'Conference Talks', 'Lab Experiments', 'Historical Mapping', 'Cataloging Finds', 'Restoration Projects', 'Digital Archiving']
time_spent = [4.0, 3.0, 3.5, 2.0, 2.5, 1.5, 2.0, 3.0, 2.5, 2.0, 1.5]
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#8A2BE2', '#FF7F50', '#3CB371', '#6A5ACD', '#D2691E', '#9ACD32', '#20B2AA']

# Plot pie chart
plt.figure(figsize=(12, 8))
plt.pie(time_spent, labels=activities, colors=colors, autopct='%1.1f%%', startangle=140)

# Draw a circle at the center of pie to make it look like a donut
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')

plt.title('Time Allocation for Archaeological Activities', pad=40)
plt.show()