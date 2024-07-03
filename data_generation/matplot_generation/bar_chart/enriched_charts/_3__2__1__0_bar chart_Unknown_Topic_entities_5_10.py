
import matplotlib.pyplot as plt

# Data
countries = ['Japan', 'Switzerland', 'Spain', 'Singapore', 'France', 'Australia', 'Canada', 'Italy', 'South Korea', 'Norway', 'Sweden', 'New Zealand', 'Germany', 'United Kingdom', 'United States', 'China', 'Brazil', 'India', 'South Africa', 'Nigeria']
life_expectancy = [84.2, 83.8, 83.5, 83.4, 82.7, 82.5, 82.3, 82.2, 82.1, 82.0, 82.0, 81.8, 81.2, 81.1, 78.5, 76.9, 75.5, 69.7, 63.9, 54.3]

# Create vertical bar chart
fig, ax = plt.subplots(figsize=(14, 10))

bars = ax.bar(countries, life_expectancy, width=0.5, color=['#4B0082', '#FF4500', '#32CD32', '#1E90FF', '#FFD700', '#8A2BE2', '#FF69B4', '#A52A2A', '#5F9EA0', '#D2691E', '#DC143C', '#008B8B', '#B8860B', '#00CED1', '#FF6347', '#4682B4', '#DAA520', '#6A5ACD', '#7FFF00', '#8B0000'])

# Customizing the plot
ax.set_title('Life Expectancy by Country (in years)', fontsize=20, pad=20)
ax.set_ylabel('Life Expectancy (years)', fontsize=16)
ax.set_xlabel('Country', fontsize=16)
ax.set_xticklabels(countries, rotation=45, ha='right')

# Set bar labels to show the life expectancy values
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, height, f'{height}', ha='center', va='bottom')

# Show the plot
plt.tight_layout()
plt.show()