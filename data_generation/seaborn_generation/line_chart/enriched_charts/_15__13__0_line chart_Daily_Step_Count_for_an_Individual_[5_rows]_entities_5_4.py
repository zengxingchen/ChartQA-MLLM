
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Month': [i for i in range(1, 53)],
    'Average_Temperature': [
        30, 32, 35, 38, 40, 42, 44, 43, 41, 38, 35, 32, 30, 28, 27, 25, 23, 21, 
        20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 
        0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13
    ]
}

df = pd.DataFrame(data)

sns.set_theme(style="whitegrid")

plt.figure(figsize=(16, 8))
plot = sns.lineplot(x='Month', y='Average_Temperature', data=df, linewidth=2.5, color="#ff6347")

plt.annotate('Peak temperature', 
             xy=(7, df.loc[6, 'Average_Temperature']), 
             xycoords='data',
             xytext=(10, 45),
             textcoords='data',
             arrowprops=dict(arrowstyle="->",
                             connectionstyle="arc3"),
             )

plt.annotate('Lowest temperature', 
             xy=(52, df.loc[51, 'Average_Temperature']), 
             xycoords='data',
             xytext=(40, -15),
             textcoords='data',
             arrowprops=dict(arrowstyle="->",
                             connectionstyle="arc3"),
             )

plt.title('Monthly Average Temperature of City XYZ', pad=20)
plt.xlabel('Month')
plt.ylabel('Average Temperature (°C)')

plt.show()