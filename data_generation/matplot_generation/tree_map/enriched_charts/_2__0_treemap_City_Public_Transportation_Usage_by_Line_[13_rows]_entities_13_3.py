
import matplotlib.pyplot as plt
import squarify

# Data for the treemap
labels = [
    'Financial Services', 'Technology', 'Healthcare', 'Consumer Goods', 
    'Energy', 'Industrials', 'Telecommunications', 'Utilities', 
    'Real Estate', 'Materials', 'Consumer Services', 'Media', 'Transportation'
]
sizes = [15, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
colors = [
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',  
    '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',  
    '#bcbd22', '#17becf', '#aec7e8', '#ffbb78', '#98df8a'
]

# Create a figure of specified width and height
plt.figure(figsize=(18, 10))

# Create a treemap with specified data, labels, and color
squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.8)

# Set the title of the chart
plt.title('Sector Distribution in the Stock Market')

# Remove the axis
plt.axis('off')

# Display the treemap
plt.show()