
import matplotlib.pyplot as plt

# Data to plot
labels = 'Stocks', 'Bonds', 'Real Estate', 'Commodities', 'Cryptocurrency'
sizes = [40.5, 25.3, 18.7, 10.1, 5.4]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Create pie chart
plt.figure(figsize=(10, 7))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)

plt.title('Investment Portfolio Distribution in 2023', pad=20)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()