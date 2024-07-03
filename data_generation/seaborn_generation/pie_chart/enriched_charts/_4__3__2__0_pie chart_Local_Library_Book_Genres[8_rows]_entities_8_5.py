
import matplotlib.pyplot as plt

# Data points
genres = [
    'Pop', 'Rock', 'Hip-Hop', 'Classical', 'Jazz', 
    'Country', 'Reggae', 'Electronic', 'Blues', 'Folk'
]

popularity = [
    22.5, 18.0, 14.0, 12.0, 10.0, 
    8.5, 6.0, 5.5, 2.5, 1.0
]

# Colors for each section
colors = [
    '#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0',
    '#ffb3e6', '#ff6666', '#c4e17f', '#ffcc80', '#99ffcc'
]

# Resize the chart
plt.figure(figsize=(12, 7))

# Create the pie chart
plt.pie(popularity, labels=genres, colors=colors, autopct='%1.1f%%', startangle=140)

# Set the title
plt.title('Popularity of Music Genres in 2023', pad=30)

# Display the chart
plt.show()