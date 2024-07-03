
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Provided chart table data
data = [
    {'Year': 2018, 'Protein': 0.3, 'Fiber': 0.1, 'Vitamins': 0.25, 'Minerals': 0.2, 'Fat': 0.15},
    {'Year': 2019, 'Protein': 0.28, 'Fiber': 0.12, 'Vitamins': 0.27, 'Minerals': 0.18, 'Fat': 0.15},
    {'Year': 2020, 'Protein': 0.26, 'Fiber': 0.13, 'Vitamins': 0.3, 'Minerals': 0.16, 'Fat': 0.15},
    {'Year': 2021, 'Protein': 0.29, 'Fiber': 0.14, 'Vitamins': 0.28, 'Minerals': 0.17, 'Fat': 0.12},
    {'Year': 2022, 'Protein': 0.27, 'Fiber': 0.15, 'Vitamins': 0.26, 'Minerals': 0.19, 'Fat': 0.13}
]

# Convert to DataFrame
df = pd.DataFrame(data)

# Melt the DataFrame to long-form
df_long = df.melt(id_vars='Year', var_name='Nutrient', value_name='Percentage')

# Sort categories for consistent stacking
df_long.sort_values(by=['Year', 'Nutrient'], inplace=True)

# Set the color palette using specific color codes
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']

# Start plotting
fig, ax = plt.subplots(figsize=(12, 8))

# Bottom value for stacking
bottom = pd.Series([0.0] * df['Year'].nunique())

for index, (name, group) in enumerate(df_long.groupby('Nutrient')):
    sns.barplot(
        x='Year', y='Percentage', data=group, 
        label=name, color=colors[index], ci=None, edgecolor='black', linewidth=0.5
    )
    # Update bottom value for stacking
    bottom += group['Percentage'].values

# Customizing the plot
ax.set_ylim(0, 1)
ax.set_ylabel('Percentage')
ax.set_xlabel('Year')
ax.set_title('Distribution of Nutrients in Food by Year')

# Display legend
plt.legend(title='Nutrient', loc='upper left', bbox_to_anchor=(1, 1))

# Convert y-axis back to percentage
ax.yaxis.set_major_formatter(plt.FuncFormatter('{:.0%}'.format))

plt.tight_layout()
plt.show()