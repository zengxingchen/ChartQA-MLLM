
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Provided chart table data
data = [
    {'Appliance': 2018, 'Lighting': '25%', 'Heating': '32%', 'Cooling': '17%', 'Electronics': '15%', 'Refrigeration': '7%', 'Other': '4%'},
    {'Appliance': 2019, 'Lighting': '24%', 'Heating': '30%', 'Cooling': '19%', 'Electronics': '16%', 'Refrigeration': '6%', 'Other': '5%'},
    {'Appliance': 2020, 'Lighting': '22%', 'Heating': '29%', 'Cooling': '21%', 'Electronics': '17%', 'Refrigeration': '6%', 'Other': '5%'}
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
df_long = df.melt(id_vars='Appliance', var_name='Category', value_name='Percentage')

# Sort categories for consistent stacking
df_long.sort_values(by=['Appliance', 'Category'], inplace=True)

# Set the color palette
colors = sns.color_palette('pastel', len(df_long['Category'].unique()))

# Start plotting
fig, ax = plt.subplots(figsize=(10, 6))

# Bottom value for stacking
bottom = pd.Series([0.0, 0.0, 0.0])

for index, (name, group) in enumerate(df_long.groupby('Category')):
    # Plotting each category
    sns.barplot(
        x='Appliance', y='Percentage', data=group, 
        label=name, color=colors[index], bottom=bottom
    )
    # Update bottom value for stacking
    bottom += group['Percentage'].values

# Customizing the plot
ax.set_ylim(0, 1)
ax.set_ylabel('Percentage')
ax.set_title('100% Stacked Bar Chart of Appliance Energy Usage')

# Display legend
plt.legend(title='Category', loc='upper left', bbox_to_anchor=(1, 1))

# Convert y-axis back to percentage
ax.yaxis.set_major_formatter(plt.FuncFormatter('{:.0%}'.format))

plt.tight_layout()
plt.show()