
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
production = [50, 52, 55, 60, 70, 80, 85, 83, 75, 65, 55, 50]

# Plotting the line chart
plt.figure(figsize=(14, 7))  # Change width and height of the chart
plt.plot(months, production, marker='s', linestyle='-', color='#ffa500', linewidth=2.5)  # Modify color scheme

# Adding title and labels
plt.title('Monthly Production of Factory ABC', fontsize=18)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Production (in tons)', fontsize=12)

# Adding an annotation for the highest production
highest_prod_index = production.index(max(production))
highest_prod_month = months[highest_prod_index]
plt.annotate('Peak Production', xy=(highest_prod_index, max(production)), xytext=(highest_prod_index, max(production) + 5),
             arrowprops=dict(facecolor='#ff4500', shrink=0.05))

# Add a grid, set axis ranges and show the plot
plt.grid(True)
plt.ylim(45, 90)
plt.show()