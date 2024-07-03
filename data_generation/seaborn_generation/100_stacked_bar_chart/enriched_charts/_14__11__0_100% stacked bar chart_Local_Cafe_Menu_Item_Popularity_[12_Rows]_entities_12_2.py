
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = {
    'Category': ['Sleep Quality', 'Physical Activity', 'Diet Quality', 'Social Interaction', 'Work-Life Balance'],
    'Anxiety': [30, 35, 20, 40, 25],
    'Depression': [25, 40, 30, 35, 30],
    'Stress': [45, 25, 50, 25, 45],
}

df = pd.DataFrame(data)

df_percentage = df.set_index('Category')
df_percentage = df_percentage.divide(df_percentage.sum(axis=1), axis=0)

fig, ax = plt.subplots(figsize=(10, 8))
df_percentage.plot(kind='bar', stacked=True, color=['#FFA07A', '#6495ED', '#90EE90'], ax=ax, width=0.7)

for n in df_percentage:
    for i, (cs, ab, pc) in enumerate(zip(df_percentage.iloc[:, :].cumsum(1)[n], 
                                          df_percentage[n], df_percentage[n])):
        if pc > 0:
            plt.text(i, cs - ab / 2, str(round(pc * 100, 1)) + '%', va='center', ha='center', fontsize=10)

plt.title('Impact of Various Factors on Mental Health', pad=20)
ax.set_ylabel('Percentage')
ax.set_xlabel('Factors')
plt.legend(title='Mental Health Indicators', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()