
import matplotlib.pyplot as plt

# Data from the provided table
data = [
    {'Genre': 'Fantasy', 'Checkout Count': 450},
    {'Genre': 'Science Fiction', 'Checkout Count': 300},
    {'Genre': 'Mystery', 'Checkout Count': 500},
    {'Genre': 'Romance', 'Checkout Count': 350},
    {'Genre': 'Biographies', 'Checkout Count': 200},
    {'Genre': "Children's Books", 'Checkout Count': 600},
    {'Genre': 'Young Adult', 'Checkout Count': 480},
    {'Genre': 'Graphic Novels', 'Checkout Count': 320}
]

# Extracting the corresponding data for plotting
genres = [item['Genre'] for item in data]
checkout_counts = [item['Checkout Count'] for item in data]

# Specify the color for each pie slice
colors = plt.cm.Paired(range(len(genres)))

# Explode the largest piece (Children's Books in this case)
explode = [0.1 if genre == "Children's Books" else 0 for genre in genres]

# Create the pie chart
plt.figure(figsize=(10, 8))
plt.pie(checkout_counts, explode=explode, labels=genres, autopct=lambda p: '{:.0f}%\n({:.0f})'.format(p, (p/100)*sum(checkout_counts)), colors=colors, startangle=140)

# Draw a circle at the center of pie to make it look like a donut
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')

# Adding a title to the pie chart
plt.title('Checkout Counts by Genre', pad=20)

# Display the chart
plt.show()