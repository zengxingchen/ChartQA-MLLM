
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Country': ['China', 'India', 'United States', 'Indonesia', 'Pakistan', 'Brazil', 'Nigeria', 'Bangladesh', 'Russia', 'Mexico', 'Japan', 'Ethiopia', 'Philippines', 'Egypt', 'Vietnam', 'DR Congo', 'Turkey', 'Iran', 'Germany', 'Thailand'],
    'Population': [1400, 1366, 331, 273, 220, 213, 206, 166, 145, 128, 126, 115, 109, 102, 97, 89, 84, 83, 83, 70],
    'MentalHealthIndex': [60, 45, 80, 55, 40, 65, 30, 50, 70, 58, 85, 35, 50, 42, 60, 25, 65, 60, 75, 70],
    'HealthcareSpending': [6.4, 3.1, 16.9, 3.0, 2.8, 9.5, 3.5, 2.4, 5.6, 6.3, 10.2, 1.9, 4.0, 3.0, 6.0, 1.2, 6.1, 6.5, 11.3, 4.8],
    'PopulationDensity': [150, 420, 36, 151, 286, 25, 226, 1265, 9, 66, 347, 115, 368, 102, 311, 40, 110, 52, 232, 137]
}

df = pd.DataFrame(data)

plt.figure(figsize=(18, 12))
bubble_chart = sns.scatterplot(data=df, x='Population', y='MentalHealthIndex', size='PopulationDensity', sizes=(20, 600), hue='Country', palette=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#9edae5', '#ffbb78', '#98df8a', '#ff9896', '#c5b0d5', '#c49c94', '#f7b6d2', '#c7c7c7', '#dbdb8d', '#c49c94'])

plt.title('Population vs Mental Health Index by Country', fontsize=22, pad=20)
plt.xlabel('Population (in millions)', fontsize=16)
plt.ylabel('Mental Health Index', fontsize=16)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)

plt.tight_layout()
plt.show()