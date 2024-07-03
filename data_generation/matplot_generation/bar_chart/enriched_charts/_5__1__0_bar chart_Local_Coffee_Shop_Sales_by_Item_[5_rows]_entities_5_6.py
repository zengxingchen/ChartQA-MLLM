
import matplotlib.pyplot as plt

# Data for plotting
years = [
    2011, 2012, 2013, 2014, 2015, 2016,
    2017, 2018, 2019, 2020, 2021, 2022, 2023
]
average_hours_of_sleep = [
    6.8, 6.9, 7.0, 7.1, 7.0, 7.2,
    7.4, 7.3, 7.6, 7.8, 7.5, 7.9, 8.0
]

# Changing figure size
plt.figure(figsize=(12, 8))

# Plotting - horizontal bar chart
bar_height = 0.6
plt.barh(years, average_hours_of_sleep, color=[
    '#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#FFC300',
    '#DAF7A6', '#C70039', '#900C3F', '#581845', '#FF5733',
    '#C70039', '#900C3F', '#581845'
], height=bar_height)

# Customize chart
plt.xlabel('Average Hours of Sleep', fontsize=14)
plt.ylabel('Year', fontsize=14)
plt.title('Average Hours of Sleep Per Night Over the Years', fontsize=16, pad=20)

# Set y-axis limits to start from 6.5 instead of 0
plt.xlim(6.5, 8.5)

# Show plot
plt.show()