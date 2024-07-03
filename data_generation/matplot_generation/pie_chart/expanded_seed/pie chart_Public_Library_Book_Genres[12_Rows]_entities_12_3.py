
import matplotlib.pyplot as plt

# Data from the table
data = [
    {'Genre': 'Mystery', 'Number of Checkouts': 435},
    {'Genre': 'Fantasy', 'Number of Checkouts': 390},
    {'Genre': 'Science Fiction', 'Number of Checkouts': 350},
    {'Genre': 'Non-Fiction', 'Number of Checkouts': 480},
    {'Genre': 'Romance', 'Number of Checkouts': 320},
    {'Genre': 'Historical', 'Number of Checkouts': 300},
    {'Genre': 'Biographies', 'Number of Checkouts': 220},
    {'Genre': 'Self-Help', 'Number of Checkouts': 180},
    {'Genre': "Children's Books", 'Number of Checkouts': 570},
    {'Genre': 'Young Adult', 'Number of Checkouts': 460},
    {'Genre': 'Graphic Novels', 'Number of Checkouts': 250},
    {'Genre': 'Cookbooks', 'Number of Checkouts': 190}
]

# Extracting genres and the number of checkouts
genres = [entry['Genre'] for entry in data]
checkouts = [entry['Number of Checkouts'] for entry in data']

# Generating colors for each genre
colors = plt.cm.tab20c.colors  # using the tab20c colormap for diverse colors

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
fig, ax = plt.subplots()
wedges, texts, autotexts = ax.pie(checkouts, labels=genres, colors=colors,
                                  autopct='%1.1f%%', startangle=140, textprops=dict(color="w"))

# Draw a circle at the center of pie to make it look like a donut
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle.
ax.axis('equal')

# Annotating with genre labels
plt.setp(texts, size=8, weight="bold")
ax.set_title('Checkout Distribution by Genre')

# Legend with genre labels
ax.legend(wedges, genres,
          title="Genres",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.show()