
import matplotlib.pyplot as plt

# Data
categories = ['Novels', 'Poetry', 'Drama', 'Short Stories', 'Essays']
market_share = [40, 25, 20, 10, 5]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Create a pie chart
plt.figure(figsize=(12, 8))
plt.pie(market_share, labels=categories, autopct='%1.1f%%', startangle=140, colors=colors)

# Title
plt.title('Literature Categories Market Share in 2023', y=1.08)

# Display the chart
plt.show()