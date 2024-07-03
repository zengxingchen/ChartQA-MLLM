
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = {
    'Category': ['Children', 'Teens', 'Adults', 'Seniors', 'Athletes', 'General Population'],
    'Physical Health': [25, 20, 30, 20, 15, 25],
    'Mental Health': [20, 25, 30, 25, 20, 25],
    'Nutrition': [30, 25, 20, 25, 30, 25],
    'Exercise': [25, 30, 20, 30, 35, 25],
}

df = pd.DataFrame(data)

df_percentage = df.set_index('Category')
df_percentage = df_percentage.divide(df_percentage.sum(axis=1), axis=0)

fig, ax = plt.subplots(figsize=(12, 9))
df_percentage.plot(kind='bar', stacked=True, color=['#E74C3C', '#8E44AD', '#3498DB', '#2ECC71'], ax=ax, width=0.8)

for n in df_percentage:
    for i, (cs, ab, pc) in enumerate(zip(df_percentage.iloc[:, :].cumsum(1)[n], 
                                          df_percentage[n], df_percentage[n])):
        if pc > 0:
            plt.text(i, cs - ab / 2, str(round(pc * 100, 1)) + '%', va='center', ha='center', fontsize=10)

plt.title('Health & Psychology Aspects by Category', pad=20)
ax.set_ylabel('Percentage')
ax.set_xlabel('Categories')
plt.legend(title='Health Aspects', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()