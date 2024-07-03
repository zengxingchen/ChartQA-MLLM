
import matplotlib.pyplot as plt

# Data
years = [
    2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 
    2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 
    2029, 2030, 2031
]
visitors = [
    100, 120, 150, 180, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 
    700, 800, 850, 900, 950, 1000, 1100, 1150, 1200, 1250, 1300, 1350, 1400
]

# Plot
plt.figure(figsize=(16, 12))
plt.fill_between(years, visitors, color='#FF6347', alpha=0.7)

# Titles and labels
plt.title('Annual Visitors to the Art Gallery', fontsize=22, pad=20)
plt.xlabel('Year', fontsize=18)
plt.ylabel('Visitors (in thousands)', fontsize=18)

# Annotations
for i, txt in enumerate(visitors):
    plt.annotate(txt, (years[i], visitors[i]), textcoords="offset points", xytext=(0, 5), ha='center')

# Display the plot
plt.show()