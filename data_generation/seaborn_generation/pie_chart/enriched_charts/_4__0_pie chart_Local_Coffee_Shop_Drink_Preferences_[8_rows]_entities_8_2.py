
import matplotlib.pyplot as plt

# Data to plot
labels = 'Stocks', 'Bonds', 'Real Estate', 'Commodities', 'Cryptocurrency', 'Mutual Funds', 'ETFs', 'Cash'
sizes = [450, 300, 150, 100, 50, 75, 65, 30]
colors = ['#ff6666','#66b2ff','#99ff99','#ffcc66','#ff99e6', '#c4e17f', '#c266d6', '#76d7c4']

# Change the size of the figure (width, height)
plt.figure(figsize=(12, 8))

# Plot
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

plt.title('Distribution of Investment Types in a Portfolio', y=1.05)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()