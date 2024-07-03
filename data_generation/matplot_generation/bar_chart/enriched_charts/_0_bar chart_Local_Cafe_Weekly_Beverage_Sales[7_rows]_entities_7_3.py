
import matplotlib.pyplot as plt

# Data points
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
revenue = [20000, 21000, 18500, 22300, 24000, 22500,
           21500, 23000, 22000, 23500, 22500, 24500]

# Colors for each bar
colors = ['#FF6347', '#FF4500', '#FFD700', '#ADFF2F', '#7FFF00',
          '#32CD32', '#00FA9A', '#40E0D0', '#1E90FF', '#0000FF',
          '#8A2BE2', '#FF1493']

# Creating horizontal bar chart
plt.figure(figsize=(14, 8)) # changing the width and height of the chart
plt.barh(months, revenue, color=colors, edgecolor='black', height=0.6) # changed direction, color, and band height

# Customizing the chart
plt.xlabel('Revenue in USD', fontsize=12)
plt.ylabel('Month', fontsize=12)
plt.title('Monthly Revenue for XYZ Corporation in 2021', fontsize=16)
plt.xlim(0, 25000) # Adjust the x-axis to accommodate the data range

# Display the chart
plt.tight_layout()
plt.show()