
import matplotlib.pyplot as plt

# Given data
data = [
    {'Year': 2017, 'Average Daily Coffee Consumption (Cups)': 2.5, 'City': 'Amsterdam'},
    {'Year': 2018, 'Average Daily Coffee Consumption (Cups)': 2.8, 'City': 'Amsterdam'},
    {'Year': 2019, 'Average Daily Coffee Consumption (Cups)': 2.2, 'City': 'Amsterdam'},
    {'Year': 2020, 'Average Daily Coffee Consumption (Cups)': 2.7, 'City': 'Amsterdam'},
    {'Year': 2021, 'Average Daily Coffee Consumption (Cups)': 2.4, 'City': 'Amsterdam'},
    {'Year': 2022, 'Average Daily Coffee Consumption (Cups)': 2.9, 'City': 'Amsterdam'},
    {'Year': 2023, 'Average Daily Coffee Consumption (Cups)': 2.1, 'City': 'Amsterdam'},
    {'Year': 2024, 'Average Daily Coffee Consumption (Cups)': 2.3, 'City': 'Amsterdam'},
    {'Year': 2025, 'Average Daily Coffee Consumption (Cups)': 1.9, 'City': 'Amsterdam'},
    {'Year': 2026, 'Average Daily Coffee Consumption (Cups)': 2.0, 'City': 'Amsterdam'},
    {'Year': 2027, 'Average Daily Coffee Consumption (Cups)': 1.8, 'City': 'Amsterdam'},
    {'Year': 2028, 'Average Daily Coffee Consumption (Cups)': 1.6, 'City': 'Amsterdam'},
    {'Year': 2029, 'Average Daily Coffee Consumption (Cups)': 1.5, 'City': 'Amsterdam'},
    {'Year': 2030, 'Average Daily Coffee Consumption (Cups)': 1.3, 'City': 'Amsterdam'}
]

# Extracting Years and Average Daily Coffee Consumption from the data
years = [item['Year'] for item in data]
coffee_consumption = [item['Average Daily Coffee Consumption (Cups)'] for item in data]

# Creating the plot
plt.figure(figsize=(14, 7)) # Adjust size as needed

# Plotting the data
plt.plot(years, coffee_consumption, color='#2ca02c', linestyle='-', marker='s', 
         markerfacecolor='#d62728', markersize=10, linewidth=2, 
         label='Average Daily Coffee Consumption')

# Adding titles and labels
plt.title('Average Daily Coffee Consumption in Amsterdam Over the Years', fontsize=18, pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Average Daily Coffee Consumption (Cups)', fontsize=14)

# Adding grid
plt.grid(True)

# Adding legend
plt.legend(loc='upper right')

# Inverting y-axis
plt.gca().invert_yaxis()

# Adding annotations
for i, txt in enumerate(coffee_consumption):
    plt.annotate(txt, (years[i], coffee_consumption[i]), textcoords="offset points", xytext=(0,5), ha='center')

# Displaying the plot
plt.show()