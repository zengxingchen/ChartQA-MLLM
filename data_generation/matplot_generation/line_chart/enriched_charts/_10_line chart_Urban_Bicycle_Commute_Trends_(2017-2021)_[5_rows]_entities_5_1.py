
import matplotlib.pyplot as plt

# Given data
data = [
    {'Year': 2017, 'Average Daily Steps (Thousands)': 7.5, 'City': 'Amsterdam'},
    {'Year': 2018, 'Average Daily Steps (Thousands)': 7.8, 'City': 'Amsterdam'},
    {'Year': 2019, 'Average Daily Steps (Thousands)': 8.2, 'City': 'Amsterdam'},
    {'Year': 2020, 'Average Daily Steps (Thousands)': 7.9, 'City': 'Amsterdam'},
    {'Year': 2021, 'Average Daily Steps (Thousands)': 8.5, 'City': 'Amsterdam'},
    {'Year': 2022, 'Average Daily Steps (Thousands)': 8.0, 'City': 'Amsterdam'},
    {'Year': 2023, 'Average Daily Steps (Thousands)': 8.7, 'City': 'Amsterdam'},
    {'Year': 2024, 'Average Daily Steps (Thousands)': 8.3, 'City': 'Amsterdam'},
    {'Year': 2025, 'Average Daily Steps (Thousands)': 9.0, 'City': 'Amsterdam'},
    {'Year': 2026, 'Average Daily Steps (Thousands)': 8.6, 'City': 'Amsterdam'},
    {'Year': 2027, 'Average Daily Steps (Thousands)': 9.2, 'City': 'Amsterdam'},
    {'Year': 2028, 'Average Daily Steps (Thousands)': 8.8, 'City': 'Amsterdam'},
    {'Year': 2029, 'Average Daily Steps (Thousands)': 9.5, 'City': 'Amsterdam'},
    {'Year': 2030, 'Average Daily Steps (Thousands)': 9.1, 'City': 'Amsterdam'}
]

# Extracting Years and Average Daily Steps from the data
years = [item['Year'] for item in data]
steps = [item['Average Daily Steps (Thousands)'] for item in data]

# Creating the plot
plt.figure(figsize=(12, 6)) # Adjust size as needed

# Plotting the data
plt.plot(years, steps, color='#1f77b4', linestyle='-', marker='o', 
         markerfacecolor='#ff7f0e', markersize=10, linewidth=2, 
         label='Average Daily Steps')

# Adding titles and labels
plt.title('Average Daily Steps in Amsterdam Over the Years', fontsize=18, pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Average Daily Steps (Thousands)', fontsize=14)

# Adding grid
plt.grid(True)

# Adding legend
plt.legend(loc='upper left')

# Adding annotations
for i, txt in enumerate(steps):
    plt.annotate(txt, (years[i], steps[i]), textcoords="offset points", xytext=(0,5), ha='center')

# Displaying the plot
plt.show()