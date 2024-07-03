
import matplotlib.pyplot as plt

# Data for the bar chart
countries = [
    'Canada', 'Russia', 'Germany', 'United Kingdom', 'France', 'Spain', 
    'Italy', 'Greece', 'Turkey', 'Australia', 'Brazil', 'India', 
    'China', 'Japan', 'South Korea', 'Mexico', 'South Africa', 
    'Argentina', 'Nigeria', 'Egypt'
]

unemployment_rates = [
    5.6, 4.3, 3.8, 4.0, 8.1, 13.3, 9.2, 16.7, 12.5, 5.3, 11.6, 7.0, 
    4.8, 2.8, 3.7, 3.5, 30.8, 9.8, 27.1, 9.6
]

# Modify the color scheme
colors = [
    '#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFA1', '#A133FF', 
    '#FF9133', '#91FF33', '#5733FF', '#33FF91', '#A1FF33', '#FF33FF', 
    '#33A1FF', '#FF3391', '#33FF33', '#FF3333', '#33FF57', '#5733FF', 
    '#33FFA1', '#A1FF33'
]

# Set the figure size for better clarity or visual appeal
plt.figure(figsize=(16, 10))

# Change the direction of the chart from vertical to horizontal
plt.barh(countries, unemployment_rates, color=colors, height=0.6)

# Add labels and title to the chart
plt.xlabel('Unemployment Rate (%)')
plt.title('Unemployment Rates by Country', pad=20)

# Display the chart
plt.show()