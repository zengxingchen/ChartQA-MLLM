
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Year': list(range(2000, 2021)),
    'Happiness Score': [
        6.5, 6.4, 6.6, 6.7, 6.8, 6.9, 7.0,
        6.8, 6.7, 6.6, 6.8, 7.0, 7.1, 7.3,
        7.4, 7.5, 7.6, 7.8, 7.9, 8.0, 8.1
    ]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 8))

line_chart = sns.lineplot(data=df, x='Year', y='Happiness Score', marker='o', color='#FF6347', linewidth=2)

for i in range(df.shape[0]):
    plt.text(x=df['Year'][i], y=df['Happiness Score'][i] + 0.05, s=f"{df['Happiness Score'][i]}", ha='center')

plt.title('Annual Average Happiness Score', fontsize=18, pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Happiness Score', fontsize=14)

plt.show()