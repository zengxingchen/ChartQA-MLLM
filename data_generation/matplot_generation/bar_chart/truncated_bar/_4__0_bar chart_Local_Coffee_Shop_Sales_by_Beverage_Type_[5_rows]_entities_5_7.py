
import matplotlib.pyplot as plt

# Data
years = [
    2011, 2012, 2013, 2014, 2015,
    2016, 2017, 2018, 2019, 2020,
    2021, 2022
]
concerts = [
    120, 160, 210, 330, 450,
    600, 810, 1020, 1300, 1650,
    2000, 2450
]

# Plot configuration
plt.figure(figsize=(16, 10))
bars = plt.bar(years, concerts, width=0.7, color=[
    '#4B0082', '#FF6347', '#4682B4', '#32CD32',
    '#FFD700', '#8A2BE2', '#FF4500', '#2E8B57',
    '#DA70D6', '#FF1493', '#00BFFF', '#FFD700',
])

# Axes labels and title
plt.ylabel('Number of Concerts')
plt.xlabel('Year')
plt.title('Annual Number of Concerts (2011-2022)', pad=20)

# Set y-axis limit
plt.ylim(100, 2500)

# Show the plot
plt.show()