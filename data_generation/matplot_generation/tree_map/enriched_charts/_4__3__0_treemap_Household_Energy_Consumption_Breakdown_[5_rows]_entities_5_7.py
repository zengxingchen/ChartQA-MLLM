
import matplotlib.pyplot as plt
import squarify

# Data points
regions = [
    'Louvre Museum', 'British Museum', 'Metropolitan Museum of Art', 
    'Vatican Museums', 'Smithsonian Institution', 'Tate Modern', 
    'National Gallery', 'Musée d\'Orsay', 'Rijksmuseum', 
    'State Hermitage Museum', 'Uffizi Gallery', 'Guggenheim Museum', 
    'Museum of Modern Art', 'Centre Pompidou', 'Art Institute of Chicago'
]
number_of_exhibits = [
    35000, 25000, 28000, 27000, 30000, 24000, 26000, 22000, 
    23000, 31000, 20000, 18000, 26000, 19000, 27000
]
visitor_count = [
    5000000, 6000000, 4700000, 4500000, 7000000, 4200000, 
    5200000, 3700000, 3400000, 6200000, 3200000, 2800000, 
    4500000, 2900000, 3500000
]

# Color scheme using specific color codes
colors = [
    '#FF6347', '#4682B4', '#32CD32', '#FFD700', '#FF4500',
    '#98FB98', '#DA70D6', '#87CEEB', '#FF69B4', '#20B2AA',
    '#9370DB', '#FFC0CB', '#00CED1', '#8A2BE2', '#7FFF00'
]

# Create a figure with altered width and height
fig, ax = plt.subplots(figsize=(16, 12))

# Creating a treemap
squarify.plot(sizes=number_of_exhibits, label=regions, color=colors, alpha=0.8, value=visitor_count, edgecolor='white', linewidth=2)

# Chart title and subtitle
plt.title('Museum Exhibits and Visitor Count by Institution', fontsize=18, color='darkblue')
plt.suptitle('Cultural Impact of Global Museums', fontsize=22)

# Remove the axes
plt.axis('off')

# Show plot
plt.show()