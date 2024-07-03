
import matplotlib.pyplot as plt

# Table data
data = [
    {'Genre': 'Mystery', 'Number of Books': 340},
    {'Genre': 'Science Fiction', 'Number of Books': 280},
    {'Genre': 'Romance', 'Number of Books': 390},
    {'Genre': 'Biographies', 'Number of Books': 200},
    {'Genre': "Children's Literature", 'Number of Books': 450},
    {'Genre': 'Non-fiction', 'Number of Books': 300},
    {'Genre': 'Young Adult', 'Number of Books': 220},
    {'Genre': 'Self-help', 'Number of Books': 120}
]

# Extracting the labels and values
genres = [entry['Genre'] for entry in data]
book_counts = [entry['Number of Books'] for entry in data]

# Diversifying the visualization with colors and explode
colors = plt.cm.Paired(range(len(genres)))
explode = [0.05 if book_count == max(book_counts) else 0.01 for book_count in book_counts]

# Creating the pie chart
plt.figure(figsize=(10, 6))
plt.pie(book_counts, labels=genres, autopct='%1.1f%%', colors=colors, explode=explode, startangle=140, shadow=True)

# Draw a circle at the center to transform it into a donut chart
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.title('Distribution of Books by Genre')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Display the chart
plt.show()