
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Year": [i for i in range(2000, 2024)],
    "Number_of_Book_Releases": [
        120, 125, 130, 140, 145, 150, 160, 165, 170, 180, 185, 190, 200, 210, 
        215, 220, 230, 240, 250, 260, 275, 280, 290, 300
    ]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 10))
sns.set_theme(style="whitegrid")
area_chart = sns.lineplot(x="Year", y="Number_of_Book_Releases", data=df)
area_chart.fill_between(df['Year'], df['Number_of_Book_Releases'], alpha=0.4, color='#4B0082')

plt.title('Annual Number of Book Releases Over Time', fontsize=18)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Number of Book Releases', fontsize=14)

plt.annotate(f'{df.iloc[-1]["Number_of_Book_Releases"]}',
             xy=(df.iloc[-1]['Year'], df.iloc[-1]['Number_of_Book_Releases']),
             xytext=(df.iloc[-2]['Year'], df.iloc[-1]['Number_of_Book_Releases'] + 15),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=12)

sns.despine(left=True, bottom=True)
plt.show()