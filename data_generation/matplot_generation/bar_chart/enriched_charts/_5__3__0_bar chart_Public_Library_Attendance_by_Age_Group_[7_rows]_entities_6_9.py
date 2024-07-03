
import matplotlib.pyplot as plt

# Data
years = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']
carbon_emissions = [120, 145, 160, 190, 210, 230, 250, 280, 310, 330, 350, 370, 390, 410]

# Colors for each bar
colors = ['#4B0082', '#800080', '#FF4500', '#FFD700', '#ADFF2F', '#7FFF00', '#00FF7F', '#00CED1', '#1E90FF', '#0000FF', '#8A2BE2', '#FF69B4', '#BA55D3', '#9400D3']

# Create a horizontal bar chart
plt.figure(figsize=(10, 8))  # Change the figure size (width x height)
bar_height = 0.4  # Change the bar height
plt.barh(years, carbon_emissions, color=colors, height=bar_height)

# Setting the title and labels
plt.title('Annual Carbon Emissions of XYZ Corporation', pad=20)
plt.xlabel('Carbon Emissions (in tons)')
plt.ylabel('Year')

# Adjust the limits if necessary
plt.xlim([100, max(carbon_emissions) + 50])

# Display the chart
plt.tight_layout()
plt.show()