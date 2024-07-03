
import matplotlib.pyplot as plt

# Data points
equipment = ['Basketball', 'Football', 'Tennis', 'Running', 'Cycling', 'Swimming', 'Others']
market_share = [18.5, 22.1, 14.3, 16.7, 12.9, 9.5, 6.0]

# Colors using hexadecimal color codes
colors = ['#FF6347', '#4682B4', '#FFD700', '#32CD32', '#8A2BE2', '#00CED1', '#FF69B4']

# Plotting the pie chart
plt.figure(figsize=(12, 7))  # Width and height of the chart
plt.pie(market_share, labels=equipment, colors=colors, autopct='%1.1f%%', startangle=140)

# Title of the chart
plt.title('Market Share of Different Types of Sports Equipment in 2023', pad=20)

# Display the chart
plt.show()