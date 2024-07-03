
import matplotlib.pyplot as plt

# Data for plotting
years = [
    2011, 2012, 2013, 2014, 2015, 2016,
    2017, 2018, 2019, 2020, 2021, 2022, 2023
]
attendance_in_thousands = [
    25, 28, 35, 42, 50, 55,
    62, 78, 90, 110, 120, 130, 145
]

# Changing figure size
plt.figure(figsize=(12, 8))

# Plotting - horizontal bar chart
bar_height = 0.6
plt.barh(years, attendance_in_thousands, color=[
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
    '#aec7e8', '#ffbb78', '#98df8a'
], height=bar_height)

# Customize chart
plt.xlabel('Attendance in Thousands', fontsize=14)
plt.ylabel('Year', fontsize=14)
plt.title('Annual Music Festival Attendance', fontsize=16)

# Resize bar height
plt.yticks(years, [str(year) for year in years], fontsize=10)

# Set y-axis limits to start from a specific value
plt.xlim(20, 160)

# Show plot
plt.show()