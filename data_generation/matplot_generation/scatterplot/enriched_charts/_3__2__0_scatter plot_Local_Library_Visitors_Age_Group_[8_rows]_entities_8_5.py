
import matplotlib.pyplot as plt

# Data
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", 
          "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose", 
          "Austin", "Jacksonville", "Fort Worth", "Columbus", "Charlotte", 
          "Seattle", "Denver", "El Paso", "Detroit", "Boston", 
          "San Francisco", "Miami", "Orlando", "Atlanta", "Portland", 
          "Las Vegas", "Nashville", "Baltimore", "Washington", "Cincinnati", 
          "Indianapolis", "Louisville", "Milwaukee"]
annual_expenditure = [85, 80, 75, 60, 55, 50, 45, 70, 65, 95, 
                      68, 48, 53, 47, 50, 77, 72, 40, 45, 88, 
                      100, 78, 55, 66, 73, 62, 57, 52, 82, 49, 
                      54, 58, 51]
average_savings = [25, 22, 20, 18, 15, 12, 10, 23, 17, 30, 
                   19, 11, 14, 10, 13, 24, 21, 8, 9, 28, 
                   35, 24, 15, 18, 20, 19, 16, 14, 26, 11, 
                   13, 16, 12]

# Create figure and axis objects
fig, ax = plt.subplots(figsize=(14, 10))

# Scatter plot
ax.scatter(annual_expenditure, average_savings, color=[
    "#FF5733", "#33FF57", "#3357FF", "#FF33A8", "#A833FF", 
    "#33FFF5", "#FF8C33", "#57FF33", "#FF3333", "#33FFA8", 
    "#FF5733", "#33FF57", "#3357FF", "#FF33A8", "#A833FF", 
    "#33FFF5", "#FF8C33", "#57FF33", "#FF3333", "#33FFA8",
    "#33FFBD", "#FF5733", "#3357FF", "#FF8C33", "#A833FF", 
    "#33FFF5", "#FF8C33", "#57FF33", "#FF3333", "#33FFA8",
    "#33FFBD", "#FF5733", "#3357FF"
])

# Title and labels
plt.title('Average Savings vs. Annual Expenditure in Different Cities', pad=20, fontsize=16)
plt.xlabel('Annual Expenditure ($1000s)', fontsize=14)
plt.ylabel('Average Savings ($1000s)', fontsize=14)

# Show plot
plt.show()