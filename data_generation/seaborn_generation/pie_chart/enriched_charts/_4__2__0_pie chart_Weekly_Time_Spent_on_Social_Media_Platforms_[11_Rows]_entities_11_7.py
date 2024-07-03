
import matplotlib.pyplot as plt

# Data
platforms = ['Netflix', 'Amazon Prime', 'Disney+', 'Hulu', 'HBO Max', 'Apple TV+', 'Paramount+', 'Peacock']
market_share = [35, 25, 15, 10, 8, 5, 2, 1]
colors = ['#FF6347', '#4682B4', '#FFD700', '#32CD32', '#8A2BE2', '#FF7F50', '#20B2AA', '#DC143C']

# Plotting the pie chart
fig, ax = plt.subplots(figsize=(12, 8))
ax.pie(market_share, labels=platforms, autopct='%1.1f%%', startangle=140, colors=colors)
ax.axis('equal')

# Setting the title
plt.title("Market Share of Streaming Platforms in 2023", pad=20)

# Display the chart
plt.show()