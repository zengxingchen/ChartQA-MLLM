
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
    'Sales': [250, 270, 260, 280, 300, 310, 320, 340, 330, 350, 370, 380,
              390, 410, 430, 450, 440, 460, 480, 470, 490, 510, 530, 520,
              540, 550, 570, 580, 600, 620, 640]
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

plt.figure(figsize=(16, 8))

sns.lineplot(data=df, x='Date', y='Sales', color='#3498db')
plt.fill_between(df['Date'], df['Sales'], color="#aed6f1")

plt.xticks(rotation=45)

highest_sales_date = df.loc[df['Sales'].idxmax(), 'Date']
highest_sales = df['Sales'].max()
plt.text(highest_sales_date, highest_sales, f'Highest: {highest_sales}', ha='left', va='bottom')

plt.title("Daily Sales in January 2023", fontsize=16)
plt.xlabel("Date", fontsize=14)
plt.ylabel("Sales", fontsize=14)

plt.show()