
import matplotlib.pyplot as plt

# Data provided
data = [
    {'Appliance': 'HVAC Systems', 'Percentage of Energy Use': 46},
    {'Appliance': 'Water Heater', 'Percentage of Energy Use': 14},
    {'Appliance': 'Washer and Dryer', 'Percentage of Energy Use': 13},
    {'Appliance': 'Lighting', 'Percentage of Energy Use': 12},
    {'Appliance': 'Refrigerator', 'Percentage of Energy Use': 9}
]

# Extracting the appliance labels and corresponding percentages for the pie chart
labels = [item['Appliance'] for item in data]
sizes = [item['Percentage of Energy Use'] for item in data]

# Colors for each section
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99', '#c2c2f0']

# Explode the 1st slice (HVAC Systems)
explode = (0.1, 0, 0, 0, 0)  

# Plotting the pie chart
plt.figure(figsize=(8, 8))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

# Draw a circle at the center to turn the pie into a donut chart
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')  

# Adding a title
plt.title('Percentage of Household Energy Use by Appliance')

# Show the plot
plt.show()