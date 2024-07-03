
import matplotlib.pyplot as plt

# Data
years = [
    2010, 2011, 2012, 2013, 2014, 
    2015, 2016, 2017, 2018, 2019, 
    2020, 2021, 2022, 2023, 2024
]
research_and_development = [
    60, 65, 70, 75, 80, 
    85, 90, 95, 100, 105, 
    110, 115, 120, 125, 130
]
marketing = [
    50, 55, 60, 62, 65, 
    68, 70, 72, 75, 78, 
    80, 83, 85, 88, 90
]
sales = [
    40, 42, 45, 46, 48, 
    50, 52, 54, 56, 58, 
    60, 62, 64, 66, 68
]
customer_support = [
    35, 37, 38, 40, 42, 
    43, 45, 46, 48, 50, 
    52, 53, 55, 57, 60
]

# Configuration for the figure size
plt.figure(figsize=(12, 10))

# Stacked bar chart
bar_height = 0.5
plt.barh(years, research_and_development, height=bar_height, color='#1f77b4', edgecolor='white', label='Research and Development')
plt.barh(years, marketing, height=bar_height, left=research_and_development, color='#ff7f0e', edgecolor='white', label='Marketing')
plt.barh(years, sales, height=bar_height, left=[i+j for i,j in zip(research_and_development, marketing)], color='#2ca02c', edgecolor='white', label='Sales')
plt.barh(years, customer_support, height=bar_height, left=[i+j+k for i,j,k in zip(research_and_development, marketing, sales)], color='#d62728', edgecolor='white', label='Customer Support')

# Adding labels and title
plt.xlabel('Investment (in millions)', fontsize=14)
plt.ylabel('Year', fontsize=14)
plt.title('Annual Investment in Various Business Areas from 2010 to 2024', fontsize=16, pad=20)

# Show legend
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=2)

# Display the chart
plt.show()