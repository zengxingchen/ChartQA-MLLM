
import matplotlib.pyplot as plt

# Data for stacked area chart
years = range(2012, 2023)
science_fiction = [12000, 13000, 13500, 14000, 14500, 15000, 15500, 16000, 16500, 17000, 17500]
fantasy = [15000, 16000, 16500, 17000, 18000, 18500, 19000, 20000, 20500, 21000, 22000]
mystery = [25000, 26000, 27000, 27500, 28000, 28500, 29000, 29500, 30000, 30500, 31000]
non_fiction = [50000, 52000, 53000, 54000, 56000, 57000, 58000, 60000, 62000, 63000, 65000]

# Plot
plt.figure(figsize=(16, 12))  # Change width and height of the chart
plt.stackplot(years, science_fiction, fantasy, mystery, non_fiction, 
              colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])

# Customize the plot
plt.title('Book Sales by Genre from 2012 to 2022', fontsize=18)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Number of Books Sold', fontsize=14)
plt.legend(['Science Fiction', 'Fantasy', 'Mystery', 'Non-Fiction'], loc='upper left')

# Annotation
for i, y in enumerate(years):
    plt.annotate(f'{science_fiction[i]}', (y, science_fiction[i]), textcoords="offset points", xytext=(0,10), ha='center')

plt.show()