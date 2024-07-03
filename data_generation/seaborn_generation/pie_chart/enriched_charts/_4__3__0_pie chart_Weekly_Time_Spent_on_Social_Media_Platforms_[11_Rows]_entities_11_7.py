
import matplotlib.pyplot as plt

# Data
platforms = ['Netflix', 'Amazon Prime Video', 'Disney+', 'Hulu', 'HBO Max', 'Apple TV+', 'Peacock', 'Paramount+']
market_share = [31, 22, 15, 10, 8, 7, 4, 3]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6','#c4e17f','#76d7c4']

# Plotting the pie chart
fig, ax = plt.subplots(figsize=(12, 9))
ax.pie(market_share, labels=platforms, autopct='%1.1f%%', startangle=140, colors=colors)
ax.axis('equal')

# Setting the title
plt.title("Market Share of Streaming Platforms", pad=20)

# Display the chart
plt.show()