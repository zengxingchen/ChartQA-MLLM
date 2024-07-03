
import matplotlib.pyplot as plt

# Data
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
expenditure = [500, 550, 620, 680, 710, 750, 800, 850, 920, 980, 1030, 1080, 1150, 1200]

# Plot
plt.figure(figsize=(12, 8))
plt.fill_between(years, expenditure, color='#FF5733', alpha=0.7)

# Titles and labels
plt.title('Annual Expenditure on Space Exploration', fontsize=18)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Expenditure (in millions)', fontsize=14)

# Annotations
for i, txt in enumerate(expenditure):
    plt.annotate(txt, (years[i], expenditure[i]), textcoords="offset points", xytext=(0, 5), ha='center')

# Display the plot
plt.show()