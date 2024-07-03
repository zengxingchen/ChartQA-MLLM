
import matplotlib.pyplot as plt

# Data points
technology = ['Quantum Computing', 'Artificial Intelligence', 'Robotics', 'Blockchain', 'Internet of Things', 'Virtual Reality', 'Others']
market_share = [15.0, 25.0, 20.0, 10.0, 12.0, 8.0, 10.0]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c4e17f']

# Create a pie chart
plt.figure(figsize=(12, 9))  # Modify the width and height of the chart
plt.pie(market_share, labels=technology, colors=colors, autopct='%1.1f%%', startangle=140)

# Chart title
plt.title('Market Share of Future Technologies in 2023', pad=20)

# Display the chart
plt.show()