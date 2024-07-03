
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Year': [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021],
    'Average Running Speed (km/h)': [10.5, 10.8, 11.2, 11.0, 11.5, 11.3, 11.8, 12.0, 12.2, 12.5, 12.8]
}
df = pd.DataFrame(data)

f, ax = plt.subplots(figsize=(12, 8))

sns.lineplot(x="Year", y="Average Running Speed (km/h)", data=df, color="#33A1FF", marker='o')

ax.set_title('Average Running Speed Over the Years', fontsize=16, pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Average Running Speed (km/h)', fontsize=12)

for x, y in zip(df['Year'], df['Average Running Speed (km/h)']):
    ax.text(x, y, y, color="red", ha="center", va="bottom")

plt.show()