
import matplotlib.pyplot as plt

# Given data
data = [
    {'Year': 2017, 'Average Daily Water Consumption (Liters)': 120},
    {'Year': 2018, 'Average Daily Water Consumption (Liters)': 125},
    {'Year': 2019, 'Average Daily Water Consumption (Liters)': 130},
    {'Year': 2020, 'Average Daily Water Consumption (Liters)': 128},
    {'Year': 2021, 'Average Daily Water Consumption (Liters)': 135},
    {'Year': 2022, 'Average Daily Water Consumption (Liters)': 132},
    {'Year': 2023, 'Average Daily Water Consumption (Liters)': 140},
    {'Year': 2024, 'Average Daily Water Consumption (Liters)': 138},
    {'Year': 2025, 'Average Daily Water Consumption (Liters)': 145},
    {'Year': 2026, 'Average Daily Water Consumption (Liters)': 142},
    {'Year': 2027, 'Average Daily Water Consumption (Liters)': 150},
    {'Year': 2028, 'Average Daily Water Consumption (Liters)': 148},
    {'Year': 2029, 'Average Daily Water Consumption (Liters)': 155},
    {'Year': 2030, 'Average Daily Water Consumption (Liters)': 153}
]

# Extracting Years and Average Daily Water Consumption from the data
years = [item['Year'] for item in data]
water_consumption = [item['Average Daily Water Consumption (Liters)'] for item in data]

# Creating the plot
plt.figure(figsize=(14, 7))  # Adjust size as needed

# Plotting the data
plt.plot(years, water_consumption, color='#3498db', linestyle='-', marker='s', 
         markerfacecolor='#e74c3c', markersize=10, linewidth=2, 
         label='Average Daily Water Consumption')

# Adding titles and labels
plt.title('Average Daily Water Consumption in Liters Over the Years', fontsize=18, pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Average Daily Water Consumption (Liters)', fontsize=14)

# Adding grid
plt.grid(True)

# Adding legend
plt.legend(loc='upper right')

# Adding annotations
for i, txt in enumerate(water_consumption):
    plt.annotate(txt, (years[i], water_consumption[i]), textcoords="offset points", xytext=(0,5), ha='center')

# Displaying the plot
plt.show()