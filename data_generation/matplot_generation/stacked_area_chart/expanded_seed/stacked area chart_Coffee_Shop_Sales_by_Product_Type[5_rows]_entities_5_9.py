
import matplotlib.pyplot as plt

# Provided data
data = [
    {'Year': 2018, 'Espresso': 12000, 'Lattes': 18000, 'Americanos': 7000, 'Teas': 8000, 'Pastries': 15000},
    {'Year': 2019, 'Espresso': 13000, 'Lattes': 19000, 'Americanos': 7500, 'Teas': 8500, 'Pastries': 16000},
    {'Year': 2020, 'Espresso': 11000, 'Lattes': 17000, 'Americanos': 6800, 'Teas': 9000, 'Pastries': 14000},
    {'Year': 2021, 'Espresso': 14000, 'Lattes': 20000, 'Americanos': 8000, 'Teas': 9500, 'Pastries': 16500},
    {'Year': 2022, 'Espresso': 15000, 'Lattes': 21000, 'Americanos': 8500, 'Teas': 10000, 'Pastries': 17000}
]

# Extracting individual lists for plotting
years = [item['Year'] for item in data]
espresso = [item['Espresso'] for item in data]
lattes = [item['Lattes'] for item in data]
americanos = [item['Americanos'] for item in data]
teas = [item['Teas'] for item in data]
pastries = [item['Pastries'] for item in data]

# Plotting the stacked area chart
plt.stackplot(years, espresso, lattes, americanos, teas, pastries, labels=['Espresso', 'Lattes', 'Americanos', 'Teas', 'Pastries'],
               colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'], alpha=0.8)

# Adding labels, title, and legend
plt.xlabel('Year')
plt.ylabel('Sales Amount')
plt.title('Beverage and Pastry Sales Over Time')
plt.legend(loc='upper left')

# Customizing ticks on the x-axis for better readability
plt.xticks(years)

# Display the plot
plt.show()