
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Category': ['2020 Q1', '2020 Q2', '2020 Q3', '2020 Q4', '2021 Q1', '2021 Q2', '2021 Q3', '2021 Q4', '2022 Q1', '2022 Q2', '2022 Q3', '2022 Q4'],
    'Value A': [10, 15, 20, 10, 25, 30, 20, 25, 35, 30, 25, 20],
    'Value B': [30, 25, 35, 25, 20, 25, 30, 20, 20, 25, 30, 35],
    'Value C': [25, 30, 25, 35, 30, 25, 35, 30, 25, 30, 20, 25],
    'Value D': [35, 30, 20, 30, 25, 20, 15, 25, 20, 15, 25, 20]
}

df = pd.DataFrame(data)
df.set_index('Category', inplace=True)
df_percent = df.div(df.sum(axis=1), axis=0) * 100

fig, ax = plt.subplots(figsize=(12, 8))
df_percent.plot(kind='bar', stacked=True, width=0.8, ax=ax, color=['#3366CC', '#DC3912', '#FF9900', '#109618'])

ax.set_title('Quarterly Distribution of Health Metrics Over Years', pad=20)
ax.set_ylabel('Percentage')
ax.set_xlabel('Category')
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=4)

plt.tight_layout()
plt.show()