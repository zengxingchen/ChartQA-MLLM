
import matplotlib.pyplot as plt

# Data points
genres = [
    'Action', 'Comedy', 'Drama', 'Horror', 'Sci-Fi', 
    'Romance', 'Thriller', 'Animation', 'Documentary', 'Fantasy'
]

popularity = [
    20.5, 18.0, 16.2, 10.7, 9.8, 
    8.3, 7.4, 5.6, 2.5, 1.0
]

# Colors for each section
colors = [
    '#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A133FF',
    '#33FFA1', '#FFA133', '#A1FF33', '#5733FF', '#FF33C5'
]

# Resize the chart
plt.figure(figsize=(12, 8))

# Create the pie chart
plt.pie(popularity, labels=genres, colors=colors, autopct='%1.1f%%', startangle=140)

# Set the title
plt.title('Popularity of Movie Genres in 2023', fontsize=14, pad=20)

# Display the chart
plt.show()