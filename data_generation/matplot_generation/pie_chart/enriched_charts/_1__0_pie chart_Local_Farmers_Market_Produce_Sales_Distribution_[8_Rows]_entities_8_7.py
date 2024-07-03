
import matplotlib.pyplot as plt

# Data
genres = ["Fiction", "Non-Fiction", "Mystery", "Romance", "Science Fiction", "Fantasy", "Historical", "Biography", "Self-Help"]
books_sold = [300, 150, 100, 200, 120, 180, 80, 60, 90]

# Colors
colors = [
    "#FF5733",  # Fiction
    "#33FF57",  # Non-Fiction
    "#3357FF",  # Mystery
    "#FF33A5",  # Romance
    "#33FFF5",  # Science Fiction
    "#FFB533",  # Fantasy
    "#8D33FF",  # Historical
    "#33FFB5",  # Biography
    "#FF3385",  # Self-Help
]

# Create pie chart
plt.figure(figsize=(10, 8))  # width and height in inches
plt.pie(books_sold, labels=genres, colors=colors, autopct='%1.1f%%', startangle=140)

# Chart title
plt.title('Books Sold by Genre in 2023', pad=20)

# Show plot
plt.show()