
import matplotlib.pyplot as plt

# Data
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
basketball = [1100, 1300, 1350, 1450, 1550, 1650, 1750, 1850, 1900, 2000]
football = [2300, 2400, 2500, 2650, 2800, 2900, 3000, 3100, 3250, 3400]
tennis = [1600, 1700, 1750, 1850, 1950, 2000, 2150, 2250, 2350, 2450]
swimming = [2700, 2800, 2900, 2950, 3050, 3150, 3250, 3350, 3450, 3550]

# Configuration for the figure size
plt.figure(figsize=(16, 10))

# Stacked horizontal bar chart
plt.barh(years, basketball, height=0.7, color='#1f77b4', edgecolor='white', label='Basketball')
plt.barh(years, football, height=0.7, left=basketball, color='#ff7f0e', edgecolor='white', label='Football')
plt.barh(years, tennis, height=0.7, left=[i+j for i,j in zip(basketball, football)], color='#2ca02c', edgecolor='white', label='Tennis')
plt.barh(years, swimming, height=0.7, left=[i+j+k for i,j,k in zip(basketball, football, tennis)], color='#d62728', edgecolor='white', label='Swimming')

# Adding labels and title
plt.xlabel('Funding (in Million USD)', fontsize=14)
plt.ylabel('Year', fontsize=14)
plt.title('Sports Funding by Category from 2010 to 2019', fontsize=16, pad=20)

# Adding numerical labels
for year, bball, fball, ten, swim in zip(years, basketball, football, tennis, swimming):
    plt.text(bball / 2, year, str(bball), ha='center', va='center', fontsize=10, color='white')
    plt.text(bball + fball / 2, year, str(fball), ha='center', va='center', fontsize=10, color='white')
    plt.text(bball + fball + ten / 2, year, str(ten), ha='center', va='center', fontsize=10, color='white')
    plt.text(bball + fball + ten + swim / 2, year, str(swim), ha='center', va='center', fontsize=10, color='white')

# Show legend
plt.legend(loc='lower right')

# Display the chart
plt.show()