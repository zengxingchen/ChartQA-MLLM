
import matplotlib.pyplot as plt

# Data from the table provided
years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021']
technology = [100, 120, 130, 150, 170, 200, 220]
healthcare = [80, 85, 90, 95, 100, 110, 120]
finance = [90, 95, 100, 110, 120, 130, 140]
retail = [60, 70, 75, 80, 85, 90, 100]

# Stacking data
healthcare_bottom = [technology[i] for i in range(len(technology))]
finance_bottom = [healthcare_bottom[i] + healthcare[i] for i in range(len(healthcare))]
retail_bottom = [finance_bottom[i] + finance[i] for i in range(len(finance))]

# Setting figure size
plt.figure(figsize=(12, 10))

# Plotting data
bar_width = 0.8
plt.bar(years, technology, width=bar_width, color='#1f77b4', edgecolor='white', label='Technology')
plt.bar(years, healthcare, bottom=healthcare_bottom, width=bar_width, color='#ff7f0e', edgecolor='white', label='Healthcare')
plt.bar(years, finance, bottom=finance_bottom, width=bar_width, color='#2ca02c', edgecolor='white', label='Finance')
plt.bar(years, retail, bottom=retail_bottom, width=bar_width, color='#d62728', edgecolor='white', label='Retail')

# Adding titles and labels
plt.xlabel('Year')
plt.ylabel('Revenue in Millions')
plt.title('Annual Revenue by Business Sector (2015-2021)')
plt.legend(loc='upper left')

# Display the plot
plt.show()