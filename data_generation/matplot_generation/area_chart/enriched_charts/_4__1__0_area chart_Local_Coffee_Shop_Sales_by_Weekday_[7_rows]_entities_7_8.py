
import matplotlib.pyplot as plt

# Data
years = [
    2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 
    2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 
    2020, 2021, 2022, 2023
]
revenue = [
    30, 35, 40, 45, 50, 55, 65, 75, 85, 95, 105, 115, 130, 145, 
    160, 180, 195, 210, 225, 240, 260, 280, 300, 320
]

# Plot
plt.figure(figsize=(14, 9))
plt.fill_between(years, revenue, color='#3366FF', alpha=0.7)

# Titles and labels
plt.title('Annual Revenue from Online Courses', fontsize=18, pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Revenue (in millions)', fontsize=14)

# Annotations
for i, txt in enumerate(revenue):
    plt.annotate(txt, (years[i], revenue[i]), textcoords="offset points", xytext=(0, 5), ha='center')

# Display the plot
plt.show()