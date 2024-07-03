
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Your provided data
data = [
    {'Year': 2015, 'iPhone Model A': 800000, 'Samsung Galaxy S': 1200000, 'Samsung Galaxy Note': 400000, 'Google Pixel': 0, 'OnePlus': 0, 'Xiaomi': 0},
    {'Year': 2016, 'iPhone Model A': 1000000, 'Samsung Galaxy S': 1500000, 'Samsung Galaxy Note': 500000, 'Google Pixel': 200000, 'OnePlus': 0, 'Xiaomi': 0},
    # ... other data rows ...
    {'Year': 2026, 'iPhone Model A': 1520000, 'Samsung Galaxy S': 950000, 'Samsung Galaxy Note': 100000, 'Google Pixel': 750000, 'OnePlus': 650000, 'Xiaomi': 500000}
]

# Convert the list of dictionaries to a pandas DataFrame
df = pd.DataFrame(data)

# Set the index to 'Year' for easier plotting
df.set_index('Year', inplace=True)

# Plot the stacked area chart using Matplotlib and Seaborn styles
plt.figure(figsize=(12, 8))

# Use Seaborn's context and style for better visual appearance
sns.set_context('talk')
sns.set_style('whitegrid')

# Define a color palette using Seaborn
palette = sns.color_palette('husl', n_colors=len(df.columns))

# Matplotlib's `stackplot` function to create the stacked area chart
plt.stackplot(df.index, df.T, labels=df.columns, colors=palette, alpha=0.8)

# Add a legend, titles and labels
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.title('Smartphone Sales Over Years')
plt.xlabel('Year')
plt.ylabel('Number of Units Sold')

# Display the plot
plt.tight_layout()
plt.show()