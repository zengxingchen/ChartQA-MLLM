
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Year': list(range(2000, 2021)),
    'Vegetable Consumption (kg per person)': [
        80, 85, 83, 87, 90, 88, 92,
        95, 97, 100, 105, 108, 110,
        112, 115, 118, 120, 123, 125, 127, 130
    ]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 7))

line_chart = sns.lineplot(data=df, x='Year', y='Vegetable Consumption (kg per person)', marker='o', color='#1E90FF', linewidth=2)

for i in range(df.shape[0]):
    plt.text(x=df['Year'][i], y=df['Vegetable Consumption (kg per person)'][i] + 0.5, s=f"{df['Vegetable Consumption (kg per person)'][i]}", ha='center')

plt.title('Annual Average Vegetable Consumption', fontsize=18, pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Vegetable Consumption (kg per person)', fontsize=14)

plt.show()