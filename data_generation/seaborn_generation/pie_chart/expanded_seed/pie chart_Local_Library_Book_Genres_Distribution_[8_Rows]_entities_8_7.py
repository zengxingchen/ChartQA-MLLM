
import matplotlib.pyplot as plt

# Data
chart_data = [
    {'Genre': 'Fiction', 'Percentage': '35%'},
    {'Genre': 'Non-Fiction', 'Percentage': '25%'},
    {'Genre': "Children's Literature", 'Percentage': '15%'},
    {'Genre': 'Young Adult', 'Percentage': '10%'},
    {'Genre': 'Biographies', 'Percentage': '5%'},
    {'Genre': 'Science Fiction', 'Percentage': '4%'},
    {'Genre': 'Mystery', 'Percentage': '3%'},
    {'Genre': 'Graphic Novels', 'Percentage': '3%'}
]

# Parsing data into lists for the pie chart
labels = [item['Genre'] for item in chart_data]
sizes = [int(item['Percentage'].rstrip('%')) for item in chart_data]

# Colors for each section
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6', '#c4e17f', '#76d7c4']

# Explode the 1st slice (Fiction)
explode = (0.1, 0, 0, 0, 0, 0, 0, 0)

# Create the pie chart
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, colors=colors, explode=explode, autopct='%1.1f%%', startangle=140)

# Draw a circle at the center of pie to make it look like a donut
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')

plt.title('Book Genre Distribution')
plt.show()