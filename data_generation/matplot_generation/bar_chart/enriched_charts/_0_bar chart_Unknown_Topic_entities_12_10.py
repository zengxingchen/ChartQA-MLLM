
import matplotlib.pyplot as plt

# Table data represented as lists
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix',
          'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose',
          'Austin', 'Jacksonville']
temperatures = [8, 17, 10, 19, 23, 9, 20, 15, 18, 14, 19, 18]

# Custom color codes for each bar
colors = ['#FF5733', '#33FF57', '#3357FF', '#57FF33', '#FF33A6',
          '#33FFF6', '#F633FF', '#F6FF33', '#33A6FF', '#A6FF33', 
          '#FF8C33', '#A6FF33']

# Setting the size of the plot
plt.figure(figsize=(10, 8))

# Creating a horizontal bar chart
plt.barh(cities, temperatures, color=colors, height=0.5)

# Customizing the plot
plt.xlabel('Average Temperature (°C)')
plt.title('Average Temperatures of Cities')
plt.xlim(0, max(temperatures) + 5)  # Adjusting x-axis limits for better clarity
plt.grid(axis='x', linestyle='--', alpha=0.7)  # Adding a grid for the x-axis

# Display the plot
plt.show()