
import matplotlib.pyplot as plt

# Provided data
data = [
    {'Resource': 'Adult Fiction Books', 'Checkouts': 950},
    {'Resource': 'Adult Non-fiction Books', 'Checkouts': 850},
    {'Resource': "Children's Books", 'Checkouts': 1200},
    {'Resource': 'E-books', 'Checkouts': 650},
    {'Resource': 'Audiobooks', 'Checkouts': 450},
    {'Resource': 'DVDs/Blu-rays', 'Checkouts': 350},
    {'Resource': 'Magazines/Journals', 'Checkouts': 300},
    {'Resource': 'Music CDs', 'Checkouts': 150},
    {'Resource': 'Video Games', 'Checkouts': 80},
    {'Resource': 'Research Databases', 'Checkouts': 70},
    {'Resource': 'Local History Archives', 'Checkouts': 50},
    {'Resource': 'Meeting Room Usage', 'Checkouts': 40}
]

# Extracting resource names and checkout counts as separate lists
labels = [item['Resource'] for item in data]
sizes = [item['Checkouts'] for item in data]

# Define color for each slice
colors = plt.cm.tab20.colors  # Using tab20 colormap for a variety of colors

# Figure Size
plt.figure(figsize=(10,8))

# Exploding the 1st, 4th and 7th slice for emphasis
explode = (0.1, 0, 0, 0.1, 0, 0, 0.1) + (0,) * (len(data) - 7)

# Create a pie chart
plt.pie(sizes, labels=labels, colors=colors, explode=explode, autopct='%1.1f%%', startangle=140)

# Draw a circle in the center to turn the pie into a donut
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')  

# Title of the pie chart
plt.title('Library Resource Checkouts Distribution')

# Legend
plt.legend(labels, title="Resources", loc="best", bbox_to_anchor=(1, 0, 0.5, 1))

# Show the plot
plt.tight_layout()
plt.show()