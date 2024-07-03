
import matplotlib.pyplot as plt

# Data
years = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
sales = [200, 250, 320, 400, 450, 520, 600, 680, 750, 800, 850, 920]

# Plot configuration
plt.figure(figsize=(14, 8))
bars = plt.barh(years, sales, height=0.5, color=[
    '#4CAF50', '#FF5722', '#2196F3', '#9C27B0',
    '#FFC107', '#795548', '#00BCD4', '#607D8B',
    '#FF9800', '#8BC34A', '#E91E63', '#673AB7'
])

# Axes labels and title
plt.xlabel('Annual Sales (in thousands)')
plt.ylabel('Year')
plt.title('Annual Sales of Eco-Friendly Products (2011-2022)')
plt.xlim(150, 1000)

# Show the plot
plt.show()