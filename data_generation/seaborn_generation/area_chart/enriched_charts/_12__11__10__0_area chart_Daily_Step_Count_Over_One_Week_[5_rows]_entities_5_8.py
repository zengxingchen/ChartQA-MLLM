
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Date': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
    'BooksRead': [1, 2, 1, 3, 2, 3, 4, 5, 3, 4, 5, 6, 4, 5, 7, 6, 8, 7, 9, 8, 9, 8, 10, 9, 11, 10, 12, 11, 13, 12, 14]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 7))
area_chart = sns.lineplot(data=df, x='Date', y='BooksRead', color='#1f77b4')
area_chart.fill_between(df['Date'], df['BooksRead'], color='#aec7e8', alpha=0.5)

max_books = df['BooksRead'].max()
max_day = df['BooksRead'].idxmax() + 1
plt.text(max_day, max_books, 'Max Books\nRead', horizontalalignment='center', verticalalignment='bottom', color='#ff7f0e')

plt.title("Books Read Daily Over a Month", pad=20)
plt.xlabel("Day of the Month")
plt.ylabel("Books Read")

plt.show()