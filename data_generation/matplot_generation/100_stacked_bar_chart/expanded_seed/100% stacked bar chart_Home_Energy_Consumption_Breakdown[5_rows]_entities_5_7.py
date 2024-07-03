
import matplotlib.pyplot as plt
import numpy as np

# Data provided
data = [
    {'Year': 2019, 'Heating/Cooling': '42%', 'Water Heating': '20%', 'Appliances': '17%', 'Lighting': '10%', 'Electronics': '11%'},
    {'Year': 2020, 'Heating/Cooling': '40%', 'Water Heating': '21%', 'Appliances': '18%', 'Lighting': '9%', 'Electronics': '12%'},
    {'Year': 2021, 'Heating/Cooling': '38%', 'Water Heating': '22%', 'Appliances': '19%', 'Lighting': '8%', 'Electronics': '13%'},
    {'Year': 2022, 'Heating/Cooling': '37%', 'Water Heating': '23%', 'Appliances': '17%', 'Lighting': '7%', 'Electronics': '16%'},
    {'Year': 2023, 'Heating/Cooling': '35%', 'Water Heating': '24%', 'Appliances': '18%', 'Lighting': '6%', 'Electronics': '17%'}
]

# Extract year labels
years = [d['Year'] for d in data]

# Convert string percentages to floats and stack them for plotting
categories = ['Heating/Cooling', 'Water Heating', 'Appliances', 'Lighting', 'Electronics']
stacked_data = np.zeros((len(data), len(categories)))

for i, d in enumerate(data):
    for j, category in enumerate(categories):
        stacked_data[i, j] = float(d[category].strip('%'))

# Normalize the data to sum to 1 (100%)
stacked_data /= stacked_data.sum(axis=1)[:, np.newaxis]

# Plotting
fig, ax = plt.subplots()

# Colors for each category
colors = ['skyblue', 'sandybrown', 'limegreen', 'gold', 'lightcoral']

# Bottom of the bars
bottoms = np.zeros(len(data))

for idx, (category, color) in enumerate(zip(categories, colors)):
    ax.bar(years, stacked_data[:, idx], bottom=bottoms, color=color, edgecolor='white', label=category)
    bottoms += stacked_data[:, idx]

# Formatting the plot
ax.set_title('Energy Consumption by Category (Percentage)')
ax.set_xlabel('Year')
ax.set_ylabel('Percentage')
plt.xticks(years)
plt.yticks(np.arange(0, 1.1, 0.1), [f"{int(y*100)}%" for y in np.arange(0, 1.1, 0.1)])
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=len(categories))

# Display the stacked bar chart
plt.tight_layout()
plt.show()