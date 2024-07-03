
import matplotlib.pyplot as plt

# Data points
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
travelers = [850, 900, 950, 980, 1000, 1050, 1070, 1100, 1150, 1200, 500, 600, 1300, 1350]

# Create figure and plot
fig, ax = plt.subplots(figsize=(12, 6))

# Change the color scheme using specific hex codes
ax.plot(years, travelers, color='#1E90FF', marker='o')

# Set the title and labels
ax.set_title('Annual Global Air Travelers', fontsize=16, pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Travelers (millions)', fontsize=14)

# Adding annotations/labels
for (year, traveler) in zip(years, travelers):
    ax.annotate(f'{traveler}M', xy=(year, traveler), textcoords="offset points", xytext=(0,10), ha='center')

plt.grid(True)
plt.show()