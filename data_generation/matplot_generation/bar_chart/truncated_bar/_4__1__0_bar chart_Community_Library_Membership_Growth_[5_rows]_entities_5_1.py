
import matplotlib.pyplot as plt

# Data for the bar chart
countries = [
    'Canada', 'Russia', 'Germany', 'United Kingdom', 'France', 'Spain', 
    'Italy', 'Greece', 'Turkey', 'Australia', 'Brazil', 'India', 
    'China', 'Japan', 'South Korea', 'Mexico', 'South Africa', 
    'Argentina', 'Nigeria', 'Egypt'
]

life_expectancy = [
    82.3, 72.6, 81.1, 81.2, 82.9, 83.4, 83.2, 81.4, 78.6, 82.8, 75.7, 
    69.4, 76.1, 84.5, 83.3, 75.2, 64.1, 76.8, 54.3, 71.1
]

# Modify the color scheme
colors = [
    '#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFA1', '#A133FF', 
    '#FF9133', '#91FF33', '#5733FF', '#33FF91', '#A1FF33', '#FF33FF', 
    '#33A1FF', '#FF3391', '#33FF33', '#FF3333', '#33FF57', '#5733FF', 
    '#33FFA1', '#A1FF33'
]

# Set the figure size for better clarity or visual appeal
plt.figure(figsize=(12, 18))

# Change the direction of the chart from horizontal to vertical
plt.bar(countries, life_expectancy, color=colors, width=0.7)

# Set y-axis limits
plt.ylim(50, 90)

# Add labels and title to the chart
plt.ylabel('Life Expectancy (Years)')
plt.title('Average Life Expectancy by Country', pad=20)

# Display the chart
plt.show()