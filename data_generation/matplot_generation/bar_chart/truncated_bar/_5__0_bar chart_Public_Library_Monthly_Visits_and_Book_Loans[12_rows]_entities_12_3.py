
import matplotlib.pyplot as plt

# Data for the chart
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 
          'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose', 
          'Austin', 'Jacksonville', 'Fort Worth', 'Columbus', 'Charlotte']
rainfall = [120, 30, 95, 145, 20, 105, 135, 25, 140, 35, 130, 160, 138, 110, 125]

# Setting colors for each bar
colors = ['#FF6347', '#4682B4', '#9ACD32', '#FF4500', '#2E8B57', 
          '#20B2AA', '#9370DB', '#FF69B4', '#FFA500', '#8A2BE2',
          '#DC143C', '#00CED1', '#FFD700', '#7CFC00', '#D2691E']

# Increase the width and height of the chart
plt.figure(figsize=(14, 10))

# Changing the direction of the chart to vertical
plt.bar(cities, rainfall, color=colors, width=0.5)

# Customizing the chart with titles and labels
plt.ylabel('Average Rainfall (mm)')
plt.title('Average Rainfall in Various U.S. Cities', pad=20)
plt.ylim(10, 170)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)

# Display the bar chart
plt.show()