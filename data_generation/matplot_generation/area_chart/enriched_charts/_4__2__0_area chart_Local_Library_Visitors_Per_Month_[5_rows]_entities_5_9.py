
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Date': pd.date_range(start='2023-01-01', periods=30, freq='D'),
    'Books_Sold': [
        30, 45, 35, 50, 65, 55, 60, 70, 75, 85, 95, 100, 105, 110, 115,
        120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190
    ]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 10))

sns.lineplot(data=df, x='Date', y='Books_Sold', color="#FF5733")
plt.fill_between(df.Date, df.Books_Sold, color="#FF5733", alpha=0.4)

for index, value in df.iterrows():
    if index % 5 == 0:
        plt.text(value['Date'], value['Books_Sold'] + 5, f"{value['Books_Sold']} books", ha='center')

plt.title('Daily Book Sales in January 2023', fontsize=18, pad=25)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Books Sold', fontsize=14)
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()