
import matplotlib.pyplot as plt

# Data
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", 
          "San Antonio", "San Diego", "Dallas", "San Jose", "Austin", "Jacksonville", 
          "Fort Worth", "Columbus", "Charlotte", "Seattle", "Denver", "El Paso", 
          "Detroit", "Boston", "Miami", "Atlanta", "Orlando", "Minneapolis", 
          "Tampa", "Cincinnati", "Sacramento", "Las Vegas", "Portland", "St. Louis", 
          "Baltimore", "Milwaukee", "Kansas City", "Cleveland"]
library_visits = [20, 18, 16, 14, 12, 13, 10, 9, 8, 7, 11, 6, 7, 8, 9, 15, 12, 5, 6, 17, 
                  14, 13, 10, 11, 8, 7, 9, 6, 10, 7, 8, 6, 7, 6]
books_borrowed = [15, 12, 11, 9, 7, 8, 6, 7, 5, 4, 9, 3, 4, 6, 7, 12, 10, 3, 4, 14, 10, 
                  11, 8, 9, 6, 5, 7, 4, 8, 5, 6, 4, 5, 3]

# Create figure and axis objects
fig, ax = plt.subplots(figsize=(12, 9))

# Scatter plot
ax.scatter(library_visits, books_borrowed, color=["#FF5733", "#33FF57", "#3357FF", "#FF33A6", "#FF8C33", 
                                                  "#9B33FF", "#33FFD1", "#FF3333", "#33FF8C", "#FF5733", 
                                                  "#FFB733", "#337BFF", "#57FF33", "#8C33FF", "#5733FF", 
                                                  "#B733FF", "#33A6FF", "#FF5733", "#33FF57", "#3357FF", 
                                                  "#FF33A6", "#FF8C33", "#9B33FF", "#33FFD1", "#FF3333", 
                                                  "#33FF8C", "#FF5733", "#FFB733", "#337BFF", "#57FF33", 
                                                  "#8C33FF", "#5733FF", "#B733FF", "#33A6FF"])

# Title and labels
plt.title('Public Library Visits vs. Books Borrowed in Different Cities', pad=20)
plt.xlabel('Public Library Visits (millions)')
plt.ylabel('Books Borrowed (millions)')

# Show plot
plt.show()