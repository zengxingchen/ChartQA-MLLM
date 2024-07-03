
import matplotlib.pyplot as plt

# Data
movie_categories = ["Action", "Drama", "Comedy", "Horror", "Science Fiction", "Romance", "Documentary", "Animation", "Fantasy"]
amount_watched = [20, 15, 25, 10, 12, 18, 8, 5, 14]

# Colors
colors = [
    "#FF6347",  # Action
    "#4682B4",  # Drama
    "#FFD700",  # Comedy
    "#8A2BE2",  # Horror
    "#00FA9A",  # Science Fiction
    "#FF69B4",  # Romance
    "#8B4513",  # Documentary
    "#20B2AA",  # Animation
    "#FF4500",  # Fantasy
]

# Create pie chart
plt.figure(figsize=(10, 8))  # width and height in inches
plt.pie(amount_watched, labels=movie_categories, colors=colors, autopct='%1.1f%%', startangle=140)

# Chart title
plt.title('Monthly Movie Watching Habits by Genre (in hours)', pad=20)

# Show plot
plt.show()