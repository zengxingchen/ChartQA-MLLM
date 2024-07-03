
import matplotlib.pyplot as plt

# Data from the table above
countries = [
    'Canada', 'Russia', 'Germany', 'United Kingdom', 'France', 'Spain', 
    'Italy', 'Greece', 'Turkey', 'Australia', 'Brazil', 'India', 
    'China', 'Japan', 'South Korea'
]

average_temperatures = [
    -5.35, -5.1, 8.5, 8.45, 10.7, 13.3, 13.75, 15.4, 11.1, 
    21.65, 25.15, 23.65, 6.95, 11.15, 11.2
]

# Modify the color scheme, width of bars, and size of the chart
colors = [
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
    '#1fa774', '#e7969c', '#f9be2d', '#aec7e8', '#ffbb78'
]

# Set the figure size for better clarity or visual appeal
plt.figure(figsize=(14, 8))

# Change the direction of the chart from vertical to horizontal
plt.barh(countries, average_temperatures, color=colors, height=0.5)

# Add labels and title to the chart
plt.xlabel('Average Temperature (°C)')
plt.title('Average Annual Temperatures by Country')

# Display the chart
plt.show()