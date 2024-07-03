
import matplotlib.pyplot as plt

# Your data
data = [
    {'Device Type': 'Smartphones', 'Percentage of Use': '40%'},
    {'Device Type': 'Laptops', 'Percentage of Use': '30%'},
    {'Device Type': 'Desktop PCs', 'Percentage of Use': '15%'},
    {'Device Type': 'Tablets', 'Percentage of Use': '10%'},
    {'Device Type': 'Smart TVs', 'Percentage of Use': '5%'}
]

# Parsing the data
labels = [item['Device Type'] for item in data]
sizes = [float(item['Percentage of Use'].rstrip('%')) for item in data]

# Define colors for each slice
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']

# Explode the 1st slice (Smartphones)
explode = (0.1, 0, 0, 0, 0)  

# Create the pie chart
plt.figure(figsize=(8, 8))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

# Draw a circle at the center of pie to make it look like a donut
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')  

# Add a title
plt.title('Percentage Use of Devices')

# Display the chart
plt.show()