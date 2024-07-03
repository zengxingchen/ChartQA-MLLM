
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
values = [420, 380, 340, 310, 270, 230, 190, 210, 230, 250, 280, 310]

# Plotting the line chart
plt.figure(figsize=(16, 8))  # Change width and height of the chart
plt.plot(months, values, marker='o', linestyle='-', color='#1f77b4', linewidth=2.5)  # Modify color scheme

# Adding title and labels
plt.title('Monthly Average Air Quality Index (AQI)', fontsize=18)
plt.xlabel('Month', fontsize=14)
plt.ylabel('AQI', fontsize=14)

# Adding an annotation for the lowest AQI
lowest_aqi_index = values.index(min(values))
lowest_aqi_month = months[lowest_aqi_index]
plt.annotate('Lowest AQI', xy=(lowest_aqi_index, min(values)), xytext=(lowest_aqi_index, min(values) - 40),
             arrowprops=dict(facecolor='#ff7f0e', shrink=0.05))

# Add a grid, set axis ranges and show the plot
plt.grid(True)
plt.ylim(150, 450)
plt.gca().invert_yaxis()
plt.show()