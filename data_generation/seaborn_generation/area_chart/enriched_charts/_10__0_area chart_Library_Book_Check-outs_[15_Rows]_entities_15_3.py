
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
    'Visitors': [100, 150, 130, 170, 160, 180, 190, 220, 210, 200, 195, 205, 215, 225, 230,
                 240, 235, 245, 255, 260, 270, 275, 280, 290, 285, 295, 300, 310, 320, 330, 340]
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

plt.figure(figsize=(14, 7))
sns.lineplot(data=df, x='Date', y='Visitors', color='#ff5733')
plt.fill_between(df['Date'], df['Visitors'], color="#c70039")

plt.xticks(rotation=45)

highest_visitors_date = df.loc[df['Visitors'].idxmax(), 'Date']
highest_visitors = df['Visitors'].max()
plt.text(highest_visitors_date, highest_visitors, f'Highest: {highest_visitors}', ha='left', va='bottom')

plt.title("Daily Visitors to the Museum in January 2023")
plt.xlabel("Date")
plt.ylabel("Number of Visitors")

plt.show()