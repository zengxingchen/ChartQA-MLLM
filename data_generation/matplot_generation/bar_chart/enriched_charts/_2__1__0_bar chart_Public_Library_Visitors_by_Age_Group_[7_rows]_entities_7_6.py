
import matplotlib.pyplot as plt

# Data
genres = [
    "Fiction", "Non-Fiction", "Fantasy", "Science Fiction",
    "Mystery", "Romance", "Horror", "Thriller",
    "Historical", "Biography", "Children", "Young Adult",
    "Graphic Novels", "Self-Help"
]
sales = [150, 180, 120, 90, 130, 170, 80, 110, 100, 140, 160, 200, 190, 210]

# Creating horizontal bar chart
fig, ax = plt.subplots(figsize=(12, 8))

ax.barh(genres, sales, color=[
    '#FF5733', '#33FF57', '#3357FF', '#FF33A6',
    '#FF8C33', '#33FFF7', '#FF3333', '#33FF8C',
    '#8C33FF', '#FF3380', '#33FFB8', '#FF333D',
    '#33A6FF', '#FF6A33'
], height=0.5)  # Change bar color and height

# Adding labels and title
ax.set_xlabel('Sales (in thousands)')
ax.set_title('Book Genre Sales in 2023', pad=20)

# Show the plot
plt.show()