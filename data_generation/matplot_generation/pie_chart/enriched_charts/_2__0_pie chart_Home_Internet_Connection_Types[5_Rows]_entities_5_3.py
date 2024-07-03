
import matplotlib.pyplot as plt

# Data
categories = ['Pop', 'Rock', 'Hip-Hop', 'Classical', 'Jazz', 'Country']
popularity = [30.1, 25.6, 20.4, 10.7, 8.3, 4.9]
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#8A2BE2', '#FF69B4']

# Create a pie chart
plt.figure(figsize=(12, 8))
plt.pie(popularity, labels=categories, autopct='%1.1f%%', startangle=140, colors=colors)

# Title
plt.title('Popularity of Music Genres in 2023', y=1.08)

# Display the chart
plt.show()