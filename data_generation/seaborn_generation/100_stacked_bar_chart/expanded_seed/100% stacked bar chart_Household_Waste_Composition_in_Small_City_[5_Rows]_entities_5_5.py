
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Your provided data
data = [
    {'Year': 2019, 'Organic': '40%', 'Plastic': '20%', 'Paper': '25%', 'Glass': '10%', 'Metals': '5%'},
    {'Year': 2020, 'Organic': '42%', 'Plastic': '18%', 'Paper': '24%', 'Glass': '9%', 'Metals': '7%'},
    {'Year': 2021, 'Organic': '39%', 'Plastic': '19%', 'Paper': '22%', 'Glass': '12%', 'Metals': '8%'},
    {'Year': 2022, 'Organic': '35%', 'Plastic': '22%', 'Paper': '20%', 'Glass': '15%', 'Metals': '8%'},
    {'Year': 2023, 'Organic': '38%', 'Plastic': '21%', 'Paper': '19%', 'Glass': '13%', 'Metals': '9%'}
]

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data)

# Convert percentage strings to numbers
for col in df.columns[1:]:
    df[col] = df[col].str.rstrip('%').astype('float') / 100

# Reshape the DataFrame from wide to long format
df_long = df.melt(id_vars='Year', var_name='Material', value_name='Percentage')

# Calculate the bottom position for each bar segment
df_long['Bottom'] = df_long.groupby('Year')['Percentage'].cumsum() - df_long['Percentage']

# Begin plotting
plt.figure(figsize=(10, 6))

# Create a color palette
palette = sns.color_palette("husl", len(df.columns) - 1)

# Plot each material
for i, material in enumerate(df.columns[1:]):
    sns.barplot(
        data=df_long[df_long['Material'] == material],
        x='Year',
        y='Percentage',
        color=palette[i],
        label=material,
        bottom=df_long[df_long['Material'] == material]['Bottom']
    )

# Additional plot formatting
plt.title('100% Stacked Bar Chart')
plt.ylabel('Percentage (%)')
plt.xlabel('Year')

# Move the legend outside the plot
plt.legend(title='Material', bbox_to_anchor=(1.05, 1), loc='upper left')

# Show the plot
plt.tight_layout()
plt.show()