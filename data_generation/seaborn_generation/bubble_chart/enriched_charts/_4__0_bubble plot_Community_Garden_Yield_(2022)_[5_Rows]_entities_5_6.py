
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a DataFrame from the given data
data = {
    'Country': ['China', 'India', 'United States', 'Indonesia', 'Pakistan', 'Brazil', 'Nigeria', 'Bangladesh', 'Russia', 'Mexico', 'Japan', 'Ethiopia', 'Philippines', 'Egypt', 'Vietnam', 'DR Congo', 'Turkey', 'Iran', 'Germany', 'Thailand'],
    'Population': [1400, 1366, 331, 273, 220, 213, 206, 166, 145, 128, 126, 115, 109, 102, 97, 89, 84, 83, 83, 70],
    'LifeExpectancy': [76.9, 69.7, 78.9, 71.7, 67.3, 75.9, 54.3, 72.6, 73.2, 75.4, 84.6, 66.7, 71.0, 72.0, 75.4, 61.6, 77.4, 76.2, 80.9, 77.2],
    'PopulationDensity': [150, 420, 36, 151, 286, 25, 226, 1265, 9, 66, 347, 115, 368, 102, 311, 40, 110, 52, 232, 137]
}
df = pd.DataFrame(data)

# Plot the bubble chart
plt.figure(figsize=(16, 10))
bubble_chart = sns.scatterplot(data=df, x='Population', y='LifeExpectancy', size='PopulationDensity', sizes=(20, 600), hue='Country', palette=['#E69F00', '#56B4E9', '#009E73', '#F0E442', '#0072B2', '#D55E00', '#CC79A7', '#8E44AD', '#2ECC71', '#E74C3C', '#3498DB', '#1ABC9C', '#F39C12', '#C0392B', '#7F8C8D', '#8E44AD', '#2980B9', '#27AE60', '#8E44AD', '#E74C3C'])

# Customizing the plot
plt.title('Population vs Life Expectancy by Country', fontsize=22, pad=20)
plt.xlabel('Population (in millions)', fontsize=16)
plt.ylabel('Life Expectancy (in years)', fontsize=16)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)

# Show the plot
plt.tight_layout()
plt.show()