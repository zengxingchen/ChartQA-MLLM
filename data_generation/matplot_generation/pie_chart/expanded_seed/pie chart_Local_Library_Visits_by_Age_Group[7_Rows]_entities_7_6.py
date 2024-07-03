
import matplotlib.pyplot as plt

# Data from your table
age_groups = ['0-12', '13-18', '19-25', '26-35', '36-50', '51-65', 'Over 65']
visits = [320, 450, 390, 610, 720, 530, 470]

# Defining colors for each age group
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6', '#c4e17f']

# Exploding the '26-35' age group
explode = (0, 0, 0, 0.1, 0, 0, 0)  # only "explode" the 4th slice (i.e., '26-35')

# Create a pie chart
plt.figure(figsize=(10, 7))  # Set the figure size
plt.pie(visits, labels=age_groups, colors=colors, autopct='%1.1f%%', startangle=140, explode=explode)

# Draw a circle at the center to make it a donut chart
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')  

plt.title('Number of Visits by Age Group')

# Show the plot
plt.show()