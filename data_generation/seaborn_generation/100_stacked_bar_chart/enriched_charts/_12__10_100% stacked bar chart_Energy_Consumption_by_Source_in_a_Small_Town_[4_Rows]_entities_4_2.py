
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Input data
data = [
    {'Year': 2019, 'Protein (%)': 30, 'Carbohydrates (%)': 50, 'Fats (%)': 10, 'Vitamins (%)': 5, 'Minerals (%)': 5},
    {'Year': 2020, 'Protein (%)': 32, 'Carbohydrates (%)': 48, 'Fats (%)': 11, 'Vitamins (%)': 6, 'Minerals (%)': 3},
    {'Year': 2021, 'Protein (%)': 33, 'Carbohydrates (%)': 47, 'Fats (%)': 10, 'Vitamins (%)': 6, 'Minerals (%)': 4},
    {'Year': 2022, 'Protein (%)': 31, 'Carbohydrates (%)': 46, 'Fats (%)': 12, 'Vitamins (%)': 7, 'Minerals (%)': 4},
    {'Year': 2023, 'Protein (%)': 29, 'Carbohydrates (%)': 49, 'Fats (%)': 11, 'Vitamins (%)': 6, 'Minerals (%)': 5}
]

# Create a DataFrame
df = pd.DataFrame(data)

# Set the index to 'Year'
df.set_index('Year', inplace=True)

# Normalize data to 100%
df_normalized = df.div(df.sum(axis=1), axis=0) * 100

# Define colors for each stack
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#A633FF']

# Setup seaborn style
sns.set_style('whitegrid')

# Plotting
plt.figure(figsize=(10, 8))

# Creating the bar stacks
bottom = None
bar_width = 0.6
for (columnName, columnData), color in zip(df_normalized.iteritems(), colors):
    plt.bar(df_normalized.index, columnData, bottom=bottom, color=color, label=columnName, edgecolor='white', width=bar_width)
    bottom = columnData if bottom is None else bottom + columnData

# Add legend
plt.legend(title="Nutrient Composition")

# Formatting the plot
plt.title('Nutrient Composition in Daily Diet Over the Years')
plt.xlabel('Year')
plt.ylabel('Nutrient Contribution (%)')
plt.yticks(range(0, 101, 10))
plt.xticks(df_normalized.index)
sns.despine()  # Remove the top and right spines

# Show the plot
plt.show()