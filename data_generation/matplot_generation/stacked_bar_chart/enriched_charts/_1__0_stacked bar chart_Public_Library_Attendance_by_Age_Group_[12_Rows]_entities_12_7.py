
import matplotlib.pyplot as plt

# Data
years = [
    2010, 2011, 2012, 2013, 2014, 
    2015, 2016, 2017, 2018, 2019, 
    2020, 2021, 2022, 2023, 2024
]
physical_activity = [
    50, 55, 60, 65, 70, 
    75, 80, 85, 90, 95, 
    100, 105, 110, 115, 120
]
healthy_eating = [
    40, 42, 44, 45, 46, 
    48, 50, 52, 54, 56, 
    58, 60, 62, 64, 66
]
mental_health = [
    35, 37, 38, 40, 42, 
    43, 45, 46, 48, 50, 
    52, 53, 55, 57, 60
]
sleep_quality = [
    30, 32, 33, 34, 35, 
    36, 37, 38, 40, 42, 
    44, 46, 48, 50, 52
]

# Configuration for the figure size
plt.figure(figsize=(10, 12))

# Stacked bar chart
bar_width = 0.6
plt.bar(years, physical_activity, width=bar_width, color='#FF6F61', edgecolor='white', label='Physical Activity')
plt.bar(years, healthy_eating, width=bar_width, bottom=physical_activity, color='#6B5B95', edgecolor='white', label='Healthy Eating')
plt.bar(years, mental_health, width=bar_width, bottom=[i+j for i,j in zip(physical_activity, healthy_eating)], color='#88B04B', edgecolor='white', label='Mental Health')
plt.bar(years, sleep_quality, width=bar_width, bottom=[i+j+k for i,j,k in zip(physical_activity, healthy_eating, mental_health)], color='#FFA07A', edgecolor='white', label='Sleep Quality')

# Adding labels and title
plt.ylabel('Health Metrics', fontsize=14)
plt.xlabel('Year', fontsize=14)
plt.title('Trends in Health Metrics from 2010 to 2024', fontsize=16, pad=20)

# Show legend
plt.legend(loc='upper left', bbox_to_anchor=(1,1))

# Display the chart
plt.show()