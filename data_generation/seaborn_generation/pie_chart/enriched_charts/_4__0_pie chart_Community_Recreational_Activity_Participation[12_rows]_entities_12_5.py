
import matplotlib.pyplot as plt

# Data points
genres = ['Pop', 'Rock', 'Hip-Hop', 'Classical', 'Jazz', 'Country', 'Electronic']
market_share = [30.5, 25.4, 20.2, 10.1, 7.6, 4.7, 1.5]

# Colors using hexadecimal color codes
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c4e17f']

# Plotting the pie chart
plt.figure(figsize=(8, 8))  # Width and height of the chart
plt.pie(market_share, labels=genres, colors=colors, autopct='%1.1f%%', startangle=140)

# Title of the chart
plt.title('Music Genre Popularity in 2023')

# Display the chart
plt.show()