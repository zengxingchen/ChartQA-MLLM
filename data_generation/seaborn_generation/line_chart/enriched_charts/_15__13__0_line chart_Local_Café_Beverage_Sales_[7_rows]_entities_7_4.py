
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Year': list(range(2000, 2021)),
    'Revenue': [
        3.0, 3.1, 3.3, 3.5, 3.6, 3.9, 4.2,
        4.3, 4.5, 4.8, 5.0, 5.2, 5.4, 5.6,
        5.9, 6.1, 6.4, 6.5, 6.7, 7.0, 7.2
    ]
}

df = pd.DataFrame(data)

plt.figure(figsize=(12, 6))

line_chart = sns.lineplot(data=df, x='Year', y='Revenue', marker='o', color='#FF6347', linewidth=2)

for i in range(df.shape[0]):
    plt.text(x=df['Year'][i], y=df['Revenue'][i] + 0.1, s=f"{df['Revenue'][i]}", ha='center')

plt.title('Annual Revenue Growth in the Health & Wellness Industry', fontsize=16, pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Revenue (in Billion USD)', fontsize=14)

plt.show()