
import matplotlib.pyplot as plt
import squarify

# Data points
landmarks = [
    'Eiffel Tower', 'Great Wall of China', 'Machu Picchu', 'Statue of Liberty', 
    'Louvre Museum', 'Taj Mahal', 'Colosseum', 'Christ the Redeemer', 
    'Acropolis of Athens', 'Sydney Opera House', 'Great Pyramid of Giza', 
    'Golden Gate Bridge'
]
visitors = [6.91, 10, 1.5, 4.3, 10.2, 7.8, 7.6, 2, 2.5, 8.2, 14.7, 10]
entry_fees = [25, 10, 50, 23, 17, 15, 16, 12, 20, 40, 10, 0]

# Color scheme using specific color codes
colors = [
    '#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#FF8F33', 
    '#33FFF2', '#F233FF', '#FF3333', '#33FFA8', '#A8FF33',
    '#FF5733', '#33FF57'
]

# Create a figure with altered width and height
fig, ax = plt.subplots(figsize=(16, 12))

# Creating a treemap
squarify.plot(sizes=visitors, label=landmarks, color=colors, alpha=0.8, value=entry_fees, edgecolor='white', linewidth=2)

# Chart title and subtitle
plt.title('Visitor Statistics of Famous Landmarks', fontsize=20, color='darkblue')
plt.suptitle('Yearly Visitors and Entry Fees', fontsize=24, color='navy')

# Remove the axes
plt.axis('off')

# Show plot
plt.show()