
import matplotlib.pyplot as plt
import squarify

# Data points
sector = [
    'Real Estate', 'Technology', 'Healthcare', 'Financial Services',
    'Energy', 'Consumer Goods', 'Utilities', 'Industrial Goods',
    'Telecommunications', 'Materials', 'Agriculture', 'Transportation'
]
market_share = [25, 20, 15, 10, 8, 7, 5, 4, 3, 2, 1, 1]
revenue = [1500, 1300, 1100, 900, 700, 600, 500, 400, 300, 200, 100, 100]

# Color scheme using specific color codes
colors = [
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
    '#c49c94', '#f7b6d2'
]

# Create a figure with altered width and height
fig, ax = plt.subplots(figsize=(20, 16))

# Creating a treemap
squarify.plot(sizes=market_share, label=sector, color=colors, alpha=0.8, value=revenue, edgecolor='white', linewidth=2)

# Chart title and subtitle
plt.title('Global Investment Sectors Market Share', fontsize=18, color='darkblue')
plt.suptitle('Market Share and Revenue Distribution in Various Investment Sectors', fontsize=22, y=1.05)

# Remove the axes
plt.axis('off')

# Show plot
plt.show()