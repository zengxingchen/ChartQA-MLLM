
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
rainfall = [78, 80, 95, 105, 120, 130, 140, 135, 115, 100, 85, 75]

plt.figure(figsize=(16, 10))

# Plot the line chart with a new color scheme and trend
plt.plot(months, rainfall, color='#2ca02c', linewidth=3)

# Annotate the highest rainfall in July
plt.annotate('Highest Rainfall', xy=('July', 140), xytext=('August', 135),
             arrowprops=dict(facecolor='#d62728', shrink=0.05))

plt.title('Monthly Average Rainfall in 2023', fontsize=16, pad=20)  
plt.xlabel('Month', fontsize=14)  
plt.ylabel('Rainfall (mm)', fontsize=14)  

# Display the chart
plt.show()