
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
    'Units Sold': [120, 135, 110, 155, 175, 165, 185, 195, 225, 215, 235, 255,
                   245, 265, 275, 295, 315, 305, 325, 345, 335, 355, 375, 365,
                   385, 405, 395, 415, 425, 445, 455]
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

plt.figure(figsize=(14, 7))

sns.lineplot(data=df, x='Date', y='Units Sold', color='#FF5733')
plt.fill_between(df['Date'], df['Units Sold'], color="#FFC300")

plt.xticks(rotation=45)

highest_units_sold_date = df.loc[df['Units Sold'].idxmax(), 'Date']
highest_units_sold = df['Units Sold'].max()
plt.text(highest_units_sold_date, highest_units_sold, f'Highest: {highest_units_sold}', ha='left', va='bottom')

plt.title("Daily Book Sales in January 2023")
plt.xlabel("Date")
plt.ylabel("Units Sold")

plt.show()