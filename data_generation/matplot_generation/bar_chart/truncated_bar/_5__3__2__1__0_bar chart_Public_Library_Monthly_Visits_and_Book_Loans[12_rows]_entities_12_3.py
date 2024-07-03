
import matplotlib.pyplot as plt

# Data for the chart
countries = ['USA', 'Germany', 'Canada', 'France', 'Australia', 'UK', 'Japan', 'South Korea', 
             'China', 'India', 'Brazil', 'Russia', 'South Africa', 'Mexico', 'Italy', 'Spain', 
             'Sweden', 'Norway', 'Switzerland', 'Netherlands', 'Denmark', 'Finland', 'Austria', 
             'Belgium', 'Ireland', 'New Zealand', 'Portugal', 'Greece', 'Israel', 'Singapore', 'UAE']
health_expenditure = [11000, 6000, 7000, 7500, 6800, 6400, 7200, 5600, 
                      4500, 3500, 5300, 5000, 4800, 4600, 6300, 6100, 
                      5800, 9000, 10500, 6700, 7100, 6000, 6500, 6200, 
                      7000, 6600, 5200, 5000, 6200, 6500, 5800]

# Setting colors for each bar
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFA1', 
          '#A133FF', '#FF8A33', '#8AFF33', '#33FF8A', '#A1FF33', 
          '#338AFF', '#FF5733', '#33FF57', '#3357FF', '#FF33A1',
          '#33FFA1', '#A133FF', '#FF8A33', '#8AFF33', '#33FF8A',
          '#A1FF33', '#338AFF', '#FF5733', '#33FF57', '#3357FF',
          '#FF33A1', '#33FFA1', '#A133FF', '#FF8A33', '#8AFF33', 
          '#33FF8A']

# Increase the width and height of the chart
plt.figure(figsize=(18, 12))

# Change the direction of the chart to horizontal and modify the bar width
plt.barh(countries, health_expenditure, color=colors, height=0.7)

# Customizing the chart with titles and labels
plt.xlabel('Health Expenditure (USD per person per year)')
plt.title('Annual Health Expenditure in Various Countries', pad=20)
plt.xlim(3000, 11500)
plt.grid(axis='x', color='gray', linestyle='--', linewidth=0.5)

# Display the bar chart
plt.tight_layout()
plt.show()