
import matplotlib.pyplot as plt

# Data
genres = [
    "Action", 
    "Comedy", 
    "Drama", 
    "Horror", 
    "Sci-Fi", 
    "Romantic", 
    "Documentary", 
    "Animation", 
    "Musical"
]
popularity = [300, 250, 200, 150, 100, 80, 60, 50, 30]

# Colors
colors = [
    "#FF5733",  # Action
    "#33FF57",  # Comedy
    "#3357FF",  # Drama
    "#FF33A5",  # Horror
    "#A533FF",  # Sci-Fi
    "#FFD433",  # Romantic
    "#33FFD4",  # Documentary
    "#FF3333",  # Animation
    "#33FFF2"   # Musical
]

# Create pie chart
plt.figure(figsize=(14, 10))  # width and height in inches
plt.pie(popularity, labels=genres, colors=colors, autopct='%1.1f%%', startangle=140)

# Chart title
plt.title('Popularity of Different Movie Genres in 2023', pad=40)

# Show plot
plt.show()