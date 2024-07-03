
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Your provided data
data = [
    {'Year': 2019, 'Carbohydrates': '45%', 'Proteins': '20%', 'Fats': '25%', 'Fibers': '7%', 'Vitamins': '3%'},
    {'Year': 2020, 'Carbohydrates': '48%', 'Proteins': '18%', 'Fats': '22%', 'Fibers': '8%', 'Vitamins': '4%'},
    {'Year': 2021, 'Carbohydrates': '47%', 'Proteins': '21%', 'Fats': '23%', 'Fibers': '6%', 'Vitamins': '3%'},
    {'Year': 2022, 'Carbohydrates': '46%', 'Proteins': '19%', 'Fats': '24%', 'Fibers': '8%', 'Vitamins': '3%'},
    {'Year': 2023, 'Carbohydrates': '50%', 'Proteins': '20%', 'Fats': '20%', 'Fibers': '6%', 'Vitamins': '4%'}
]

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data)

# Convert percentage strings to numbers
for col in df.columns[1:]:
    df[col] = df[col].str.rstrip('%').astype('float') / 100

# Reshape the DataFrame from wide to long format
df_long = df.melt(id_vars='Year', var_name='Nutrient', value_name='Percentage')

# Calculate the bottom position for each bar segment
df_long['Bottom'] = df_long.groupby('Year')['Percentage'].cumsum() - df_long['Percentage']

# Begin plotting
plt.figure(figsize=(12, 8))

# Create a color palette
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#FF8C33']

# Plot each nutrient
for i, nutrient in enumerate(df.columns[1:]):
    sns.barplot(
        data=df_long[df_long['Nutrient'] == nutrient],
        x='Year',
        y='Percentage',
        color=colors[i],
        label=nutrient,
        bottom=df_long[df_long['Nutrient'] == nutrient]['Bottom'],
        width=0.75
    )

# Additional plot formatting
plt.title('Nutrient Composition in Diet Over Years')
plt.ylabel('Percentage (%)')
plt.xlabel('Year')

# Move the legend outside the plot
plt.legend(title='Nutrient', bbox_to_anchor=(1.05, 1), loc='upper left')

# Show the plot
plt.tight_layout()
plt.show()