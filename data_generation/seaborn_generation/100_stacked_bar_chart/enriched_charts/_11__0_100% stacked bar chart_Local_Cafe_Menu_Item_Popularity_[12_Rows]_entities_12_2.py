
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = {
    'Category': ['Emissions', 'Recycling', 'Renewable Energy', 'Water Conservation', 'Waste Management'],
    'ValueA': [25, 30, 20, 35, 40],
    'ValueB': [35, 25, 40, 30, 20],
    'ValueC': [40, 45, 40, 35, 40],
}

df = pd.DataFrame(data)

df_percentage = df.set_index('Category')
df_percentage = df_percentage.divide(df_percentage.sum(axis=1), axis=0)

fig, ax = plt.subplots(figsize=(12, 6))
df_percentage.plot(kind='bar', stacked=True, color=['#FF6347', '#4682B4', '#3CB371'], ax=ax, width=0.6)

for n in df_percentage:
    for i, (cs, ab, pc) in enumerate(zip(df_percentage.iloc[:, :].cumsum(1)[n], 
                                          df_percentage[n], df_percentage[n])):
        if pc > 0:
            plt.text(i, cs - ab / 2, str(round(pc * 100, 1)) + '%', va='center', ha='center', fontsize=10)

plt.title('Environmental Impact Factors', pad=20)
ax.set_ylabel('Percentage')
ax.set_xlabel('Categories')
plt.legend(title='Impact Types', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()