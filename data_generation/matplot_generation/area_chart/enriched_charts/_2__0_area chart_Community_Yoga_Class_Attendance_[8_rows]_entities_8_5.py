
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = {
    'Year': [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
    'Revenue': [150, 200, 250, 300, 350, 400, 450, 500, 550, 600]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 7))
sns.set(style="whitegrid")

colors = ["#e74c3c"]

area_plot = sns.lineplot(data=df, x='Year', y='Revenue', color=colors[0])
area_plot.fill_between(df['Year'], df['Revenue'], alpha=0.3, color=colors[0])

for index, row in df.iterrows():
    plt.text(row['Year'], row['Revenue'] + 5, round(row['Revenue'], 2), 
             color='black', ha="center")

plt.title('Annual Revenue Growth of ABC Corp (2015-2024)', fontsize=16, pad=20)
plt.xlabel('Year')
plt.ylabel('Revenue (in Million $)')

plt.show()