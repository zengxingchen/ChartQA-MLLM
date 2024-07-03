
import matplotlib.pyplot as plt

# Data for the bar chart
countries = [
    'Canada', 'Russia', 'Germany', 'United Kingdom', 'France', 'Spain', 
    'Italy', 'Greece', 'Turkey', 'Australia', 'Brazil', 'India', 
    'China', 'Japan', 'South Korea', 'Mexico', 'South Africa', 
    'Argentina', 'Nigeria', 'Egypt'
]

literacy_rates = [
    99.0, 99.7, 99.5, 99.0, 99.0, 98.4, 98.8, 97.9, 96.2, 99.0, 
    93.2, 74.0, 96.8, 99.0, 99.2, 95.4, 87.0, 98.1, 62.0, 75.2
]

# Modify the color scheme
colors = [
    '#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFA1', '#A133FF', 
    '#FF9133', '#91FF33', '#5733FF', '#33FF91', '#A1FF33', '#FF33FF', 
    '#33A1FF', '#FF3391', '#33FF33', '#FF3333', '#33FF57', '#5733FF', 
    '#33FFA1', '#A1FF33'
]

# Set the figure size for better clarity or visual appeal
plt.figure(figsize=(14, 8))

# Change the direction of the chart from vertical to horizontal
plt.barh(countries, literacy_rates, color=colors, height=0.4)

# Set y-axis limits to truncate the chart
plt.xlim(60, 100)

# Add labels and title to the chart
plt.xlabel('Literacy Rate (%)')
plt.title('Literacy Rates by Country', pad=20)

# Display the chart
plt.show()