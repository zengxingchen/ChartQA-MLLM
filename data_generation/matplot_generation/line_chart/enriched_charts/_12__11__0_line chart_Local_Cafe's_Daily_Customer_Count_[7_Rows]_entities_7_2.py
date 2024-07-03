
import matplotlib.pyplot as plt
import pandas as pd

# Data points
dates = pd.date_range(start="2024-01-01", end="2024-01-31")
steps_walked = [5000, 5200, 4800, 5300, 5500, 5100, 5700, 5900, 5600, 6000, 6200, 6300, 6500, 6700, 7000, 7100, 7200, 6900, 7400, 7600, 7800, 7900, 8000, 8200, 8400, 8500, 8700, 8900, 9000, 9100, 9300]

# Create the plot
plt.figure(figsize=(14, 7))
plt.plot(dates, steps_walked, marker='o', linestyle='-', color='#1E90FF')

# Annotate the highest and lowest steps walked points
plt.annotate('Highest\n9300 steps', xy=(dates[-1], 9300), xytext=(dates[-5], 9000),
             arrowprops=dict(facecolor='#FF4500', shrink=0.05), color='#FF4500')
plt.annotate('Lowest\n4800 steps', xy=(dates[2], 4800), xytext=(dates[5], 5200),
             arrowprops=dict(facecolor='#FF4500', shrink=0.05), color='#FF4500')

# Title and labels
plt.title('Daily Steps Walked in January 2024', pad=20)
plt.xlabel('Date')
plt.ylabel('Steps Walked')

# Customize the grid
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Show the plot
plt.show()