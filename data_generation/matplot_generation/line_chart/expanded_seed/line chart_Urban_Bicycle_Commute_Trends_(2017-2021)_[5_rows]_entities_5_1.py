
import matplotlib.pyplot as plt

# Given data
data = [
    {'Year': 2017, 'Number of Commuters (Thousands)': 45, 'City': 'Amsterdam'},
    {'Year': 2018, 'Number of Commuters (Thousands)': 47, 'City': 'Amsterdam'},
    {'Year': 2019, 'Number of Commuters (Thousands)': 50, 'City': 'Amsterdam'},
    {'Year': 2020, 'Number of Commuters (Thousands)': 52, 'City': 'Amsterdam'},
    {'Year': 2021, 'Number of Commuters (Thousands)': 53, 'City': 'Amsterdam'}
]

# Extracting Years and Number of Commuters from the data
years = [item['Year'] for item in data]
commuters = [item['Number of Commuters (Thousands)'] for item in data]

# Creating the plot
plt.figure(figsize=(10, 5)) # Adjust size as needed

# Plotting the data
plt.plot(years, commuters, color='blue', linestyle='-', marker='o', 
         markerfacecolor='red', markersize=12, linewidth=2, 
         label='Number of Commuters')

# Adding titles and labels
plt.title('Number of Commuters in Amsterdam Over the Years', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Number of Commuters (Thousands)', fontsize=14)

# Adding grid
plt.grid(True)

# Adding legend
plt.legend()

# Displaying the plot
plt.show()