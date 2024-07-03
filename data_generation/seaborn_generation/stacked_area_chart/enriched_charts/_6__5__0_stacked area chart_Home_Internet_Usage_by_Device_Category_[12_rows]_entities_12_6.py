
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Define the dataset
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Carbon Emissions': [200, 220, 210, 230, 240, 250, 260, 270, 280, 290, 300, 310],
    'Renewable Energy Usage': [100, 105, 110, 115, 120, 130, 140, 150, 160, 170, 180, 190],
    'Electric Vehicle Adoption': [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Data preparation for stacked area chart
df_melted = df.melt('Month', var_name='Category', value_name='Value')

# Transformation of 'Month' to categorical type for proper ordering
df_melted['Month'] = pd.Categorical(df_melted['Month'],
                                    categories=data['Month'],
                                    ordered=True)

# Plotting
plt.figure(figsize=(16, 9))

# Carbon Emissions: #8B0000 (Dark Red), Renewable Energy Usage: #228B22 (Forest Green), Electric Vehicle Adoption: #1E90FF (Dodger Blue)
colors = ["#8B0000", "#228B22", "#1E90FF"]

# Stackplot
plt.stackplot(df['Month'], df.iloc[:, 1:].values.T, labels=df.columns[1:], colors=colors, alpha=0.8)

# Beautifying the plot
plt.title('Trends in Environmental Metrics for 2023', fontsize=18)
plt.ylabel('Values', fontsize=14)
plt.xlabel('Month', fontsize=14)
plt.xticks(rotation=45)
plt.legend(title='Category', loc='upper left')

# Annotation
for i, row in df.iterrows():
    total_value = row['Carbon Emissions'] + row['Renewable Energy Usage'] + row['Electric Vehicle Adoption']
    plt.text(row['Month'], total_value, f'{total_value}', ha='center', va='bottom')

sns.despine()

# Show the plot
plt.tight_layout()
plt.show()