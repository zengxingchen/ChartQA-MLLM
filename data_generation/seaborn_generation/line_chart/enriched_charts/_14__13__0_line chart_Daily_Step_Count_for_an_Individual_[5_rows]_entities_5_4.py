
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Day': [i for i in range(1, 53)],
    'Temperature': [
        22, 23, 22, 21, 20, 19, 18, 17, 16, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 
        24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 
        24, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15
    ]
}

df = pd.DataFrame(data)

sns.set_theme(style="whitegrid")

plt.figure(figsize=(16, 8))
plot = sns.lineplot(x='Day', y='Temperature', data=df, linewidth=2.5, color="#ff6347")

plt.annotate('Highest temperature', 
             xy=(20, df.loc[19, 'Temperature']), 
             xycoords='data',
             xytext=(10, 30),
             textcoords='data',
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))

plt.annotate('Lowest temperature', 
             xy=(31, df.loc[30, 'Temperature']), 
             xycoords='data',
             xytext=(40, 10),
             textcoords='data',
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))

plt.title('Daily Temperature Variation Over 52 Days')
plt.xlabel('Day')
plt.ylabel('Temperature (°C)')

plt.show()