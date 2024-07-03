
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Quarter': ['Q1 2023', 'Q2 2023', 'Q3 2023', 'Q4 2023', 'Q1 2024', 'Q2 2024',
                'Q3 2024', 'Q4 2024', 'Q1 2025', 'Q2 2025', 'Q3 2025', 'Q4 2025'],
    'Revenue': [20.5, 22.8, 25.1, 27.3, 29.7, 32.4, 35.6, 38.2, 40.9, 43.5, 46.2, 49.0]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 7))
chart = sns.lineplot(x='Quarter', y='Revenue', data=df, color="#1abc9c")

plt.fill_between(x=df['Quarter'], y1=df['Revenue'], color="#1abc9c", alpha=0.3)

for i in range(df.shape[0]):
    plt.text(df['Quarter'][i], df['Revenue'][i]+0.5, f"${df['Revenue'][i]}M", horizontalalignment='center')

plt.title('Quarterly Revenue Growth', fontsize=16)
plt.xlabel('Quarter')
plt.ylabel('Revenue (Million $)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()