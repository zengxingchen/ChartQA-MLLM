
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = {
    'Topic': ['Innovation', 'Marketing', 'Sales', 'Customer Service', 'Human Resources'],
    'ValueA': [15, 30, 25, 20, 35],
    'ValueB': [45, 35, 25, 40, 30],
    'ValueC': [40, 35, 50, 40, 35],
}

df = pd.DataFrame(data)

df_percentage = df.set_index('Topic')
df_percentage = df_percentage.divide(df_percentage.sum(axis=1), axis=0)

fig, ax = plt.subplots(figsize=(10, 8))
df_percentage.plot(kind='bar', stacked=True, color=['#FF5733', '#33FF57', '#3357FF'], ax=ax, width=0.8)

for n in df_percentage:
    for i, (cs, ab, pc) in enumerate(zip(df_percentage.iloc[:, :].cumsum(1)[n], 
                                          df_percentage[n], df_percentage[n])):
        if pc > 0:
            plt.text(i, cs - ab / 2, str(round(pc * 100, 1)) + '%', va='center', ha='center', fontsize=10)

plt.title('Business Department Contributions', pad=20)
ax.set_ylabel('Percentage')
ax.set_xlabel('Departments')
plt.legend(title='Contribution Types', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()