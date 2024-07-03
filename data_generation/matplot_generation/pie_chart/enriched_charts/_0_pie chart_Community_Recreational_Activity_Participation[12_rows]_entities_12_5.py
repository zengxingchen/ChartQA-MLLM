
import matplotlib.pyplot as plt

# Data points
brands = ['Samsung', 'Apple', 'Huawei', 'Xiaomi', 'OPPO', 'Vivo','Others']
market_share = [21.8, 15.6, 14.4, 8.3, 5.7, 5.6, 28.6]

# Colors using hexadecimal color codes
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']

# Plotting the pie chart
plt.figure(figsize=(10, 7))  # Width and height of the chart
plt.pie(market_share, labels=brands, colors=colors, autopct='%1.1f%%', startangle=140)

# Title of the chart
plt.title('Smartphone Market Share in 2023')

# Display the chart
plt.show()