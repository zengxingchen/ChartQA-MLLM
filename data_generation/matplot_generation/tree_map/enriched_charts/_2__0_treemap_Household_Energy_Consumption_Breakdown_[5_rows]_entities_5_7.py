
import matplotlib.pyplot as plt
import squarify

# Data points
locations = [
    'Alps', 'Rockies', 'Himalayas', 'Andes', 'Appalachians', 'Sierra Nevada', 
    'Carpathians', 'Urals', 'Pyrenees', 'Atlas Mountains', 'Caucasus', 
    'Alaska Range', 'Southern Alps', 'Drakensberg', 'Great Dividing Range'
]
visitors = [22000, 18000, 25000, 20000, 15000, 16000, 13000, 17000, 14000, 19000, 21000, 23000, 24000, 12000, 11000]
revenue = [5000, 4000, 7000, 4500, 3000, 3200, 2800, 3500, 2900, 3800, 4900, 5200, 5300, 2500, 2300]

# Color scheme using specific color codes
colors = [
    '#FF6347', '#FFD700', '#98FB98', '#00CED1', '#FF69B4', '#B0C4DE', 
    '#FFA07A', '#20B2AA', '#778899', '#7B68EE', '#6B8E23', '#4682B4', 
    '#D2691E', '#B22222', '#8B4513'
]

# Create a figure with altered width and height
fig, ax = plt.subplots(figsize=(14, 10))

# Creating a treemap
squarify.plot(sizes=visitors, label=locations, color=colors, alpha=0.8, value=revenue, edgecolor='white', linewidth=2)

# Chart title and subtitle
plt.title('Visitor and Revenue Distribution', fontsize=18, color='darkgreen')
plt.suptitle('Travel & Adventure Destinations', fontsize=22)

# Remove the axes
plt.axis('off')

# Show plot
plt.show()