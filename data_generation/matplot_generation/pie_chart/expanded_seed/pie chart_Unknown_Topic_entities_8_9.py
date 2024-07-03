
import matplotlib.pyplot as plt

# Data from the chart table
data = [
    {'Genre': 'Fiction', 'Percentage': '40%'},
    {'Genre': 'Non-Fiction', 'Percentage': '25%'},
    {'Genre': "Children's Literature", 'Percentage': '15%'},
    {'Genre': 'Young Adult', 'Percentage': '10%'},
    {'Genre': 'Biographies', 'Percentage': '5%'},
    {'Genre': 'Science Fiction', 'Percentage': '3%'},
    {'Genre': 'Self-Help', 'Percentage': '1%'},
    {'Genre': 'Others', 'Percentage': '1%'}
]

# Parse the percentage values to float and label names
percentages = [float(item['Percentage'].strip('%')) for item in data]
labels = [item['Genre'] for item in data]

# Generate color map
colors = plt.cm.tab20.colors[:len(data)]

# Create the pie chart
plt.figure(figsize=(10, 8))  # Set the figure size
plt.pie(percentages, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140, pctdistance=0.85)

# Draw a circle at the center to make it a donut chart
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')  

# Add legend to the chart
plt.legend(labels, title="Genres", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

plt.title('Book Genres Distribution')  # Add a title
plt.show()  # Display the chart