
import matplotlib.pyplot as plt

# Data from the provided table
data = [
    {'Year': '2018', 'Apple': 45, 'Samsung': 10, 'Garmin': 6, 'Xiaomi': 9, 'Fitbit': 14, 'Others': 16},
    {'Year': '2019', 'Apple': 48, 'Samsung': 11, 'Garmin': 8, 'Xiaomi': 10, 'Fitbit': 12, 'Others': 11},
    {'Year': '2020', 'Apple': 50, 'Samsung': 9, 'Garmin': 10, 'Xiaomi': 11, 'Fitbit': 9, 'Others': 11},
    {'Year': '2021', 'Apple': 53, 'Samsung': 10, 'Garmin': 12, 'Xiaomi': 13, 'Fitbit': 6, 'Others': 6},
    {'Year': '2022', 'Apple': 55, 'Samsung': 12, 'Garmin': 11, 'Xiaomi': 10, 'Fitbit': 5, 'Others': 7},
    {'Year': '2023', 'Apple': 58, 'Samsung': 13, 'Garmin': 10, 'Xiaomi': 9, 'Fitbit': 4, 'Others': 6},
    {'Year': '2024(Projected)', 'Apple': 60, 'Samsung': 15, 'Garmin': 9, 'Xiaomi': 8, 'Fitbit': 3, 'Others': 5}
]

# Extracting brand names and years
brands = list(data[0].keys())[1:]  # Exclude 'Year' from the brand list
years = [entry['Year'] for entry in data]

# Calculate the total for each year to normalize the data
totals = [sum(entry.values()) - entry['Year'] for entry in data]

# Calculate the percentage of each brand for each year
percentages = [{brand: (entry[brand] / total * 100) for brand in brands} for entry, total in zip(data, totals)]

# Initialize the base of the stacked bars
bottom = [0] * len(years)

colors = plt.cm.tab20.colors  # Using tab20 colormap for a variety of colors

# Plotting each brand
for i, brand in enumerate(brands):
    # Extract the percentage for this brand across all years
    brand_perc = [entry[brand] for entry in percentages]
    
    plt.bar(years, brand_perc, bottom=bottom, label=brand, color=colors[i % len(colors)])
    
    # Update the bottom position for the next stack
    bottom = [sum(value) for value in zip(bottom, brand_perc)]

# Additional visual configurations
plt.xlabel('Year')
plt.ylabel('Percentage (%)')
plt.title('Market Share of Wearable Brands (100% Stacked Bar Chart)')
plt.legend(title='Brands', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot
plt.show()