
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
temperatures = [5, 7, 10, 12, 15, 20, 22, 21, 18, 14, 10, 6]

plt.figure(figsize=(14, 8))

# Plot the line chart with a new color scheme and trend
plt.plot(months, temperatures, color='#1f77b4', linewidth=2)

# Annotate the highest temperature in July
plt.annotate('Highest Temp', xy=('July', 22), xytext=('August', 21),
             arrowprops=dict(facecolor='#ff7f0e', shrink=0.05))

plt.title('Monthly Average Temperatures in 2023', fontsize=14)  
plt.xlabel('Month', fontsize=12)  
plt.ylabel('Temperature (°C)', fontsize=12)  

# Display the chart
plt.show()