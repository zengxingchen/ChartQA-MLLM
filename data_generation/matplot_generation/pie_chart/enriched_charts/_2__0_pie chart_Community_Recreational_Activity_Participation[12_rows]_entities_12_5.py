
import matplotlib.pyplot as plt

# Data points
streaming_services = ['Spotify', 'Apple Music', 'Amazon Music', 'YouTube Music', 'Pandora', 'Deezer', 'Tidal', 'Others']
market_share = [31.0, 18.0, 15.0, 13.0, 7.0, 4.0, 3.0, 9.0]

# Colors using hexadecimal color codes
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#bcbd22']

# Plotting the pie chart
plt.figure(figsize=(12, 9))  # Width and height of the chart
plt.pie(market_share, labels=streaming_services, colors=colors, autopct='%1.1f%%', startangle=140)

# Title of the chart
plt.title('Streaming Service Market Share in 2023', pad=20)

# Display the chart
plt.show()