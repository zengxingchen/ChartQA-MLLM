
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = {
    'Topic': ['Diet', 'Exercise', 'Sleep'],
    'Cardiovascular Health': [25, 40, 35],
    'Mental Well-being': [35, 30, 35],
    'Physical Fitness': [30, 50, 20],
    'Weight Management': [20, 30, 50],
    'Immunity': [40, 35, 25],
}

df = pd.DataFrame(data)

df_percentage = df.set_index('Topic')
df_percentage = df_percentage.divide(df_percentage.sum(axis=1), axis=0)

fig, ax = plt.subplots(figsize=(12, 6))
df_percentage.plot(kind='bar', stacked=True, color=['#8B0000', '#FFD700', '#008000', '#00CED1', '#4B0082'], ax=ax, width=0.7)

for n in df_percentage:
    for i, (cs, ab, pc) in enumerate(zip(df_percentage.iloc[:, :].cumsum(1)[n], 
                                          df_percentage[n], df_percentage[n])):
        if pc > 0:
            plt.text(i, cs - ab / 2, str(round(pc * 100, 1)) + '%', va='center', ha='center', fontsize=10)

plt.title('Health & Psychology Contributions', pad=20)
ax.set_ylabel('Percentage')
ax.set_xlabel('Health Factors')
plt.legend(title='Health Contributions', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()