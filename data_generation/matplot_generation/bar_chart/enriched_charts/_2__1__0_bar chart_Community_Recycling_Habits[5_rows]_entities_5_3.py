
import matplotlib.pyplot as plt

# Data
countries = ['Japan', 'Switzerland', 'Singapore', 'Australia', 'Spain', 'Italy', 'Iceland', 'Israel', 'Sweden', 'France', 'Norway', 'Canada', 'New Zealand', 'Netherlands', 'United Kingdom', 'Ireland', 'Germany', 'Belgium', 'Austria', 'Finland']
life_expectancy = [84.3, 83.4, 83.1, 82.9, 82.8, 82.7, 82.7, 82.6, 82.4, 82.3, 82.2, 82.2, 82.0, 81.9, 81.6, 81.4, 81.2, 81.1, 81.0, 81.0]
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#A633FF', '#33FFF5', '#FF9933', '#99FF33', '#33FF99', '#5733FF', '#33A6FF', '#FFA533', '#5733A6', '#FF3357', '#33FFA6', '#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#A633FF']

# Figure size
plt.figure(figsize=(10, 8))

# Horizontal bar chart
plt.barh(countries, life_expectancy, color=colors, height=0.5)

# Labeling
plt.xlabel('Life Expectancy (years)')
plt.title('Top 20 Countries by Life Expectancy in 2024')

# Show and save plot
plt.tight_layout()
plt.show()