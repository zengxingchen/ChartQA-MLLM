
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
revenue = [1200, 1500, 1800, 2200, 2500, 3000, 3500, 3300, 2900, 2600, 2300, 2100]

# Figure Size
plt.figure(figsize=(14, 7))

# Plot area chart
plt.fill_between(months, revenue, color='#FF5733')

# Title and labels
plt.title('Monthly Revenue in 2023', fontsize=16, pad=20)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Revenue ($)', fontsize=12)

# Show grid
plt.grid(True)

# Annotation
for i, value in enumerate(revenue):
    plt.text(i, value + 100, str(value), ha='center')

# Show the plot
plt.show()