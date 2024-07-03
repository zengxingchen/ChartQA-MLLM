
import matplotlib.pyplot as plt

# Data from the table above
countries = [
    'United States', 'Germany', 'United Kingdom', 'France', 'Italy', 
    'Spain', 'Greece', 'Brazil', 'India', 'China', 'Japan', 
    'South Korea', 'Australia', 'Canada', 'Russia', 'Turkey',
    'Mexico', 'Argentina', 'South Africa', 'Egypt'
]

average_temperature = [
    13.0, 8.5, 9.0, 11.5, 15.0, 18.5, 17.0, 25.0, 24.5, 10.0, 
    13.5, 11.0, 21.0, 5.0, 2.5, 14.0, 20.0, 16.5, 19.0, 22.5
]

# Modify the color scheme, width of bars, and size of the chart
colors = [
    '#4B8BBE', '#306998', '#FFE873', '#FFD43B', '#646464',
    '#3C9D9B', '#F05A28', '#264653', '#2A9D8F', '#E9C46A',
    '#F4A261', '#E76F51', '#A8DADC', '#457B9D', '#1D3557',
    '#D90429', '#EF233C', '#8D99AE', '#2B2D42', '#FB8500'
]

# Set the figure size for better clarity or visual appeal
plt.figure(figsize=(14, 8))

# Change the direction of the chart from horizontal to vertical
plt.barh(countries, average_temperature, color=colors, height=0.5)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Add labels and title to the chart
plt.xlabel('Average Temperature (°C)')
plt.title('Average Annual Temperature by Country')

# Display the chart
plt.tight_layout()  # Adjust layout to fit all labels and title
plt.show()