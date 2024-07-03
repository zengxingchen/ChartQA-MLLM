
import matplotlib.pyplot as plt

# Data
countries = ['United States', 'China', 'India', 'Russia', 'Brazil', 'Australia', 'Canada', 'Germany', 'France', 'Japan', 
             'United Kingdom', 'Italy', 'Spain', 'Mexico', 'South Africa', 'Argentina', 'Indonesia', 'Saudi Arabia', 
             'South Korea', 'Turkey']
average_temperature = [12.0, 8.5, 24.0, -5.0, 22.0, 21.5, -4.0, 10.0, 11.0, 15.0, 9.5, 14.5, 16.0, 20.0, 17.5, 14.0, 
                       26.0, 27.5, 13.0, 12.5]
colors = ['#FF6347', '#FFD700', '#ADFF2F', '#00FF7F', '#00FA9A', '#7B68EE', '#6A5ACD', '#483D8B', '#2F4F4F', '#FF4500',
          '#FFA500', '#FF8C00', '#DA70D6', '#9932CC', '#8A2BE2', '#7FFF00', '#32CD32', '#8B0000', '#FF0000', '#B22222']

# Figure size
plt.figure(figsize=(12, 6))

# Vertical bar chart
plt.bar(countries, average_temperature, color=colors, width=0.6)

# Labeling
plt.ylabel('Average Temperature (°C)')
plt.title('Average Annual Temperature by Country in 2024')
plt.xticks(rotation=45, ha='right')

# Y-axis limits
plt.ylim(-10, 30)

# Show and save plot
plt.tight_layout()
plt.show()