
import matplotlib.pyplot as plt

# Data
categories = ['Android', 'iOS', 'Samsung', 'KaiOS', 'Others']
market_share = [71.93, 27.47, 0.40, 0.15, 0.05]
colors = ['#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9', '#92A8D1']

# Create a pie chart
plt.figure(figsize=(10, 6))
plt.pie(market_share, labels=categories, autopct='%1.1f%%', startangle=140, colors=colors)

# Title
plt.title('Smartphone OS Market Share in 2023')

# Display the chart
plt.show()