
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
    'Streaming Hours': [1200, 1250, 1300, 1350, 1400, 1450, 1500, 1550, 1600, 1650,
                        1700, 1750, 1800, 1850, 1900, 1950, 2000, 2050, 2100, 2150,
                        2200, 2250, 2300, 2350, 2400, 2450, 2500, 2550, 2600, 2650, 2700]
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

plt.figure(figsize=(14, 7))
sns.lineplot(data=df, x='Date', y='Streaming Hours', color='#ff5733')
plt.fill_between(df['Date'], df['Streaming Hours'], color="#ffa07a")

plt.xticks(rotation=45)

highest_hours_date = df.loc[df['Streaming Hours'].idxmax(), 'Date']
highest_hours = df['Streaming Hours'].max()
plt.text(highest_hours_date, highest_hours, f'Highest: {highest_hours}', ha='left', va='bottom')

plt.title("Monthly Streaming Hours of a Popular Music Album in 2023", pad=20)
plt.xlabel("Date")
plt.ylabel("Streaming Hours")

plt.show()