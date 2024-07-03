
import matplotlib.pyplot as plt

# Data
countries = ['USA', 'China', 'India', 'Germany', 'Brazil', 'UK', 'Canada', 'Australia']
market_share = [25, 20, 18, 15, 10, 7, 3, 2]
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700', '#FF6347', '#8A2BE2', '#40E0D0']

# Plotting the pie chart
fig, ax = plt.subplots(figsize=(10, 6))  # Change width and height
ax.pie(market_share, labels=countries, autopct='%1.1f%%', startangle=140, colors=colors)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Setting the title
plt.title("Market Share of Various Countries in Tech Industry - 2023", pad=20)

# Display the chart
plt.show()