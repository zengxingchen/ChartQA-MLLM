
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Provided data
data = [
    {'Year': 2019, 'Carbohydrates': '50%', 'Proteins': '20%', 'Fats': '15%', 'Fibers': '10%', 'Vitamins': '5%'},
    {'Year': 2020, 'Carbohydrates': '48%', 'Proteins': '22%', 'Fats': '15%', 'Fibers': '10%', 'Vitamins': '5%'},
    {'Year': 2021, 'Carbohydrates': '45%', 'Proteins': '25%', 'Fats': '15%', 'Fibers': '10%', 'Vitamins': '5%'},
    {'Year': 2022, 'Carbohydrates': '47%', 'Proteins': '23%', 'Fats': '15%', 'Fibers': '10%', 'Vitamins': '5%'},
    {'Year': 2023, 'Carbohydrates': '46%', 'Proteins': '24%', 'Fats': '15%', 'Fibers': '10%', 'Vitamins': '5%'}
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
colors = ['#FF7F50', '#87CEFA', '#DA70D6', '#32CD32', '#FFD700']

# Plot each nutrient
for i, nutrient in enumerate(df.columns[1:]):
    sns.barplot(
        data=df_long[df_long['Nutrient'] == nutrient],
        x='Year',
        y='Percentage',
        color=colors[i],
        label=nutrient,
        bottom=df_long[df_long['Nutrient'] == nutrient]['Bottom'],
        width=0.8
    )

# Additional plot formatting
plt.title('Distribution of Nutrients in Diets Over Years', fontsize=16)
plt.ylabel('Percentage (%)', fontsize=12)
plt.xlabel('Year', fontsize=12)

# Move the legend outside the plot
plt.legend(title='Nutrient', bbox_to_anchor=(1.05, 1), loc='upper left')

# Show the plot
plt.tight_layout()
plt.show()