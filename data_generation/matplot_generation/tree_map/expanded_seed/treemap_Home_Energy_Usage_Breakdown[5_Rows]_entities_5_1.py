
import matplotlib.pyplot as plt
import squarify
import pandas as pd

# Given data
data = [
    {'Category': 'Electricity', 'Subcategory': 'Lighting', 'Monthly_kWh': 300},
    {'Category': 'Electricity', 'Subcategory': 'Heating and Cooling', 'Monthly_kWh': 800},
    {'Category': 'Gas', 'Subcategory': 'Water Heating', 'Monthly_kWh': 200},
    {'Category': 'Gas', 'Subcategory': 'Cooking', 'Monthly_kWh': 100},
    {'Category': 'Renewable', 'Subcategory': 'Solar Panels', 'Monthly_kWh': 150}
]

# Convert list of dictionaries to DataFrame for easier manipulation
df = pd.DataFrame(data)

# Create a color map based on Categories
cmap = plt.cm.coolwarm
mini, maxi = df['Category'].factorize()[0].min(), df['Category'].factorize()[0].max()
norm = plt.Normalize(mini, maxi)
colors = [cmap(norm(value)) for value in df['Category'].factorize()[0]]

# Prepare data for the treemap
sizes = df['Monthly_kWh'].values
labels = ["{}\n{} kWh".format(subcat, size) for subcat, size in zip(df['Subcategory'], sizes)]

# Create a treemap
plt.figure(figsize=(12, 8))
squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.8, text_kwargs={'fontsize':10})

# Remove axis for treemap
plt.axis('off')

# Add a colorbar
import matplotlib.patches as mpatches
categories = df['Category'].unique()
handles = [mpatches.Patch(color=cmap(norm(df[df['Category']==cat].index[0])), label=cat) for cat in categories]
plt.legend(handles=handles, title='Categories')

# Title of the treemap
plt.title('Monthly Energy Consumption by Subcategory')

# Show plot
plt.show()