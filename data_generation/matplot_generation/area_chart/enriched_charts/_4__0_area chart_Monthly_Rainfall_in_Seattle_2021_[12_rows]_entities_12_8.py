
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Day': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
            21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    'Visitors': [100, 120, 150, 140, 130, 160, 180, 170, 140, 120,
                 150, 160, 170, 190, 210, 220, 200, 180, 170, 160,
                 150, 170, 190, 210, 220, 240, 230, 210, 200, 190]
}
df = pd.DataFrame(data)

palette = sns.color_palette(["#e74c3c"])

plt.figure(figsize=(14, 8))

sns.lineplot(data=df, x='Day', y='Visitors', palette=palette)
plt.fill_between(data['Day'], data['Visitors'], color="#e74c3c", alpha=0.3)

max_visitors_day = df['Visitors'].idxmax() + 1
max_visitors = df['Visitors'].max()
plt.text(max_visitors_day, max_visitors + 5, f'Peak: {max_visitors}', horizontalalignment='center', color='black')

plt.title('Daily Visitor Count Over a Month')

plt.show()