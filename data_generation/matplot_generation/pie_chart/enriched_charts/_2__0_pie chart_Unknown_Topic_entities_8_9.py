
import matplotlib.pyplot as plt

# Data points
sports = ['Football', 'Basketball', 'Running', 'Swimming', 'Cycling', 'Tennis', 'Others']
market_share = [28.3, 20.5, 15.4, 12.6, 10.2, 8.7, 4.3]
colors = ['#2a9d8f', '#e76f51', '#264653', '#f4a261', '#e9c46a', '#a1c181', '#457b9d']

# Create a pie chart
plt.figure(figsize=(12, 10))
plt.pie(market_share, labels=sports, colors=colors, autopct='%1.1f%%', startangle=90)

# Chart title
plt.title('Market Share of Different Sports Activities in 2023', pad=20)

# Display the chart
plt.show()