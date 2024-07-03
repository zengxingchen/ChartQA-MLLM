
import matplotlib.pyplot as plt

# Data
years = [
    2010, 2011, 2012, 2013, 2014, 
    2015, 2016, 2017, 2018, 2019, 
    2020, 2021, 2022, 2023, 2024
]
revenue = [
    30, 35, 45, 50, 60, 
    70, 80, 90, 100, 110, 
    120, 130, 140, 150, 160
]

# Plot configuration
plt.figure(figsize=(10, 12))
bars = plt.bar(years, revenue, width=0.5, color=[
    '#4B0082', '#7B68EE', '#4682B4', '#5F9EA0',
    '#66CDAA', '#8FBC8F', '#20B2AA', '#2E8B57',
    '#3CB371', '#6B8E23', '#ADFF2F', '#FFD700',
    '#FF8C00', '#FF4500', '#DC143C'
])

# Axes labels and title
plt.ylabel('Revenue (in million USD)')
plt.xlabel('Year')
plt.title('Annual Revenue Growth (2010-2024)', pad=20)

# Set y-axis limits
plt.ylim(20, 170)

# Show the plot
plt.show()