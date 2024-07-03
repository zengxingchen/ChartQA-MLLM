
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
    'Visitors': [100, 150, 130, 180, 160, 190, 220, 210, 250, 200, 230, 235, 215, 225, 270,
                 240, 280, 260, 255, 290, 270, 300, 280, 295, 285, 305, 310, 315, 320, 330, 340]
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

plt.figure(figsize=(16, 8))
sns.lineplot(data=df, x='Date', y='Visitors', color='#1f77b4')
plt.fill_between(df['Date'], df['Visitors'], color="#87ceeb")

plt.xticks(rotation=45)

highest_visitors_date = df.loc[df['Visitors'].idxmax(), 'Date']
highest_visitors = df['Visitors'].max()
plt.text(highest_visitors_date, highest_visitors, f'Highest: {highest_visitors}', ha='left', va='bottom', fontsize=12, color='black')

plt.title("Daily Visitors to the Science Museum in January 2023", fontsize=16, pad=20)
plt.xlabel("Date", fontsize=14)
plt.ylabel("Number of Visitors", fontsize=14)

plt.show()