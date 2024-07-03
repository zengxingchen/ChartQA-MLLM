
import matplotlib.pyplot as plt
import squarify

# Dataset
categories = [
    'Classical', 'Jazz', 'Rock', 'Pop', 'Hip-Hop', 'Reggae', 'Blues', 'Electronic', 
    'Country', 'R&B', 'Folk', 'Latin', 'Metal', 'Punk', 'Soul', 'World', 
    'Gospel', 'Disco', 'K-Pop', 'Opera'
]
counts = [
    150, 120, 300, 250, 180, 75, 90, 220, 
    110, 140, 60, 130, 160, 50, 100, 85, 
    70, 65, 95, 40
]

# Color Scheme
colors = [
    '#FF5733', '#33FF57', '#3357FF', '#5710FF', '#FFD433', '#D4FF33', 
    '#D633FF', '#FF3357', '#33FFD4', '#571033', '#5733FF', '#FF5733', 
    '#33D4FF', '#57FF33', '#FFF333', '#FF33D4', '#D4D4D4', '#FFA333', 
    '#B8FF33', '#FF8333'
]

plt.figure(figsize=(16, 12))

# Creating the treemap
squarify.plot(sizes=counts, label=categories, color=colors, alpha=0.8)

# Adding a title
plt.title('Popularity of Music Genres', fontsize=20, weight='bold')

# Removing the axes
plt.axis('off')

# Display the plot
plt.show()