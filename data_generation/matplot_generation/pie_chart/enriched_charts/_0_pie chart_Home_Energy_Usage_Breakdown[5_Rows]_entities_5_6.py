
import matplotlib.pyplot as plt

# Data
countries = ['United States', 'China', 'Japan', 'Germany', 'India', 
             'United Kingdom', 'France', 'Italy', 'Brazil', 'Canada', 
             'Russia', 'South Korea', 'Australia', 'Spain', 'Mexico']
gdp = [21.43, 14.34, 5.08, 3.86, 2.87,
       2.83, 2.72, 2.00, 1.84, 1.74,
       1.70, 1.64, 1.39, 1.39, 1.27]

# Colors
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
          '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
          '#1a55FF', '#8B0000', '#00FFFF', '#FF1493', '#FFA500']

# Pie chart
fig, ax = plt.subplots(figsize=(12, 9))  # Width, Height of the chart
ax.pie(gdp, labels=countries, colors=colors, autopct='%1.1f%%', startangle=140)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title('GDP by Country (Trillions)', pad=20)
plt.show()