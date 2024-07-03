
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = pd.DataFrame({
    'Country': ['United States', 'China', 'Japan', 'Germany', 'India',
                'United Kingdom', 'France', 'Brazil', 'Canada', 'Russia',
                'Australia', 'South Korea', 'Italy', 'Mexico', 'Spain'],
    'GDP_Billion': [21430, 14340, 5080, 3860, 2870, 2830, 2720, 1840, 1730, 1700, 1390, 1630, 2000, 1220, 1390],
    'Expenditure_Per_Capita': [12000, 3000, 6000, 7000, 1500, 8000, 7500, 2500, 9000, 4000, 11000, 8000, 7000, 2000, 7000],
    'Healthcare_Percentage': [16.8, 6.6, 10.9, 11.2, 3.6, 10.0, 11.1, 9.1, 10.4, 5.3, 9.3, 7.6, 8.8, 6.1, 8.5],
    'Population_Millions': [331, 1441, 126, 83, 1380, 68, 65, 213, 38, 146, 25, 52, 60, 129, 47]
})

data['Healthcare_Expenditure_Per_Capita'] = data['GDP_Billion'] * data['Healthcare_Percentage'] * 1e9 / (data['Population_Millions'] * 1e6)
data['Healthcare_Ratio'] = data['Healthcare_Expenditure_Per_Capita'] / data['Expenditure_Per_Capita']

sns.set(style='whitegrid')

plt.figure(figsize=(18, 14))
bubble = sns.scatterplot(data=data, x='GDP_Billion', y='Expenditure_Per_Capita',
                         size='Healthcare_Ratio', hue='Healthcare_Ratio',
                         palette=['#1f77b4','#ff7f0e','#2ca02c','#d62728'],
                         legend='brief', alpha=0.7, sizes=(20, 2000))

plt.xlabel('GDP in Billions of USD')
plt.ylabel('Healthcare Expenditure Per Capita (USD)')
plt.title('Healthcare Spending vs GDP in Selected Countries', pad=20)
plt.legend(loc='upper left', title='Healthcare Ratio')

plt.show()