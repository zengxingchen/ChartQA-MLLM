
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Given data
data = [
    {'Year': 2019, 'Espresso': 12000, 'Americano': 14500, 'Cappuccino': 17000, 'Latte': 18500, 'Mocha': 16000},
    {'Year': 2020, 'Espresso': 11500, 'Americano': 14000, 'Cappuccino': 16500, 'Latte': 18000, 'Mocha': 15500},
    {'Year': 2021, 'Espresso': 13000, 'Americano': 15500, 'Cappuccino': 18000, 'Latte': 19500, 'Mocha': 17500},
    {'Year': 2022, 'Espresso': 13500, 'Americano': 16000, 'Cappuccino': 18500, 'Latte': 20000, 'Mocha': 18000}
]

# Convert to DataFrame
df = pd.DataFrame(data)

# Pivot data for stacked area chart
df = df.set_index('Year')

# Apply Seaborn style
sns.set_theme(style="whitegrid")

# Create a color palette
palette = sns.color_palette("husl", 5)  # You can change the color palette if needed

# Stacking values for area chart
df_cum = df.cumsum(axis=1)

fig, ax = plt.subplots(figsize=(10, 6))

# Adding each layer of the stacked area chart
for i in range(len(df.columns) - 1, -1, -1):
    plt.fill_between(df_cum.index, df_cum.iloc[:,i], label=df.columns[i], color=palette[i], alpha=0.8)

# Adding the legend, title and labels
plt.legend(loc='upper left')
plt.title('Coffee Sales Over Years')
plt.xlabel('Year')
plt.ylabel('Sales')

# Display the plot
plt.show()