
import matplotlib.pyplot as plt

# Table data
destination = ['Europe', 'Asia', 'North America', 'South America', 'Africa', 'Australia']
market_share = [35.0, 25.0, 20.0, 10.0, 5.0, 5.0]
colors = ['#FF5733', '#33FF57', '#3357FF', '#F1C40F', '#8E44AD', '#1ABC9C']

# Plot
fig, ax = plt.subplots(figsize=(10, 6))  # Change width and height of the chart
ax.pie(market_share, labels=destination, autopct='%1.1f%%', startangle=140, colors=colors)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title('Preferred Travel Destinations in 2023', pad=20)
plt.show()