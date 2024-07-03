
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'City': ['New York', 'Los Angeles', 'Tokyo', 'London', 'Paris', 'Beijing', 'Sydney', 'Cape Town', 'Mumbai', 'Mexico City'],
    'Jan': [-1, 14, 5, 4, 3, -4, 22, 20, 25, 15],
    'Feb': [0, 15, 6, 4, 4, 0, 22, 20, 25, 16],
    'Mar': [5, 16, 9, 7, 8, 5, 21, 19, 27, 19],
    'Apr': [11, 17, 14, 9, 10, 14, 19, 17, 29, 20],
    'May': [17, 18, 19, 13, 15, 20, 16, 15, 30, 22],
    'Jun': [22, 20, 22, 16, 18, 24, 14, 13, 29, 19],
    'Jul': [25, 22, 25, 18, 20, 26, 13, 13, 29, 18],
    'Aug': [24, 22, 27, 18, 20, 24, 15, 14, 28, 18],
    'Sep': [20, 21, 23, 15, 16, 20, 17, 15, 28, 18],
    'Oct': [14, 19, 18, 11, 11, 13, 19, 17, 29, 17],
    'Nov': [8, 16, 12, 7, 7, 5, 20, 18, 27, 16],
    'Dec': [2, 14, 8, 5, 4, -2, 22, 19, 26, 15]
}

df = pd.DataFrame(data)

# Melting the dataset to have cities, months, and values in separate columns
df_melted = df.melt(id_vars=['City'], var_name='Month', value_name='AvgTempCelsius')

# Seaborn plot
plt.figure(figsize=(10, 8))

# Horizontal bar chart with customized colors and bar width
ax = sns.barplot(
    data=df_melted,
    y='City',
    x='AvgTempCelsius',
    hue='Month',
    palette=['#FF5733', '#FFC300', '#FFFF33', '#33FF57', '#3366FF',
             '#6633FF', '#CC33FF', '#FF33CC', '#FF335E', '#33FFFF',
             '#33FFCC', '#FF8833'],
    dodge=False
)

ax.bar_label(ax.containers[0], padding=3)
plt.xlabel('Average Temperature (°C)')
plt.ylabel('City')
plt.title('Average Monthly Temperature of World Cities')
plt.legend(title='Month', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.show()