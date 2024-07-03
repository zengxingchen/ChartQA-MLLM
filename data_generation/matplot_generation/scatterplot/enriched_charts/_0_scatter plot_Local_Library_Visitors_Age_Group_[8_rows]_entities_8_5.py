
import matplotlib.pyplot as plt

# Data
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", 
          "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose", 
          "Austin", "Jacksonville", "Fort Worth", "Columbus", "Charlotte", 
          "Seattle", "Denver", "El Paso", "Detroit", "Boston"]
income = [80, 75, 70, 65, 55, 60, 50, 78, 67, 90, 70, 54, 58, 55, 62, 80, 75, 42, 48, 85]
house_prices = [650, 570, 350, 250, 220, 240, 210, 500, 300, 800, 450, 190, 220, 200, 260, 550, 400, 160, 180, 600]

# Create figure and axis objects
fig, ax = plt.subplots(figsize=(10, 8))

# Scatter plot
ax.scatter(income, house_prices, color=["#FF6347", "#4682B4", "#32CD32", "#FFD700", "#40E0D0", 
                                        "#800080", "#FF4500", "#DA70D6", "#000080", "#008000", 
                                        "#BC8F8F", "#4169E1", "#8B4513", "#FA8072", "#2E8B57", 
                                        "#A52A2A", "#D2691E", "#CD5C5C", "#0000CD", "#ADFF2F"])

# Title and labels
plt.title('Average House Price vs. Average Annual Household Income in Different Cities')
plt.xlabel('Average Annual Household Income ($1000s)')
plt.ylabel('Average House Price ($1000s)')

# Show plot
plt.show()