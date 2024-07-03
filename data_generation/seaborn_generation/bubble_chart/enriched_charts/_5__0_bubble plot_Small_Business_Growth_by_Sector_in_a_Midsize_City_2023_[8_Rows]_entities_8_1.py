
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Country': ['United States', 'China', 'Japan', 'Germany', 'India', 'United Kingdom',
                'France', 'Brazil', 'Italy', 'Canada', 'Russia', 'South Korea', 
                'Spain', 'Australia', 'Mexico', 'Indonesia', 'Netherlands', 
                'Saudi Arabia', 'Turkey', 'Switzerland', 'Norway', 'Sweden', 'Denmark'],
    'GDP per Capita (USD)': [62589, 10410, 40200, 46445, 2170, 42230,
                             41465, 8898, 35220, 46214, 11290, 31846, 
                             29760, 55434, 10044, 4240, 52249, 23670, 
                             9125, 83780, 75234, 55134, 60834],
    'Life Expectancy (Years)': [78.86, 76.91, 84.55, 81.18, 69.73, 81.40,
                                82.66, 75.88, 84.01, 82.30, 72.41, 83.30, 
                                83.56, 83.44, 75.07, 71.72, 82.28, 75.13, 
                                77.69, 83.78, 82.30, 82.82, 81.5],
    'Population (Millions)': [331, 1438, 126, 83, 1367, 66,
                              65, 213, 60, 38, 145, 51,
                              47, 25, 128, 273, 17,
                              34, 84, 8, 5, 10, 6]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 12))
bubble_chart = sns.scatterplot(data=df,
                               x='GDP per Capita (USD)',
                               y='Life Expectancy (Years)',
                               size='Population (Millions)',
                               hue='GDP per Capita (USD)',
                               palette=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'],
                               sizes=(50, 1000),
                               alpha=0.8)

plt.title('Economic and Health Metrics of Various Countries', pad=20)
plt.xlabel('GDP per Capita (USD)')
plt.ylabel('Life Expectancy (Years)')
plt.legend(loc='upper right', title='Population (Millions)')

plt.show()