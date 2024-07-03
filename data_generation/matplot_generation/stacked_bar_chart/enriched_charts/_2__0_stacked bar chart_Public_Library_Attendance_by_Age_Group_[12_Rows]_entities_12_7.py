
import matplotlib.pyplot as plt

# Data
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
education = [1000, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]
science = [2000, 2200, 2400, 2600, 2800, 3000, 3200, 3400, 3600, 3800]
arts = [1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400]
technology = [2500, 2700, 2800, 2900, 3000, 3100, 3200, 3300, 3400, 3500]

# Configuration for the figure size
plt.figure(figsize=(10, 16))

# Stacked vertical bar chart
plt.bar(years, education, width=0.7, color='#3498db', edgecolor='white', label='Education')
plt.bar(years, science, width=0.7, bottom=education, color='#2ecc71', edgecolor='white', label='Science')
plt.bar(years, arts, width=0.7, bottom=[i+j for i,j in zip(education, science)], color='#f1c40f', edgecolor='white', label='Arts')
plt.bar(years, technology, width=0.7, bottom=[i+j+k for i,j,k in zip(education, science, arts)], color='#e74c3c', edgecolor='white', label='Technology')

# Adding labels and title
plt.ylabel('Research Funding (in Million USD)', fontsize=14)
plt.xlabel('Year', fontsize=14)
plt.title('Research Funding by Sector from 2010 to 2019', fontsize=16)

# Adding numerical labels
for year, edu, sci, art, tech in zip(years, education, science, arts, technology):
    plt.text(year, edu / 2, str(edu), ha='center', va='center', fontsize=10, color='white')
    plt.text(year, edu + sci / 2, str(sci), ha='center', va='center', fontsize=10, color='white')
    plt.text(year, edu + sci + art / 2, str(art), ha='center', va='center', fontsize=10, color='white')
    plt.text(year, edu + sci + art + tech / 2, str(tech), ha='center', va='center', fontsize=10, color='white')

# Show legend
plt.legend(loc='upper right')

# Display the chart
plt.show()