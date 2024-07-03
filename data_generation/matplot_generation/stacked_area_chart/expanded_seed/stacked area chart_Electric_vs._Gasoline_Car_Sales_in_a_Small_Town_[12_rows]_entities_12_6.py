
import matplotlib.pyplot as plt

# Provided data
data = [
    {'Year': 2012, 'Electric Cars': 20, 'Hybrid Cars': 35, 'Gasoline Cars': 600},
    {'Year': 2013, 'Electric Cars': 25, 'Hybrid Cars': 40, 'Gasoline Cars': 590},
    {'Year': 2014, 'Electric Cars': 30, 'Hybrid Cars': 45, 'Gasoline Cars': 580},
    {'Year': 2015, 'Electric Cars': 35, 'Hybrid Cars': 50, 'Gasoline Cars': 570},
    {'Year': 2016, 'Electric Cars': 40, 'Hybrid Cars': 60, 'Gasoline Cars': 550},
    {'Year': 2017, 'Electric Cars': 50, 'Hybrid Cars': 70, 'Gasoline Cars': 525},
    {'Year': 2018, 'Electric Cars': 60, 'Hybrid Cars': 80, 'Gasoline Cars': 500},
    {'Year': 2019, 'Electric Cars': 70, 'Hybrid Cars': 90, 'Gasoline Cars': 450},
    {'Year': 2020, 'Electric Cars': 85, 'Hybrid Cars': 100, 'Gasoline Cars': 300},
    {'Year': 2021, 'Electric Cars': 100, 'Hybrid Cars': 110, 'Gasoline Cars': 250},
    {'Year': 2022, 'Electric Cars': 120, 'Hybrid Cars': 120, 'Gasoline Cars': 200},
    {'Year': 2023, 'Electric Cars': 140, 'Hybrid Cars': 130, 'Gasoline Cars': 150}
]

# Extracting data for plotting
years = [entry['Year'] for entry in data]
electric_cars = [entry['Electric Cars'] for entry in data]
hybrid_cars = [entry['Hybrid Cars'] for entry in data]
gasoline_cars = [entry['Gasoline Cars'] for entry in data]

# Create the figure and axis objects
fig, ax = plt.subplots(figsize=(10, 6))

# Create the stackplot
ax.stackplot(years, electric_cars, hybrid_cars, gasoline_cars, labels=['Electric Cars', 'Hybrid Cars', 'Gasoline Cars'], colors=['#1f77b4', '#2ca02c', '#d62728'], alpha=0.6)

# Add title and labels
ax.set_title('Car Sales by Type from 2012 to 2023', fontsize=14)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Number of Cars Sold', fontsize=12)

# Add grid lines
ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)

# Add legend
ax.legend(loc='upper left')

# Customize the x-axis to show every year
plt.xticks(years, rotation=45)

# Tight layout to ensure everything fits without overlapping
plt.tight_layout()

# Display the plot
plt.show()