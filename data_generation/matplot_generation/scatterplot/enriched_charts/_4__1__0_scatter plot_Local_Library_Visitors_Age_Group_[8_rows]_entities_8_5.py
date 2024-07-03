
import matplotlib.pyplot as plt

# Data
vegetables = ["Broccoli", "Spinach", "Kale", "Carrot", "Beetroot", 
              "Cauliflower", "Zucchini", "Bell Pepper", "Asparagus", "Peas", 
              "Green Beans", "Tomato", "Cucumber", "Eggplant", "Lettuce", 
              "Mushroom", "Radish", "Turnip", "Sweet Potato", "Pumpkin", 
              "Celery", "Onion", "Garlic", "Artichoke", "Brussels Sprouts", 
              "Leek", "Okra"]
nutrient_density = [90, 95, 85, 70, 75, 80, 65, 80, 90, 70, 
                    75, 85, 60, 55, 85, 90, 50, 60, 70, 65, 
                    55, 65, 85, 80, 90, 70, 75]
caloric_content = [55, 23, 49, 41, 43, 25, 17, 31, 20, 81, 
                   31, 18, 16, 25, 14, 22, 16, 28, 86, 26, 
                   14, 40, 149, 47, 43, 61, 33]

# Create figure and axis objects
fig, ax = plt.subplots(figsize=(14, 10))

# Scatter plot
ax.scatter(nutrient_density, caloric_content, color=["#6A5ACD", "#FF4500", "#2E8B57", "#FF6347", "#8A2BE2", 
                                                     "#FFD700", "#48D1CC", "#FF1493", "#7FFF00", "#1E90FF", 
                                                     "#ADFF2F", "#DC143C", "#00CED1", "#8B0000", "#20B2AA", 
                                                     "#FF69B4", "#32CD32", "#7B68EE", "#FF7F50", "#00FA9A", 
                                                     "#FFDAB9", "#8B4513", "#CD5C5C", "#9ACD32", "#D2691E", 
                                                     "#FF8C00", "#ADFF2F"])

# Title and labels
plt.title('Nutrient Density vs. Caloric Content of Different Vegetables', fontsize=16, pad=20)
plt.xlabel('Nutrient Density', fontsize=14)
plt.ylabel('Caloric Content', fontsize=14)

# Show plot
plt.show()