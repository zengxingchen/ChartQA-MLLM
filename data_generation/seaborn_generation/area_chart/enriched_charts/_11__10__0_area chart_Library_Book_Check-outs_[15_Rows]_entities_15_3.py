
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
    'Active Users': [500, 550, 600, 580, 620, 610, 630, 640, 650, 660, 670, 680, 690, 700, 710,
                     720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870]
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

plt.figure(figsize=(16, 8))
sns.lineplot(data=df, x='Date', y='Active Users', color='#3366cc')
plt.fill_between(df['Date'], df['Active Users'], color="#99ccff")

plt.xticks(rotation=45)

highest_users_date = df.loc[df['Active Users'].idxmax(), 'Date']
highest_users = df['Active Users'].max()
plt.text(highest_users_date, highest_users, f'Highest: {highest_users}', ha='left', va='bottom')

plt.title("Daily Active Users on the Platform in January 2023")
plt.xlabel("Date")
plt.ylabel("Number of Active Users")

plt.show()