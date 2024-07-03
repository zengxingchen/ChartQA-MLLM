
import matplotlib.pyplot as plt
import squarify

# Your data
data = [
    {'Category': 'Heating', 'Subcategory': 'Central Heating', 'Annual Consumption (kWh)': 7000},
    {'Category': 'Heating', 'Subcategory': 'Water Heating', 'Annual Consumption (kWh)': 2500},
    {'Category': 'Appliances', 'Subcategory': 'Refrigerator', 'Annual Consumption (kWh)': 600},
    {'Category': 'Appliances', 'Subcategory': 'Washing Machine', 'Annual Consumption (kWh)': 150},
    {'Category': 'Lighting', 'Subcategory': 'Indoor Lighting', 'Annual Consumption (kWh)': 300}
]

# Parse the data
categories = list(set([d['Category'] for d in data]))  # Get unique categories
colors = plt.cm.Spectral([0.1 + 0.8*i/len(set(categories)) for i in range(len(set(categories)))])  # Generate colors
color_dict = dict(zip(categories, colors))  # Map categories to colors

sizes = [d['Annual Consumption (kWh)'] for d in data]  # Sizes for the rectangles
labels = ["{}\n{} kWh".format(d['Subcategory'], d['Annual Consumption (kWh)']) for d in data]
colors = [color_dict[d['Category']] for d in data]

# Plot
plt.figure(figsize=(12, 8))
squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.8)
plt.title('Annual Energy Consumption by Category and Subcategory')
plt.axis('off')

# Add legend
import matplotlib.patches as mpatches
legend_handles = [mpatches.Patch(color=color_dict[category], label=category) for category in categories]
plt.legend(handles=legend_handles, title="Categories", bbox_to_anchor=(1, 1), loc="upper left")

plt.show()