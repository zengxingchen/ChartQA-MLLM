
import matplotlib.pyplot as plt

# Data points
countries = ['China', 'United States', 'Germany', 'India', 'Japan', 'Brazil', 'United Kingdom', 'Canada', 
             'France', 'Italy', 'Australia', 'Russia', 'South Korea', 'Spain', 'Mexico', 'Indonesia', 
             'Netherlands', 'Turkey', 'Saudi Arabia', 'South Africa', 'Argentina', 'Sweden', 'Norway', 
             'Switzerland', 'Austria', 'Belgium', 'Denmark', 'Finland', 'Ireland', 'Poland', 'Greece', 
             'Portugal', 'Romania', 'Hungary', 'Czech Republic', 'Israel', 'New Zealand', 'Ukraine', 
             'Thailand', 'Vietnam']
renewable_energy = [2200, 1100, 600, 750, 300, 500, 200, 400, 250, 150, 100, 50, 90, 120, 80, 70, 60, 40, 
                    20, 30, 25, 35, 45, 15, 10, 5, 12, 8, 7, 22, 18, 14, 16, 6, 9, 4, 11, 13, 17, 21]

# Colors for each bar
colors = ['#FF6347', '#FF7F50', '#FFD700', '#ADFF2F', '#7FFF00', '#7CFC00', '#00FF00', '#32CD32', '#00FF7F', 
          '#00FA9A', '#40E0D0', '#48D1CC', '#00CED1', '#20B2AA', '#5F9EA0', '#4682B4', '#1E90FF', '#6495ED', 
          '#7B68EE', '#6A5ACD', '#8A2BE2', '#9400D3', '#9932CC', '#BA55D3', '#FF00FF', '#FF1493', '#C71585', 
          '#DB7093', '#FFA07A', '#FF4500', '#DC143C', '#B22222', '#8B0000', '#800000', '#A52A2A', '#A0522D', 
          '#D2691E', '#CD853F', '#F4A460', '#DEB887']

# Create a vertical bar chart
plt.figure(figsize=(16, 12))
plt.bar(countries, renewable_energy, color=colors, width=0.8)

# Modify the ticks, labels, and title
plt.ylabel('Renewable Energy Production (TWh)')
plt.title('Renewable Energy Production by Country')
plt.ylim(0, 2300)  # Setting the y-axis limit to start from 0 and go up to 2300 TWh

# Rotate x-axis labels for better readability
plt.xticks(rotation=90)

# Display the plot
plt.tight_layout()
plt.show()