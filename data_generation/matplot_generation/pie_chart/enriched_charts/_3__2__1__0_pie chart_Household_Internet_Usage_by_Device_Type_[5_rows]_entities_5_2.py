
import matplotlib.pyplot as plt

# Data for the pie chart
genres = ['Fantasy', 'Mystery', 'Science Fiction', 'Historical Fiction', 'Romance', 'Thriller', 'Non-Fiction', 'Biography', 'Poetry']
popularity = [22.3, 18.7, 15.0, 13.5, 11.0, 8.5, 6.0, 3.0, 2.0]

# Colors for each section of the pie chart
colors = ['#8A2BE2', '#5F9EA0', '#D2691E', '#FF7F50', '#6495ED', '#DC143C', '#00FFFF', '#FFD700', '#ADFF2F']

# Create a pie chart
plt.figure(figsize=(16, 10))  # Modify the size of the chart
plt.pie(popularity, labels=genres, colors=colors, startangle=90, autopct='%1.1f%%', pctdistance=0.85)

# Draw a circle at the center to turn the pie chart into a donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Set the title of the chart
plt.title('Popular Book Genres in 2023', y=1.05)

# Equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')

# Show the chart
plt.show()