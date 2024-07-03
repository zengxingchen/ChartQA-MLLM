
import matplotlib.pyplot as plt

# Data for the chart
countries = ['Japan', 'Switzerland', 'Australia', 'Spain', 'Italy', 'Iceland', 
             'Israel', 'Sweden', 'France', 'Canada', 'Norway', 'Netherlands', 
             'United Kingdom', 'New Zealand', 'Ireland', 'Germany']
life_expectancy = [84, 83, 83, 83, 83, 82, 82, 82, 82, 82, 82, 81, 81, 81, 81, 81]

# Setting colors for each bar
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#A833FF', 
          '#FF9633', '#33FFF1', '#9633FF', '#FFC133', '#33FF75',
          '#FF33C4', '#33C4FF', '#33FF6F', '#FF3339', '#FF8F33', '#9FFF33']

# Increase the width and height of the chart
plt.figure(figsize=(12, 8))

# Change the direction of the chart to horizontal and modify the bar width
plt.barh(countries, life_expectancy, color=colors, height=0.6)

# Customizing the chart with titles and labels
plt.xlabel('Average Life Expectancy (years)')
plt.title('Average Life Expectancy in Various Countries')
plt.grid(color='gray', linestyle='--', linewidth=0.5)

# Set y-axis limits
plt.xlim(78, 85)

# Display the bar chart
plt.show()