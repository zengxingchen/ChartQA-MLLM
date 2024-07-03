
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Date': ["2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04", "2023-01-05",
             "2023-01-06", "2023-01-07", "2023-01-08", "2023-01-09", "2023-01-10",
             "2023-01-11", "2023-01-12", "2023-01-13", "2023-01-14", "2023-01-15",
             "2023-01-16", "2023-01-17", "2023-01-18", "2023-01-19", "2023-01-20",
             "2023-01-21", "2023-01-22", "2023-01-23", "2023-01-24", "2023-01-25",
             "2023-01-26", "2023-01-27", "2023-01-28", "2023-01-29", "2023-01-30",
             "2023-01-31"],
    'Views': [1200, 1300, 1100, 1500, 1700, 1600, 1800, 1900, 2200, 2100, 2300, 2500,
              2400, 2600, 2700, 2900, 3100, 3000, 3200, 3400, 3300, 3500, 3700, 3600,
              3800, 4000, 3900, 4100, 4200, 4400, 4500]
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

plt.figure(figsize=(16, 8))

sns.lineplot(data=df, x='Date', y='Views', color='#4a90e2')
plt.fill_between(df['Date'], df['Views'], color="#a7c7e7")

plt.xticks(rotation=45)

highest_views_date = df.loc[df['Views'].idxmax(), 'Date']
highest_views = df['Views'].max()
plt.text(highest_views_date, highest_views, f'Highest: {highest_views}', ha='left', va='bottom')

plt.title("Daily Website Views in January 2023")
plt.xlabel("Date")
plt.ylabel("Views")

plt.show()