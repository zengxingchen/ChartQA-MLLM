
import matplotlib.pyplot as plt

# Data
years = [2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027]
revenue = [400, 450, 470, 500, 550, 580, 610, 630, 660, 700, 750, 800, 850, 900, 950, 1000, 1100, 1150, 1200, 1250, 1300, 1350, 1400]

# Plot
plt.figure(figsize=(14, 10))
plt.fill_between(years, revenue, color='#1F77B4', alpha=0.6)

# Titles and labels
plt.title('Annual Revenue of Tech Startup', fontsize=20)
plt.xlabel('Year', fontsize=16)
plt.ylabel('Revenue (in millions)', fontsize=16)

# Annotations
for i, txt in enumerate(revenue):
    plt.annotate(txt, (years[i], revenue[i]), textcoords="offset points", xytext=(0, 5), ha='center')

# Display the plot
plt.show()