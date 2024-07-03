
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Provided chart table data
data = [
    {'Year': 2018, 'Transportation': '28%', 'Industry': '25%', 'Residential': '15%', 'Commercial': '18%', 'Agriculture': '14%'},
    {'Year': 2019, 'Transportation': '27%', 'Industry': '26%', 'Residential': '16%', 'Commercial': '19%', 'Agriculture': '12%'},
    {'Year': 2020, 'Transportation': '26%', 'Industry': '24%', 'Residential': '18%', 'Commercial': '20%', 'Agriculture': '12%'}
]

# Convert to DataFrame 
df = pd.DataFrame(data)

# Function to convert percentage to float
def percent_to_float(s):
    return float(s.strip('%')) / 100

# Apply the function to each percentage column
for col in df.columns[1:]:
    df[col] = df[col].apply(percent_to_float)

# Melt the DataFrame to long-form
df_long = df.melt(id_vars='Year', var_name='Sector', value_name='Percentage')

# Sort categories for consistent stacking
df_long.sort_values(by=['Year', 'Sector'], inplace=True)

# Set the color palette using specific color codes
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Start plotting
fig, ax = plt.subplots(figsize=(12, 8))

# Bottom value for stacking
bottom = pd.Series([0.0, 0.0, 0.0])

for index, (name, group) in enumerate(df_long.groupby('Sector')):
    # Plotting each category
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
ax.set_title('100% Stacked Bar Chart of Energy Consumption by Sector')

# Display legend
plt.legend(title='Sector', loc='upper left', bbox_to_anchor=(1, 1))

# Convert y-axis back to percentage
ax.yaxis.set_major_formatter(plt.FuncFormatter('{:.0%}'.format))

plt.tight_layout()
plt.show()