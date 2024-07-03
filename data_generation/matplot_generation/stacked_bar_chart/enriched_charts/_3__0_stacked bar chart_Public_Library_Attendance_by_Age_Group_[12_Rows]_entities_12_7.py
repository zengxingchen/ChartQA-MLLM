
import matplotlib.pyplot as plt

# Data
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
technology = [3500, 3700, 3900, 4100, 4300, 4500, 4700, 4900, 5100, 5300]
healthcare = [2000, 2200, 2400, 2600, 2800, 3000, 3200, 3400, 3600, 3800]
finance = [1500, 1700, 1900, 2100, 2300, 2500, 2700, 2900, 3100, 3300]
education = [1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800]

# Configuration for the figure size
plt.figure(figsize=(12, 10))

# Stacked vertical bar chart
plt.bar(years, technology, width=0.6, color='#1f77b4', edgecolor='white', label='Technology')
plt.bar(years, healthcare, width=0.6, bottom=technology, color='#ff7f0e', edgecolor='white', label='Healthcare')
plt.bar(years, finance, width=0.6, bottom=[i+j for i,j in zip(technology, healthcare)], color='#2ca02c', edgecolor='white', label='Finance')
plt.bar(years, education, width=0.6, bottom=[i+j+k for i,j,k in zip(technology, healthcare, finance)], color='#d62728', edgecolor='white', label='Education')

# Adding labels and title
plt.ylabel('Revenue (in Millions)', fontsize=14)
plt.xlabel('Year', fontsize=14)
plt.title('Annual Revenue by Sector from 2010 to 2019', fontsize=16)

# Adding numerical labels
for i in range(len(years)):
    plt.text(years[i], technology[i] / 2, f'{technology[i]}', ha='center', va='center', color='white', fontsize=10)
    plt.text(years[i], technology[i] + healthcare[i] / 2, f'{healthcare[i]}', ha='center', va='center', color='white', fontsize=10)
    plt.text(years[i], technology[i] + healthcare[i] + finance[i] / 2, f'{finance[i]}', ha='center', va='center', color='white', fontsize=10)
    plt.text(years[i], technology[i] + healthcare[i] + finance[i] + education[i] / 2, f'{education[i]}', ha='center', va='center', color='white', fontsize=10)

# Show legend
plt.legend(loc='upper left', bbox_to_anchor=(1,1))

# Display the chart
plt.tight_layout()
plt.show()