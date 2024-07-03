
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Provided chart table data
data = [
    {'Year': 2018, 'Cardiovascular': 0.25, 'Diabetes': 0.15, 'Cancer': 0.3, 'Respiratory': 0.1, 'Other': 0.2},
    {'Year': 2019, 'Cardiovascular': 0.2, 'Diabetes': 0.17, 'Cancer': 0.32, 'Respiratory': 0.12, 'Other': 0.19},
    {'Year': 2020, 'Cardiovascular': 0.18, 'Diabetes': 0.19, 'Cancer': 0.28, 'Respiratory': 0.15, 'Other': 0.2},
    {'Year': 2021, 'Cardiovascular': 0.22, 'Diabetes': 0.16, 'Cancer': 0.26, 'Respiratory': 0.14, 'Other': 0.22}
]

# Convert to DataFrame
df = pd.DataFrame(data)

# Melt the DataFrame to long-form
df_long = df.melt(id_vars='Year', var_name='Disease', value_name='Percentage')

# Sort categories for consistent stacking
df_long.sort_values(by=['Year', 'Disease'], inplace=True)

# Set the color palette using specific color codes
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']

# Start plotting
fig, ax = plt.subplots(figsize=(10, 6))

# Bottom value for stacking
bottom = pd.Series([0.0] * df['Year'].nunique())

for index, (name, group) in enumerate(df_long.groupby('Disease')):
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
ax.set_title('Distribution of Common Diseases by Year')

# Display legend
plt.legend(title='Disease', loc='upper left', bbox_to_anchor=(1, 1))

# Convert y-axis back to percentage
ax.yaxis.set_major_formatter(plt.FuncFormatter('{:.0%}'.format))

plt.tight_layout()
plt.show()