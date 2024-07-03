
import matplotlib.pyplot as plt

# Data points
manufacturers = ['Samsung', 'Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Others']
market_share = [31.4, 22.1, 10.2, 9.5, 5.6, 4.6, 16.6]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']

# Create a pie chart
plt.figure(figsize=(10, 8))  # Modify the width and height of the chart
plt.pie(market_share, labels=manufacturers, colors=colors, autopct='%1.1f%%', startangle=140)

# Chart title
plt.title('Smartphone Market Share in 2023')

# Display the chart
plt.show()