
import matplotlib.pyplot as plt

# Data
years = [
    2010, 2011, 2012, 2013, 2014, 
    2015, 2016, 2017, 2018, 2019, 
    2020, 2021, 2022, 2023, 2024
]
education = [
    60, 62, 64, 66, 68, 
    70, 72, 74, 76, 78, 
    80, 82, 84, 86, 88
]
healthcare = [
    45, 48, 50, 52, 54, 
    56, 58, 60, 62, 64, 
    66, 68, 70, 72, 74
]
infrastructure = [
    40, 42, 44, 46, 48, 
    50, 52, 54, 56, 58, 
    60, 62, 64, 66, 68
]
defense = [
    35, 37, 38, 40, 42, 
    44, 46, 48, 50, 52, 
    54, 56, 58, 60, 62
]

# Configuration for the figure size
plt.figure(figsize=(14, 8))

# Stacked bar chart
bar_height = 0.6
plt.barh(years, education, height=bar_height, color='#2E8B57', edgecolor='white', label='Education')
plt.barh(years, healthcare, height=bar_height, left=education, color='#4682B4', edgecolor='white', label='Healthcare')
plt.barh(years, infrastructure, height=bar_height, left=[i+j for i,j in zip(education, healthcare)], color='#DAA520', edgecolor='white', label='Infrastructure')
plt.barh(years, defense, height=bar_height, left=[i+j+k for i,j,k in zip(education, healthcare, infrastructure)], color='#A52A2A', edgecolor='white', label='Defense')

# Adding labels and title
plt.xlabel('Government Spending (in Billion $)', fontsize=14)
plt.ylabel('Year', fontsize=14)
plt.title('Government Spending on Various Sectors (2010-2024)', fontsize=16, pad=20)

# Show legend
plt.legend(loc='upper right', bbox_to_anchor=(1,1))

# Adding numerical labels
for i in range(len(years)):
    plt.text(education[i]/2, years[i], str(education[i]), ha='center', va='center', color='white', fontsize=10)
    plt.text(education[i] + healthcare[i]/2, years[i], str(healthcare[i]), ha='center', va='center', color='white', fontsize=10)
    plt.text(education[i] + healthcare[i] + infrastructure[i]/2, years[i], str(infrastructure[i]), ha='center', va='center', color='white', fontsize=10)
    plt.text(education[i] + healthcare[i] + infrastructure[i] + defense[i]/2, years[i], str(defense[i]), ha='center', va='center', color='white', fontsize=10)

# Display the chart
plt.show()