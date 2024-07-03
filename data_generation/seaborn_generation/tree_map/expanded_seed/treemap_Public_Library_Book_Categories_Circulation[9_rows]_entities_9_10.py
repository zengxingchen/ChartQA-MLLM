
import matplotlib.pyplot as plt
import squarify
import seaborn as sns

# Your data
data = [
    {'Category': 'Fiction', 'Checkouts': 12000, 'Percentage': 25},
    {'Category': 'Non-Fiction', 'Checkouts': 9000, 'Percentage': 19},
    {'Category': "Children's Books", 'Checkouts': 15000, 'Percentage': 31},
    {'Category': 'Young Adult', 'Checkouts': 4000, 'Percentage': 8},
    {'Category': 'Mystery', 'Checkouts': 3000, 'Percentage': 6},
    {'Category': 'Biography', 'Checkouts': 2000, 'Percentage': 4},
    {'Category': 'Science Fiction', 'Checkouts': 2500, 'Percentage': 5},
    {'Category': 'Reference', 'Checkouts': 500, 'Percentage': 1},
    {'Category': 'Travel', 'Checkouts': 1000, 'Percentage': 2}
]

# Preparing the sizes and labels
sizes = [item['Checkouts'] for item in data]
labels = [f"{item['Category']} ({item['Percentage']}%)" for item in data]

# Colors
palette = sns.color_palette("Spectral", len(data))  # You can choose different palettes
colors = [palette[i] for i in range(len(data))]

# Create a figure to draw treemap
plt.figure(figsize=(12, 8))

# Creating the treemap
squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.8)

# Remove axis
plt.axis('off')

# Add title
plt.title('Library Checkouts by Category')

# Show the plot
plt.show()