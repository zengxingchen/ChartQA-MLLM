
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = {
    'Category': ['Software', 'Hardware', 'Services', 'Consulting', 'Licensing'],
    'Revenues': [150, 100, 90, 70, 50],
    'Expenses': [70, 40, 30, 20, 10],
    'Profit': [80, 60, 60, 50, 40]
}
df = pd.DataFrame(data)

df_percentage = df.set_index('Category')
df_percentage = df_percentage.divide(df_percentage.sum(axis=1), axis=0)

fig, ax = plt.subplots(figsize=(8, 12))
df_percentage.plot(kind='bar', stacked=True, color=['#1f77b4', '#ff7f0e', '#2ca02c'], ax=ax, width=0.7)

for n in df_percentage:
    for i, (cs, ab, pc) in enumerate(zip(df_percentage.iloc[:, :].cumsum(1)[n], 
                                          df_percentage[n], df_percentage[n])):
        if pc > 0:
            plt.text(i, cs - ab / 2, str(round(pc * 100, 1)) + '%', va='center', ha='center')

plt.title('Financial Performance Breakdown', pad=20)
ax.set_ylabel('Percentage')
ax.set_xlabel('Business Categories')
plt.legend(title='Financial Metrics', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()