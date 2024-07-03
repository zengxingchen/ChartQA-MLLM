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
    'Hours_Studied': [2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 
                      6.5, 7.0, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 
                      8.0, 8.5, 9.0, 3.5, 4.0, 4.5, 5.0]
}
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

plt.figure(figsize=(16, 10))
sns.lineplot(data=df, x='Date', y='Hours_Studied', color='#1f77b4')
plt.fill_between(df['Date'], df['Hours_Studied'], color="#c6dbef")

plt.xticks(rotation=45)
highest_hours_date = df.loc[df['Hours_Studied'].idxmax(), 'Date']
highest_hours = df['Hours_Studied'].max()
plt.text(highest_hours_date, highest_hours, f'Highest: {highest_hours} hours', ha='left', va='bottom')

plt.title("Daily Hours Spent on Studying in January 2023", pad=20)
plt.xlabel("Date")
plt.ylabel("Hours Studied")

plt.show()