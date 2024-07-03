
import matplotlib.pyplot as plt

# Data from the table
data = [
    {'Age Group': '0-8', 'Screen Time (hours)': 1.5},
    {'Age Group': '9-12', 'Screen Time (hours)': 3.0},
    {'Age Group': '13-18', 'Screen Time (hours)': 4.5},
    {'Age Group': '19-25', 'Screen Time (hours)': 6.5},
    {'Age Group': '26-35', 'Screen Time (hours)': 8.0},
    {'Age Group': '36-45', 'Screen Time (hours)': 6.0},
    {'Age Group': '46-65', 'Screen Time (hours)': 4.0}
]

# Extracting Age Groups and Screen Times
age_groups = [entry['Age Group'] for entry in data]
screen_times = [entry['Screen Time (hours)'] for entry in data]

# Colors for the pie chart sectors
colors = plt.get_cmap('tab20').colors

# Explode the 2nd and 3rd slice (9-12 & 13-18 age groups)
explode = (0, 0.1, 0.1, 0, 0, 0, 0)

# Creating the pie chart
plt.figure(figsize=(10, 6))
plt.pie(screen_times, labels=age_groups, autopct='%1.1f%%', startangle=140, colors=colors, explode=explode)

# Draw a circle at the center of pie to make it look like a donut
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')  

# Title for the pie chart
plt.title('Screen Time Distribution by Age Group')

# Display the pie chart
plt.show()