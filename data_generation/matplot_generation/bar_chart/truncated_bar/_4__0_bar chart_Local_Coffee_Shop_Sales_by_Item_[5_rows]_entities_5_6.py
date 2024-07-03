
import matplotlib.pyplot as plt

# Data for plotting
years = [
    2011, 2012, 2013, 2014, 2015, 2016,
    2017, 2018, 2019, 2020, 2021
]
new_york = [1200, 1400, 1250, 1300, 1350, 1280, 1320, 1400, 1450, 1500, 1550]
los_angeles = [380, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490]
chicago = [910, 920, 930, 940, 950, 960, 970, 980, 990, 1000, 1010]
houston = [1300, 1250, 1350, 1400, 1450, 1500, 1550, 1600, 1650, 1700, 1750]
phoenix = [200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400]

# Changing figure size
plt.figure(figsize=(12, 10))

# Plotting - vertical bar chart
bar_width = 0.4
plt.bar(years, new_york, color='#1f77b4', width=bar_width, label='New York')
plt.bar([year + bar_width for year in years], los_angeles, color='#ff7f0e', width=bar_width, label='Los Angeles')
plt.bar([year + 2*bar_width for year in years], chicago, color='#2ca02c', width=bar_width, label='Chicago')
plt.bar([year + 3*bar_width for year in years], houston, color='#d62728', width=bar_width, label='Houston')
plt.bar([year + 4*bar_width for year in years], phoenix, color='#9467bd', width=bar_width, label='Phoenix')

# Customize chart
plt.xlabel('Year', fontsize=14)
plt.ylabel('Rainfall (mm)', fontsize=14)
plt.title('Annual Rainfall in Major Cities', fontsize=16)

# Resize bar width and set y-axis limit
plt.ylim(300, 1800)

# Resize bar height
plt.xticks([year + 2*bar_width for year in years], [str(year) for year in years], fontsize=10)

# Show legend
plt.legend()

# Show plot
plt.show()