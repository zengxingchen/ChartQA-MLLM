
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Country': ['United States', 'China', 'Germany', 'Norway', 'France', 'United Kingdom', 
                'Netherlands', 'Canada', 'Sweden', 'Italy', 'Japan', 'South Korea',
                'Australia', 'Brazil', 'India'],
    'Average Temperature (°C)': [13, 10, 9, 2, 11, 8, 7, 1, 3, 12, 15, 14, 22, 25, 28],
    'Green Energy Production (GWh)': [1000, 2500, 600, 400, 700, 500, 450, 900, 300, 550, 800, 650, 1200, 1100, 1800],
    'Happiness Index': [7.0, 5.8, 6.5, 7.6, 6.8, 6.7, 6.9, 7.2, 7.5, 6.6, 5.9, 6.2, 7.1, 6.3, 4.9],
    'Population (Millions)': [331, 1440, 83, 5, 65, 68, 17, 38, 10, 60, 126, 52, 26, 213, 1393]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 12))
bubble_chart = sns.scatterplot(data=df, 
                               x='Average Temperature (°C)', 
                               y='Happiness Index', 
                               size='Green Energy Production (GWh)', 
                               hue='Country', 
                               palette=['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6',
                                        '#c2f0c2','#ff6666','#c2d1f0','#666699','#ff8c66','#999966',
                                        '#66ff66','#ffb366','#ff3399'],
                               sizes=(100, 2000))

plt.title('Average Temperature vs Happiness and Green Energy Production', fontsize=16, pad=20)
plt.xlabel('Average Temperature (°C)', fontsize=14)
plt.ylabel('Happiness Index', fontsize=14)

bubble_chart.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Country')

plt.show()