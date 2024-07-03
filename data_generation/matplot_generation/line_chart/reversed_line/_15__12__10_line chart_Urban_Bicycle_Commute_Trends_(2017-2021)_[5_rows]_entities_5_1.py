
import matplotlib.pyplot as plt

# Given data
data = [
    {'Year': 2025, 'Projected Annual Expenditure (Million USD)': 450},
    {'Year': 2026, 'Projected Annual Expenditure (Million USD)': 470},
    {'Year': 2027, 'Projected Annual Expenditure (Million USD)': 490},
    {'Year': 2028, 'Projected Annual Expenditure (Million USD)': 480},
    {'Year': 2029, 'Projected Annual Expenditure (Million USD)': 510},
    {'Year': 2030, 'Projected Annual Expenditure (Million USD)': 500},
    {'Year': 2031, 'Projected Annual Expenditure (Million USD)': 530},
    {'Year': 2032, 'Projected Annual Expenditure (Million USD)': 520},
    {'Year': 2033, 'Projected Annual Expenditure (Million USD)': 550},
    {'Year': 2034, 'Projected Annual Expenditure (Million USD)': 540},
    {'Year': 2035, 'Projected Annual Expenditure (Million USD)': 560},
    {'Year': 2036, 'Projected Annual Expenditure (Million USD)': 550},
    {'Year': 2037, 'Projected Annual Expenditure (Million USD)': 570},
    {'Year': 2038, 'Projected Annual Expenditure (Million USD)': 560}
]

# Extracting Years and Projected Annual Expenditure from the data
years = [item['Year'] for item in data]
expenditure = [item['Projected Annual Expenditure (Million USD)'] for item in data]

# Creating the plot
plt.figure(figsize=(16, 8)) # Adjust size as needed

# Plotting the data
plt.plot(years, expenditure, color='#1E90FF', linestyle='-', marker='o', 
         markerfacecolor='#FFD700', markersize=8, linewidth=2, 
         label='Projected Annual Expenditure')

# Adding titles and labels
plt.title('Projected Annual Expenditure in Emerging Technologies Over the Years', fontsize=18, pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Projected Annual Expenditure (Million USD)', fontsize=14)

# Adding grid
plt.grid(True)

# Adding legend
plt.legend(loc='upper left')

# Invert y-axis
plt.gca().invert_yaxis()

# Adding annotations
for i, txt in enumerate(expenditure):
    plt.annotate(txt, (years[i], expenditure[i]), textcoords="offset points", xytext=(0,5), ha='center')

# Displaying the plot
plt.show()