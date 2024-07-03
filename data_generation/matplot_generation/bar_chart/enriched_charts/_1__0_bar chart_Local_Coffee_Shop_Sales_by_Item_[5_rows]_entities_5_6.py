
import matplotlib.pyplot as plt

# Data for plotting
years = [
    2011, 2012, 2013, 2014, 2015, 2016,
    2017, 2018, 2019, 2020, 2021, 2022, 2023
]
revenue_in_millions = [
    25, 30, 35, 40, 45, 50,
    60, 70, 85, 100, 120, 135, 150
]

# Changing figure size
plt.figure(figsize=(10, 12))

# Plotting - vertical bar chart
bar_width = 0.5
plt.bar(years, revenue_in_millions, color=[
    '#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0',
    '#ffb3e6', '#c4e17f', '#76d7c4', '#f7c6c7', '#f7b267',
    '#ffb6c1', '#ffd700', '#32cd32'
], width=bar_width)

# Customize chart
plt.ylabel('Revenue in Millions', fontsize=14)
plt.xlabel('Year', fontsize=14)
plt.title('Annual Revenue Over the Years', fontsize=16)

# Resize bar width
plt.xticks(years, [str(year) for year in years], fontsize=10, rotation=45)

# Show plot
plt.show()