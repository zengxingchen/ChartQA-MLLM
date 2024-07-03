
import matplotlib.pyplot as plt
import squarify

# Dataset
categories = [
    'Painting', 'Sculpture', 'Photography', 'Graphic Design', 'Fashion Design', 
    'Interior Design', 'Architecture', 'Ceramics', 'Printmaking', 'Illustration', 
    'Digital Art', 'Industrial Design', 'Calligraphy', 'Textile Art', 'Video Art', 
    'Performance Art', 'Mixed Media', 'Jewelry Design', 'Glass Art', 'Conceptual Art'
]
counts = [
    200, 180, 250, 150, 130, 160, 220, 90, 70, 140, 
    110, 100, 80, 120, 60, 50, 85, 75, 95, 40
]

# Color Scheme
colors = [
    '#FFB6C1', '#FFA07A', '#FA8072', '#E9967A', '#F08080', 
    '#CD5C5C', '#DC143C', '#FF0000', '#B22222', '#8B0000', 
    '#FF6347', '#FF4500', '#FF8C00', '#FFA500', '#FFD700', 
    '#FFFF00', '#FFFFE0', '#FFFACD', '#FAFAD2', '#FFEFD5'
]

plt.figure(figsize=(18, 14))

# Creating the treemap
squarify.plot(sizes=counts, label=categories, color=colors, alpha=0.8)

# Adding a title
plt.title('Popularity of Art & Design Disciplines', fontsize=22, weight='bold')

# Removing the axes
plt.axis('off')

# Display the plot
plt.show()