
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Day': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
            16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    'AverageTemperature': [16, 17, 19, 21, 25, 23, 29, 30, 28, 26,
                           25, 28, 24, 22, 20, 18, 17, 15, 14, 12,
                           16, 19, 21, 22, 24, 27, 29, 31, 32, 30],
    'MWh': [4.2, 4.5, 5, 5.4, 6, 5.6, 6.5, 6.8, 6.2, 6, 5.9, 6.1,
            5.5, 5.2, 4.9, 4.6, 4.4, 4.1, 4.0, 3.8, 4.3, 5.1, 5.3,
            5.4, 5.7, 6.3, 6.7, 7.0, 7.2, 6.9]
}

df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(12, 6))
scatterplot = sns.scatterplot(x='AverageTemperature', y='MWh',
                              data=df, palette=['#FF6347', '#4682B4'])

scatterplot.set_title('Relationship Between Temperature and Electricity Consumption')
scatterplot.set_xlabel('Average Daily Temperature (°C)')
scatterplot.set_ylabel('Electricity Consumption (MWh)')

plt.show()