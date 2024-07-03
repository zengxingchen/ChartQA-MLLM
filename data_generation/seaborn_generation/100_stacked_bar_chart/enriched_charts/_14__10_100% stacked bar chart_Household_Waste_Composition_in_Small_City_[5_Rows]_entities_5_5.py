
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Your provided data
data = [
    {'Year': 2019, 'Carbohydrates': '50%', 'Proteins': '20%', 'Fats': '18%', 'Fibers': '8%', 'Vitamins': '4%'},
    {'Year': 2020, 'Carbohydrates': '52%', 'Proteins': '18%', 'Fats': '17%', 'Fibers': '8%', 'Vitamins': '5%'},
    {'Year': 2021, 'Carbohydrates': '49%', 'Proteins': '21%', 'Fats': '19%', 'Fibers': '7%', 'Vitamins': '4%'},
    {'Year': 2022, 'Carbohydrates': '51%', 'Proteins': '19%', 'Fats': '18%', 'Fibers': '9%', 'Vitamins': '3%'},
    {'Year': 2023, 'Carbohydrates': '53%', 'Proteins': '20%', 'Fats': '17%', 'Fibers': '7%', 'Vitamins': '3%'}
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
plt.figure(figsize=(10, 6))

# Create a color palette
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Plot each nutrient
for i, nutrient in enumerate(df.columns[1:]):
    sns.barplot(
        data=df_long[df_long['Nutrient'] == nutrient],
        x='Year',
        y='Percentage',
        color=colors[i],
        label=nutrient,
        bottom=df_long[df_long['Nutrient'] == nutrient]['Bottom'],
        width=0.6
    )

# Additional plot formatting
plt.title('Nutrient Composition in Athlete Diets Over Years', pad=20)
plt.ylabel('Percentage (%)')
plt.xlabel('Year')

# Move the legend outside the plot
plt.legend(title='Nutrient', bbox_to_anchor=(1.05, 1), loc='upper left')

# Show the plot
plt.tight_layout()
plt.show()