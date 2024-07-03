
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
red_dresses = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]
blue_dresses = [60, 55, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165]

# Plot setup
fig, ax = plt.subplots(figsize=(10, 12))

# Stacked bar chart (vertical)
plt.bar(months, red_dresses, color='#FF5733', edgecolor='white', width=0.5, label='Red Dresses')
plt.bar(months, blue_dresses, bottom=red_dresses, color='#3498DB', edgecolor='white', width=0.5, label='Blue Dresses')

# Labels, title and legend
plt.ylabel('Number of Dresses Sold')
plt.title('Monthly Sales of Red and Blue Dresses')
plt.legend(loc='upper left')

# Show the plot
plt.show()