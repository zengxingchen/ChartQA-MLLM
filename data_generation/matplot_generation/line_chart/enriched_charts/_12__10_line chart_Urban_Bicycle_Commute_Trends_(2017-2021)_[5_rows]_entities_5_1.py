
import matplotlib.pyplot as plt

# Given data
data = [
    {'Year': 2017, 'Average Annual Rainfall (mm)': 850},
    {'Year': 2018, 'Average Annual Rainfall (mm)': 890},
    {'Year': 2019, 'Average Annual Rainfall (mm)': 920},
    {'Year': 2020, 'Average Annual Rainfall (mm)': 870},
    {'Year': 2021, 'Average Annual Rainfall (mm)': 940},
    {'Year': 2022, 'Average Annual Rainfall (mm)': 915},
    {'Year': 2023, 'Average Annual Rainfall (mm)': 960},
    {'Year': 2024, 'Average Annual Rainfall (mm)': 930},
    {'Year': 2025, 'Average Annual Rainfall (mm)': 970},
    {'Year': 2026, 'Average Annual Rainfall (mm)': 940},
    {'Year': 2027, 'Average Annual Rainfall (mm)': 980},
    {'Year': 2028, 'Average Annual Rainfall (mm)': 950},
    {'Year': 2029, 'Average Annual Rainfall (mm)': 990},
    {'Year': 2030, 'Average Annual Rainfall (mm)': 960}
]

# Extracting Years and Average Annual Rainfall from the data
years = [item['Year'] for item in data]
rainfall = [item['Average Annual Rainfall (mm)'] for item in data]

# Creating the plot
plt.figure(figsize=(14, 7)) # Adjust size as needed

# Plotting the data
plt.plot(years, rainfall, color='#4CAF50', linestyle='-', marker='s', 
         markerfacecolor='#FF5722', markersize=8, linewidth=2, 
         label='Average Annual Rainfall')

# Adding titles and labels
plt.title('Average Annual Rainfall in Amsterdam Over the Years', fontsize=18, pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Average Annual Rainfall (mm)', fontsize=14)

# Adding grid
plt.grid(True)

# Adding legend
plt.legend(loc='upper right')

# Adding annotations
for i, txt in enumerate(rainfall):
    plt.annotate(txt, (years[i], rainfall[i]), textcoords="offset points", xytext=(0,5), ha='center')

# Displaying the plot
plt.show()