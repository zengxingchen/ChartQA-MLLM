
import matplotlib.pyplot as plt
import squarify

# Data for the treemap
labels = [
    'Fantasy', 'Science Fiction', 'Mystery', 'Romance', 
    'Historical Fiction', 'Horror', 'Thriller', 'Non-fiction', 
    'Biography', 'Poetry', 'Drama', 'Graphic Novels', 
    "Children's Literature", 'Classics'
]
sizes = [20, 18, 15, 12, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
colors = [
    '#4B0082', '#8A2BE2', '#7FFF00', '#DC143C', 
    '#00FFFF', '#FF7F50', '#FF1493', '#696969', 
    '#FFD700', '#ADFF2F', '#FF69B4', '#CD5C5C', 
    '#F08080', '#20B2AA'
]

# Create a figure of specified width and height
plt.figure(figsize=(16, 9))

# Create a treemap with specified data, labels, and color
squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.8)

# Set the title of the chart
plt.title('Popular Book Genres', fontsize=20)

# Remove the axis
plt.axis('off')

# Display the treemap
plt.show()