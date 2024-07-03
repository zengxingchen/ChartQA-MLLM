
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Year': [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021],
    'Concert Ticket Sales': [150, 180, 170, 200, 210, 195, 220, 230, 240, 220, 250]
}
df = pd.DataFrame(data)

f, ax = plt.subplots(figsize=(12, 7))

sns.lineplot(x="Year", y="Concert Ticket Sales", data=df, color="#4B0082", marker='o')

ax.set_title('Annual Concert Ticket Sales Over Time', fontsize=16, pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Concert Ticket Sales (in thousands)', fontsize=14)

for x, y in zip(df['Year'], df['Concert Ticket Sales']):
    ax.text(x, y, y, color="black", ha="center")

plt.show()