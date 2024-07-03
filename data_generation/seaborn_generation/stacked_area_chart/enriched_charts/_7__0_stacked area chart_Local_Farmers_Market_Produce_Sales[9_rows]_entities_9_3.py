
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Preparing the data
data = {
    'Quarter': ['Q1-2021', 'Q2-2021', 'Q3-2021', 'Q4-2021', 'Q1-2022', 'Q2-2022', 'Q3-2022', 'Q4-2022', 'Q1-2023', 'Q2-2023', 'Q3-2023', 'Q4-2023'],
    'Industry_A': [45.23, 50.12, 48.34, 52.78, 47.56, 49.34, 51.45, 53.67, 50.12, 52.34, 54.78, 56.45],
    'Industry_B': [34.56, 36.45, 38.67, 40.23, 42.56, 44.23, 46.78, 48.34, 49.45, 50.67, 52.34, 54.12],
    'Industry_C': [50.34, 52.78, 55.21, 60.45, 58.34, 60.56, 62.23, 65.12, 63.56, 66.34, 68.23, 70.34]
}

df = pd.DataFrame(data)
df.set_index('Quarter', inplace=True)

# Calculate the cumulative CO2 emissions
cumulative_emissions = df.cumsum(axis=1)

# Set the plot size
plt.figure(figsize=(14, 7))

# Plotting the data
plt.stackplot(df.index, cumulative_emissions['Industry_A'],
              cumulative_emissions['Industry_B'],
              cumulative_emissions['Industry_C'],
              labels=['Industry A', 'Industry B', 'Industry C'],
              colors=['#4CAF50', '#FF9800', '#2196F3'], alpha=0.8)

# Adding the legend
plt.legend(loc='upper left')

# Annotating a specific point
plt.annotate('Peak Emission', xy=('Q4-2023', cumulative_emissions.loc['Q4-2023', 'Industry_C']),
             xytext=(-50, -30), textcoords='offset points', arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.5'))

# Adding title and labels
plt.title('Quarterly CO2 Emissions from Different Industries (in million tons)')
plt.xlabel('Quarter')
plt.ylabel('CO2 Emissions')

# Display the plot
plt.tight_layout()
plt.show()