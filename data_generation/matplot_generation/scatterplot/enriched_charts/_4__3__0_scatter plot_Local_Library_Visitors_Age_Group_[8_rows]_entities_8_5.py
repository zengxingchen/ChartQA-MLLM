
import matplotlib.pyplot as plt

# Data
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", 
          "San Antonio", "San Diego", "Dallas", "San Jose", "Austin", "Jacksonville", 
          "Fort Worth", "Columbus", "Charlotte", "Seattle", "Denver", "El Paso", 
          "Detroit", "Boston", "Miami", "Atlanta", "Orlando", "Minneapolis", 
          "Tampa", "Cincinnati", "Sacramento", "Las Vegas", "Portland", "St. Louis", 
          "Baltimore", "Milwaukee", "Kansas City", "Cleveland"]
rainfall = [49.9, 14.8, 36.9, 49.8, 8.04, 41.5, 32.9, 10.3, 37.6, 15.8, 
            34.3, 50.3, 34.0, 39.2, 43.1, 37.5, 14.3, 8.8, 33.5, 49.9, 
            61.9, 50.2, 52.2, 30.6, 46.3, 42.6, 18.5, 4.2, 36.2, 41.0, 
            41.9, 34.8, 39.1, 39.1]
visitor_counts = [18, 16, 14, 20, 8, 12, 10, 7, 9, 5, 11, 6, 7, 8, 9, 15, 
                  12, 5, 6, 17, 14, 13, 10, 11, 8, 7, 9, 6, 10, 7, 8, 6, 7, 6]

# Create figure and axis objects
fig, ax = plt.subplots(figsize=(14, 10))

# Scatter plot
ax.scatter(rainfall, visitor_counts, color=["#FF5733", "#33FF57", "#3357FF", "#FF33A6", "#FF8C33", 
                                            "#9B33FF", "#33FFD1", "#FF3333", "#33FF8C", "#FF5733", 
                                            "#FFB733", "#337BFF", "#57FF33", "#8C33FF", "#5733FF", 
                                            "#B733FF", "#33A6FF", "#FF5733", "#33FF57", "#3357FF", 
                                            "#FF33A6", "#FF8C33", "#9B33FF", "#33FFD1", "#FF3333", 
                                            "#33FF8C", "#FF5733", "#FFB733", "#337BFF", "#57FF33", 
                                            "#8C33FF", "#5733FF", "#B733FF", "#33A6FF"])

# Title and labels
plt.title('Annual Rainfall vs. Visitor Count in Different Cities', pad=20)
plt.xlabel('Average Annual Rainfall (inches)')
plt.ylabel('Annual Visitor Count (millions)')

# Show plot
plt.show()