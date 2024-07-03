import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = {
    'Topic': ['Topic1', 'Topic2', 'Topic3', 'Topic4', 'Topic5', 'Topic6'],
    'ValueX': [50, 40, 35, 45, 30, 25],
    'ValueY': [20, 35, 25, 30, 40, 50],
    'ValueZ': [30, 25, 40, 25, 30, 25],
}
df = pd.DataFrame(data)

df_percentage = df.set_index('Topic')
df_percentage = df_percentage.divide(df_percentage.sum(axis=1), axis=0)

fig, ax = plt.subplots(figsize=(8, 10))
df_percentage.plot(kind='bar', stacked=True, color=['#1E88E5', '#D81B60', '#FFC107'], ax=ax, width=0.7)

for n in df_percentage:
    for i, (cs, ab, pc) in enumerate(zip(df_percentage.iloc[:, :].cumsum(1)[n], 
                                          df_percentage[n], df_percentage[n])):
        if pc > 0:
            plt.text(i, cs - ab / 2, str(round(pc * 100, 1)) + '%', va='center', ha='center')

plt.title('Diverse Topics Percentage Stacked Bar Chart', y=1.05)
ax.set_ylabel('Percentage')
ax.set_xlabel('Topics')
plt.legend(title='Values', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()