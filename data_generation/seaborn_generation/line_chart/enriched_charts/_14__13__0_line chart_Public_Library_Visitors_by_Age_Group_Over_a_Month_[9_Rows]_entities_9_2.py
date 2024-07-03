
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Year': [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021],
    'Annual CO2 Emissions (Mt)': [1000, 1050, 1075, 1100, 1080, 1120, 1150, 1140, 1160, 1180, 1190]
}
df = pd.DataFrame(data)

f, ax = plt.subplots(figsize=(10, 6))

sns.lineplot(x="Year", y="Annual CO2 Emissions (Mt)", data=df, color="#FF5733", marker='s')

ax.set_title('Annual CO2 Emissions Over Time', fontsize=16, pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Annual CO2 Emissions (Mt)', fontsize=12)

for x, y in zip(df['Year'], df['Annual CO2 Emissions (Mt)']):
    ax.text(x, y, y, color="blue", ha="center", va="bottom")

plt.show()