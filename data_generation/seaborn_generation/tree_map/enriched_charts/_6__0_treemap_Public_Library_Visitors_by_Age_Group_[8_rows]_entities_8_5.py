
import matplotlib.pyplot as plt
import squarify

# Data points for the treemap
categories = ['Running', 'Cycling', 'Swimming', 'Yoga', 'Hiking', 'Pilates', 'Weightlifting', 'Boxing', 'Dancing', 'Climbing', 'Skating', 'Skiing', 'Rowing', 'Surfing', 'Tennis', 'Golf', 'Martial Arts', 'Basketball', 'Soccer']
count = [1350, 1150, 950, 850, 800, 750, 700, 650, 600, 550, 500, 450, 400, 350, 300, 250, 200, 150, 100]

# TreeMap customization
color_palette = ['#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#33FFA8', '#A833FF', '#FFD133', '#D1FF33', '#33FFF5', '#F533FF', '#33D1FF', '#FF5733', '#8D33FF', '#33FF8D', '#FF3385', '#85FF33', '#33FF85', '#FF338D', '#338DFF']
plt.figure(figsize=(18, 10))

# Creating the treemap
squarify.plot(sizes=count, label=categories, color=color_palette, alpha=0.8)

# Title and labels
plt.title('Participation in Various Sports & Fitness Activities', fontsize=18, fontweight='bold')
plt.axis('off')

plt.show()