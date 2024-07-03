
import matplotlib.pyplot as plt
import squarify

# Data
categories = [
    'Flights', 'Accommodation', 'Food', 'Transport', 'Tours', 'Souvenirs', 
    'Insurance', 'Gear', 'Visas', 'Guidebooks', 'Vaccinations', 'Entertainment', 
    'Gifts', 'Emergencies', 'Miscellaneous', 'Internet', 'Laundry', 'Donations'
]
amounts = [
    800, 1200, 500, 300, 400, 150, 200, 350, 100, 50, 75, 200, 100, 150, 100, 
    50, 30, 20
]
colors = [
    '#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A133FF', '#FF9C33', '#33FFDA',
    '#FF5733', '#57FF33', '#3357FF', '#FF33A1', '#A133FF', '#FF9C33', '#33FFDA',
    '#FF5733', '#33FF57', '#3357FF', '#FF33A1'
]

# Creating a figure to accommodate a larger treemap
fig, ax = plt.subplots(1, figsize=(16, 8))

# Creating the treemap
squarify.plot(sizes=amounts, label=categories, color=colors, alpha=0.8, ax=ax)

# Title of the treemap
plt.title('Backpacking Trip Budget Breakdown', fontsize=20, pad=20)

# Removing the axes for better aesthetic
plt.axis('off')

# Display the plot
plt.show()