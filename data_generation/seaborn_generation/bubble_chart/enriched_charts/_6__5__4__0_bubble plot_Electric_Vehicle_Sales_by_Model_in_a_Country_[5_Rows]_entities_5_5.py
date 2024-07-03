
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Country': ['United States', 'China', 'Germany', 'Norway', 'France', 'United Kingdom', 
                'Netherlands', 'Canada', 'Sweden', 'Italy', 'Japan', 'South Korea',
                'Australia', 'Brazil', 'India'],
    'Average Temperature (°C)': [13, 10, 9, 2, 11, 8, 7, 1, 3, 12, 15, 14, 22, 25, 28],
    'Books Published': [250000, 450000, 85000, 10000, 75000, 95000, 15000, 20000, 12000, 65000, 120000, 105000, 50000, 70000, 200000],
    'Reading Hours Per Week': [10.5, 8.2, 9.6, 12.1, 8.5, 9.4, 10.3, 11.0, 11.5, 8.8, 9.0, 8.7, 10.1, 7.2, 6.5],
    'Population (Millions)': [331, 1440, 83, 5, 65, 68, 17, 38, 10, 60, 126, 52, 26, 213, 1393]
}

df = pd.DataFrame(data)

plt.figure(figsize=(18, 14))
bubble_chart = sns.scatterplot(data=df, 
                               x='Average Temperature (°C)', 
                               y='Reading Hours Per Week', 
                               size='Books Published', 
                               hue='Country', 
                               palette=['#FF5733','#33FF57','#3357FF','#FF33A8','#A833FF','#33FFA2',
                                        '#FF8C33','#338FFF','#FF33C4','#C433FF','#33FFD7','#FF3380',
                                        '#8033FF','#FF5733','#3380FF'],
                               sizes=(100, 2500))

plt.title('Average Temperature vs Reading Hours and Books Published', fontsize=16, pad=20)
plt.xlabel('Average Temperature (°C)', fontsize=14)
plt.ylabel('Reading Hours Per Week', fontsize=14)

bubble_chart.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Country')

plt.show()