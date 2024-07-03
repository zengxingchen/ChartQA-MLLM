
import matplotlib.pyplot as plt

# Define data
products = [
    "Smartphone", "Laptop", "Tablet", "Smartwatch", "Camera", "Headphones", 
    "Speaker", "Television", "Printer", "Monitor", "Keyboard", "Mouse", 
    "Router", "Smart Home Hub", "VR Headset", "Drone", "Fitness Tracker", 
    "E-Reader", "Smart Glasses", "Portable Charger", "Gaming Console", 
    "Projector", "Action Camera", "Digital Frame", "Electric Scooter", 
    "Wireless Charger"
]

price = [
    700, 1200, 500, 300, 800, 150, 100, 1000, 200, 300, 50, 30, 120, 250, 
    600, 900, 200, 150, 400, 50, 500, 600, 450, 100, 800, 70
]

popularity = [
    400, 350, 300, 250, 450, 200, 180, 380, 220, 270, 150, 130, 160, 210, 
    300, 330, 240, 200, 280, 170, 320, 290, 260, 190, 340, 160
]

rating = [
    85, 90, 78, 82, 88, 75, 80, 87, 76, 83, 72, 70, 74, 81, 86, 89, 77, 84, 
    88, 79, 92, 85, 82, 73, 91, 78
]

# Create a figure with specified width and height
fig, ax = plt.subplots(figsize=(18, 12))

# Bubble sizes as a fraction of popularity (adjust the scaling as needed)
sizes = [popularity[i] / 1.5 for i in range(len(popularity))]

# Scatter plot (using price as weight for bubble size)
scatter = ax.scatter(
    price, rating, s=sizes, alpha=0.6,
    color=[
        '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', 
        '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#9edae5', '#ffbb78', 
        '#98df8a', '#ff9896', '#c49c94', '#f7b6d2', '#c7c7c7', '#dbdb8d', 
        '#aec7e8', '#ff7f0e', '#c5b0d5', '#ff9896', '#9edae5', '#98df8a', 
        '#ffbb78', '#2ca02c'
    ]
)

# Customize the appearance
ax.set_title('Gadget Prices, Popularity, and Ratings', pad=20)
ax.set_xlabel('Price ($)')
ax.set_ylabel('Rating (%)')
ax.grid(True)

# Adding the names of the products to the bubbles
for i, txt in enumerate(products):
    ax.annotate(txt, (price[i], rating[i]))

plt.show()