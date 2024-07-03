
import matplotlib.pyplot as plt

# Data from the provided table
data = [
    {'Source': 'Product Sales', 'Percentage of Revenue': '50%'},
    {'Source': 'Service Income', 'Percentage of Revenue': '30%'},
    {'Source': 'Subscription Fees', 'Percentage of Revenue': '10%'},
    {'Source': 'Commission Income', 'Percentage of Revenue': '5%'},
    {'Source': 'Rental Income', 'Percentage of Revenue': '5%'}
]

# Extracting the labels and the corresponding percentages
labels = [item['Source'] for item in data]
percentages = [float(item['Percentage of Revenue'].strip('%')) for item in data]

# Colors to distinguish each section
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99', '#c2c2f0']

# Explode the first slice (Product Sales) to highlight it
explode = (0.1, 0, 0, 0, 0)

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(percentages, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)

# Draw a circle at the center to turn it into a donut chart
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')  

# Add a legend
plt.legend(labels, loc="best")

# Title for the chart
plt.title('Revenue Sources')

# Show the chart
plt.show()