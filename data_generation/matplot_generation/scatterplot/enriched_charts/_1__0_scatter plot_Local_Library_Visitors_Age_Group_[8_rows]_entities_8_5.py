
import matplotlib.pyplot as plt

# Data
fruit = ["Apple", "Banana", "Cherry", "Date", "Elderberry", 
         "Fig", "Grapefruit", "Honeydew", "Indian Fig", "Jackfruit", 
         "Kiwi", "Lemon", "Mango", "Nectarine", "Orange", 
         "Papaya", "Quince", "Raspberry", "Strawberry", "Tangerine", 
         "Ugli Fruit", "Watermelon"]
sweetness = [70, 90, 85, 80, 75, 65, 50, 60, 55, 95, 60, 25, 85, 75, 80, 70, 50, 45, 75, 85, 40, 80]
sourness = [30, 10, 15, 20, 25, 35, 50, 40, 45, 5, 40, 75, 15, 25, 20, 30, 50, 55, 25, 15, 60, 20]

# Create figure and axis objects
fig, ax = plt.subplots(figsize=(12, 9))

# Scatter plot
ax.scatter(sweetness, sourness, color=["#FF7F50", "#FFD700", "#DC143C", "#8B0000", "#4B0082", 
                                       "#8FBC8F", "#FF8C00", "#ADFF2F", "#FF4500", "#DA70D6", 
                                       "#008000", "#20B2AA", "#F08080", "#8A2BE2", "#4169E1", 
                                       "#CD5C5C", "#D2691E", "#9ACD32", "#7FFFD4", "#FF1493", 
                                       "#9932CC", "#00CED1"])

# Title and labels
plt.title('Average Sweetness vs. Average Sourness of Different Fruits')
plt.xlabel('Average Sweetness')
plt.ylabel('Average Sourness')

# Show plot
plt.show()