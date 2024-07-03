
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data preparation
data = {
    'Day': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
    'AverageTemperature': [22, 24, 28, 30, 21, 26, 27, 25, 31, 32, 20, 29, 19, 23, 24],
    'IceCreamSales': [100, 150, 200, 220, 90, 180, 190, 160, 230, 240, 80, 210, 70, 130, 150]
}

df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(10, 6))
scatterplot = sns.scatterplot(x='AverageTemperature', y='IceCreamSales', data=df, color='#FF6347')

# Add a title and adjust aesthetics
scatterplot.set_title('Ice Cream Sales vs Temperature', fontsize=16)
scatterplot.set_xlabel('Average Temperature (°C)', fontsize=12)
scatterplot.set_ylabel('Ice Cream Sales (units)', fontsize=12)

plt.show()