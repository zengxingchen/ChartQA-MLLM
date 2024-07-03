
import matplotlib.pyplot as plt

# Data points
genres = ['Action', 'Comedy', 'Drama', 'Horror', 'Romance', 'Sci-Fi', 'Others']
market_share = [15.4, 20.7, 25.3, 8.9, 12.1, 10.6, 7.0]

# Colors using hexadecimal color codes
colors = ['#ff6666', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c2f0c2']

# Plotting the pie chart
plt.figure(figsize=(10, 6))  # Width and height of the chart
plt.pie(market_share, labels=genres, colors=colors, autopct='%1.1f%%', startangle=140)

# Title of the chart
plt.title('Market Share of Different Movie Genres in 2023', pad=20)

# Display the chart
plt.show()