
import matplotlib.pyplot as plt

# Data
locations = ["Beach", "Museum", "Mountain", "Theme Park", "Zoo", 
             "Aquarium", "Historical Site", "National Park", "Botanical Garden", "Concert Hall", 
             "Cinema", "Art Gallery", "Festival", "Sports Event", "Market", 
             "Theatre", "Exhibition", "Food Fair", "Street Performance", "Library", 
             "Lecture", "Book Fair"]
visitors = [15000, 8000, 12000, 10000, 6000, 7000, 9000, 11000, 5000, 7500, 
            9500, 8500, 13000, 14000, 5500, 6000, 4000, 10000, 3000, 2000, 
            4500, 5000]
average_spend = [50, 20, 70, 80, 30, 25, 40, 60, 35, 55, 45, 50, 65, 75, 20, 55, 30, 40, 15, 5, 10, 25]

# Create figure and axis objects
fig, ax = plt.subplots(figsize=(14, 10))

# Scatter plot
ax.scatter(visitors, average_spend, color=["#FF5733", "#33FF57", "#3357FF", "#FF33A1", "#FF8C33", 
                                           "#33FFF5", "#8C33FF", "#FF335E", "#F5FF33", "#335FFF", 
                                           "#FF33D1", "#33FF8C", "#5733FF", "#FF3357", "#8FFF33", 
                                           "#33D1FF", "#FF5733", "#33FF57", "#3357FF", "#FF33A1", 
                                           "#FF8C33", "#33FFF5"])

# Title and labels
plt.title('Visitor Numbers vs. Average Spend at Various Locations')
plt.xlabel('Number of Visitors')
plt.ylabel('Average Spend ($)')

# Show plot
plt.show()