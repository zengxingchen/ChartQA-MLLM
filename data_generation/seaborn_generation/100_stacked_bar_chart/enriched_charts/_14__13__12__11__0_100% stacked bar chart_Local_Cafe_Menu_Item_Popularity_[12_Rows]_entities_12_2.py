
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = {
    'Category': ['Children', 'Teens', 'Adults', 'Seniors', 'Athletes', 'General Population'],
    'CO2 Emissions': [15, 20, 25, 15, 20, 25],
    'Renewable Energy Usage': [25, 20, 20, 30, 25, 30],
    'Water Conservation': [35, 30, 25, 30, 20, 20],
    'Recycling Rates': [25, 30, 30, 25, 35, 25],
}

df = pd.DataFrame(data)

df_percentage = df.set_index('Category')
df_percentage = df_percentage.divide(df_percentage.sum(axis=1), axis=0)

fig, ax = plt.subplots(figsize=(14, 10))
df_percentage.plot(kind='bar', stacked=True, color=['#FF5733', '#33FF57', '#3357FF', '#FF33A1'], ax=ax, width=0.7)

for n in df_percentage:
    for i, (cs, ab, pc) in enumerate(zip(df_percentage.iloc[:, :].cumsum(1)[n], 
                                          df_percentage[n], df_percentage[n])):
        if pc > 0:
            plt.text(i, cs - ab / 2, str(round(pc * 100, 1)) + '%', va='center', ha='center', fontsize=10)

plt.title('Environmental Awareness by Category', pad=20, fontsize=16)
ax.set_ylabel('Percentage')
ax.set_xlabel('Categories')
plt.legend(title='Environmental Aspects', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()