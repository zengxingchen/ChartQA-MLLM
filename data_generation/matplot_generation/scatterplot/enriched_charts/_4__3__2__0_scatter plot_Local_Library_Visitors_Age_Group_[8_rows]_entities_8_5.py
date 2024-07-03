
import matplotlib.pyplot as plt

# Data
cities = ["Tokyo", "Delhi", "Shanghai", "São Paulo", "Mumbai", 
          "Beijing", "Cairo", "Dhaka", "Mexico City", "Osaka", 
          "Karachi", "Chongqing", "Istanbul", "Buenos Aires", "Kolkata", 
          "Lagos", "Kinshasa", "Manila", "Rio de Janeiro", "Guangzhou", 
          "Lahore", "Bangalore", "Moscow", "Shenzhen", "Jakarta", 
          "London", "Lima", "Bangkok", "Chengdu", "Tehran", 
          "Ho Chi Minh City", "Hong Kong", "Hanoi", "Singapore"]

population_density = [6500, 11000, 3900, 7400, 21000, 
                      1300, 19000, 44000, 6100, 12000, 
                      24000, 200, 2900, 5700, 24000, 
                      7000, 44000, 42000, 5500, 1600, 
                      6300, 11000, 4900, 6700, 14000, 
                      5700, 3200, 5300, 1200, 11500, 
                      37000, 6900, 6800, 8200]

average_life_expectancy = [84, 69, 80, 75, 70, 
                           81, 73, 71, 76, 82, 
                           67, 78, 77, 76, 70, 
                           53, 60, 71, 74, 80, 
                           68, 73, 76, 79, 71, 
                           81, 75, 77, 78, 75, 
                           76, 84, 76, 83]

# Create figure and axis objects
fig, ax = plt.subplots(figsize=(16, 12))

# Scatter plot
ax.scatter(population_density, average_life_expectancy, color=[
    "#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", 
    "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf", 
    "#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", 
    "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf", 
    "#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", 
    "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf", 
    "#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"])

# Title and labels
plt.title('Average Life Expectancy vs. Population Density in Different Cities', pad=20, fontsize=18)
plt.xlabel('Population Density (people per sq km)', fontsize=14)
plt.ylabel('Average Life Expectancy (years)', fontsize=14)

# Show plot
plt.show()