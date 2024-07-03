
import matplotlib.pyplot as plt

# Data
years = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']
revenue = [150, 175, 200, 220, 260, 280, 300, 330, 360, 390, 410, 450, 480, 500]

# Colors for each bar
colors = ['#1F77B4', '#AEC7E8', '#FF7F0E', '#FFBB78', '#2CA02C', '#98DF8A', '#D62728', '#FF9896', '#9467BD', '#C5B0D5', '#8C564B', '#C49C94', '#E377C2', '#F7B6D2']

# Create a vertical bar chart
plt.figure(figsize=(12, 6))  # Change the figure size (width x height)
bar_width = 0.5  # Change the bar width
plt.bar(years, revenue, color=colors, width=bar_width)

# Setting the title and labels
plt.title('Annual Revenue Growth of XYZ Corporation')
plt.ylabel('Revenue (in millions)')
plt.xlabel('Year')

# Adjust the limits if necessary
plt.ylim([0, max(revenue) + 50])

# Display the chart
plt.tight_layout()
plt.show()