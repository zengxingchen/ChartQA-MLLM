
import matplotlib.pyplot as plt
import squarify

# Data points
regions = ['North', 'South', 'East', 'West', 'Central', 'Northeast', 'Southeast', 'Southwest', 'Northwest']
sales = [12000, 15000, 18000, 22000, 17000, 8000, 14000, 19000, 16000]
profit = [2000, 3000, 4000, 7000, 3500, 1000, 2500, 4500, 3000]

# Color scheme using specific color codes
colors = [
    '#63D1F4', '#FFD97D', '#FFDBE9', '#FF9AA2', '#C7CEEA',
    '#FFB7B2', '#B5EAD7', '#C3B1E1', '#A2D2FF'
]

# Create a figure with altered width and height
fig, ax = plt.subplots(figsize=(12, 8))

# Creating a treemap
squarify.plot(sizes=sales, label=regions, color=colors, alpha=0.8, value=profit, edgecolor='white', linewidth=2)

# Chart title and subtitle
plt.title('Regional Sales and Profit Distribution', fontsize=18, color='darkblue')
plt.suptitle('Company Performance by Region', fontsize=22)

# Remove the axes
plt.axis('off')

# Show plot
plt.show()