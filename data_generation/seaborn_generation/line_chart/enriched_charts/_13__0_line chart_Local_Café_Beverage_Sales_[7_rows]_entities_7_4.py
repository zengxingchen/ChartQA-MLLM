
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Year': list(range(2000, 2021)),
    'Revenue': [
        2.5, 2.7, 2.8, 3.0, 3.1, 3.5, 3.7,
        4.0, 4.2, 4.5, 4.7, 4.8, 5.0, 5.3,
        5.6, 5.8, 6.0, 6.2, 6.4, 6.7, 7.0
    ]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 7))

line_chart = sns.lineplot(data=df, x='Year', y='Revenue', marker='o', color='#1E90FF', linewidth=2)

for i in range(df.shape[0]):
    plt.text(x=df['Year'][i], y=df['Revenue'][i] + 0.1, s=f"{df['Revenue'][i]}", ha='center')

plt.title('Annual Revenue Growth in the Tech Industry', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Revenue (in Billion USD)', fontsize=14)

plt.show()