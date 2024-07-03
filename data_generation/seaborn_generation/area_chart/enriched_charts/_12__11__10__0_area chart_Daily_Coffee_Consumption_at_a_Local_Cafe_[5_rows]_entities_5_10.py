
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Year': ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022'],
    'GDP Growth Rate (%)': [2.5, 2.8, 3.1, 2.9, 3.3, 3.7, 3.9, 4.1, 4.3, 4.5, 4.7, 5.0, 5.2]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 7))
chart = sns.lineplot(x='Year', y='GDP Growth Rate (%)', data=df, color="#2E86C1")

plt.fill_between(x=df['Year'], y1=df['GDP Growth Rate (%)'], color="#AED6F1", alpha=0.4)

for i in range(df.shape[0]):
    plt.text(df['Year'][i], df['GDP Growth Rate (%)'][i] + 0.1, f"{df['GDP Growth Rate (%)'][i]}%", horizontalalignment='center')

plt.title('Annual GDP Growth Rate Over Time', fontsize=18, pad=20)
plt.xlabel('Year')
plt.ylabel('GDP Growth Rate (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()