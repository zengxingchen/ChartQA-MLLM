
import matplotlib.pyplot as plt

# Data to plot
categories = ['Research', 'Writing', 'Editing', 'Field Work', 'Interviewing', 'Reading', 'Publishing', 'Networking', 'Data Analysis', 'Presentation']
time_spent = [2.5, 3, 1.5, 1.2, 0.8, 2.3, 0.7, 1.5, 2, 1]
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFF5', '#FF8C33', '#A833FF', '#FFD433', '#33FF8C', '#8C33FF']

# Plot pie chart
plt.figure(figsize=(12, 8))
plt.pie(time_spent, labels=categories, colors=colors, autopct='%1.1f%%', startangle=140)

# Draw a circle at the center of pie to make it look like a donut
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')

plt.title('Time Allocation in Literature & Writing Activities', pad=20)
plt.show()