
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
    'Steps': [5000, 5200, 4800, 5500, 6000, 6100, 6300, 7000, 6900, 7200, 7400, 7500,
              7600, 7800, 8000, 8200, 8500, 8300, 8600, 8800, 8700, 9000, 9200, 9100,
              9400, 9500, 9700, 9800, 10000, 10200, 10400]
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

plt.figure(figsize=(18, 10))

sns.lineplot(data=df, x='Date', y='Steps', color='#ff5733')
plt.fill_between(df['Date'], df['Steps'], color="#ffc1b6")

plt.xticks(rotation=45)

highest_steps_date = df.loc[df['Steps'].idxmax(), 'Date']
highest_steps = df['Steps'].max()
plt.text(highest_steps_date, highest_steps, f'Highest: {highest_steps}', ha='left', va='bottom')

plt.title("Daily Steps Count in January 2023", fontsize=16)
plt.xlabel("Date", fontsize=14)
plt.ylabel("Steps", fontsize=14)

plt.show()