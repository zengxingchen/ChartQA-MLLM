
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Year': [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021],
    'Productivity Index': [75, 70, 72, 68, 65, 67, 70, 73, 71, 74, 76]
}

df = pd.DataFrame(data)

f, ax = plt.subplots(figsize=(10, 5))

sns.lineplot(data=df, x='Year', y='Productivity Index', color='#1f77b4', linewidth=2.5)

ax.set(xlim=(2010, 2022), xlabel='Year', ylabel='Productivity Index')
ax.set_title('Annual Productivity Trends in Business', fontsize=16)

for x, y in zip(df['Year'], df['Productivity Index']):
    ax.text(x, y, f'{y}', color='black', ha="center")

plt.show()