
import matplotlib.pyplot as plt

# Data
instrument = ["Smartphone", "Laptop", "Tablet", "Smartwatch", "Desktop", 
              "Headphones", "Camera", "Printer", "Monitor", "Keyboard", 
              "Mouse", "Speaker", "Drone", "SmartHomeDevice", "FitnessTracker", 
              "GameConsole", "TV", "VRHeadset", "EReader", "SmartGlasses", 
              "Projector", "3DPrinter"]
sales = [1000, 800, 600, 300, 400, 
         500, 350, 250, 450, 700, 
         750, 650, 150, 200, 500, 
         550, 400, 100, 300, 50, 
         100, 80]
price = [700, 1200, 500, 250, 1000, 
         200, 1500, 300, 400, 100, 
         50, 150, 800, 350, 100, 
         500, 800, 600, 120, 900, 
         400, 1000]

# Create figure and axis objects
fig, ax = plt.subplots(figsize=(16, 12))

# Scatter plot
ax.scatter(sales, price, color=["#1E90FF", "#32CD32", "#FF4500", "#DAA520", "#4B0082", 
                                "#FF69B4", "#00CED1", "#8B0000", "#20B2AA", "#FF6347", 
                                "#4682B4", "#D2691E", "#8A2BE2", "#5F9EA0", "#7FFF00", 
                                "#DC143C", "#FF7F50", "#8B0000", "#6495ED", "#F08080", 
                                "#4169E1", "#FF1493"])

# Title and labels
plt.title('Sales vs. Price of Various Tech Products', fontsize=20, pad=20)
plt.xlabel('Sales (in thousands)', fontsize=15)
plt.ylabel('Price (in dollars)', fontsize=15)

# Show plot
plt.show()