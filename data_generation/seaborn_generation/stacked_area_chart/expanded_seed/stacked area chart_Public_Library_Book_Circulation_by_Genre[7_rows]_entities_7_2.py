
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = [
    {'Year': 2015, 'Fiction': 7500, 'Non-Fiction': 6200, 'Young Adult': 3900, "Children's": 9200, 'Reference': 2100, 'Graphic Novels': 1700},
    {'Year': 2016, 'Fiction': 7700, 'Non-Fiction': 6400, 'Young Adult': 4050, "Children's": 9300, 'Reference': 2000, 'Graphic Novels': 1800},
    {'Year': 2017, 'Fiction': 7900, 'Non-Fiction': 6600, 'Young Adult': 4200, "Children's": 9400, 'Reference': 1950, 'Graphic Novels': 1900},
    {'Year': 2018, 'Fiction': 8150, 'Non-Fiction': 6750, 'Young Adult': 4400, "Children's": 9500, 'Reference': 1850, 'Graphic Novels': 2000},
    {'Year': 2019, 'Fiction': 8300, 'Non-Fiction': 6900, 'Young Adult': 4600, "Children's": 9600, 'Reference': 1800, 'Graphic Novels': 2100},
    {'Year': 2020, 'Fiction': 8500, 'Non-Fiction': 7100, 'Young Adult': 4800, "Children's": 9750, 'Reference': 1750, 'Graphic Novels': 2200},
    {'Year': 2021, 'Fiction': 8700, 'Non-Fiction': 7300, 'Young Adult': 5000, "Children's": 9800, 'Reference': 1700, 'Graphic Novels': 2300}
]

# Create a dataframe
df = pd.DataFrame(data)

# Set Year as index
df.set_index('Year', inplace=True)

# Accumulate data for stacking
df_accumulated = df.cumsum(axis=1)

# Start the plot
sns.set(style="whitegrid")
plt.figure(figsize=(10, 7))

# List of categories (reversed for stacking purposes)
categories = df.columns[::-1]

# Plot each category
for i, category in enumerate(categories):
    sns.lineplot(data=df_accumulated, x=df_accumulated.index, y=category, label=category, sort=False)

# Fill the area between the lines
for i, category in enumerate(categories[:-1]):
    plt.fill_between(df_accumulated.index, df_accumulated[category], df_accumulated[categories[i + 1]], alpha=0.5)

# Optional: reverse legend order
handles, labels = plt.gca().get_legend_handles_labels()
plt.legend(reversed(handles), reversed(labels), title='Category', loc='upper left')

# Optional: add titles and labels
plt.title('Stacked Area Chart of Book Sales by Category')
plt.xlabel('Year')
plt.ylabel('Number of Books Sold')

# Show the plot
plt.tight_layout()
plt.show()