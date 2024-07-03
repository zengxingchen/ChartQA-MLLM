
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Day': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    'BookSales': [5, 10, 15, 7, 9, 13, 8, 12, 14, 6, 11, 16, 5, 9, 7, 13, 14, 8, 10, 6],
    'LibraryVisits': [20, 35, 50, 25, 40, 45, 30, 42, 55, 22, 38, 60, 18, 33, 28, 50, 52, 34, 37, 20]
}

df = pd.DataFrame(data)

plt.figure(figsize=(12, 8))
scatterplot = sns.scatterplot(x='BookSales', y='LibraryVisits', data=df, color='#1E90FF')

scatterplot.set_title('Library Visits vs Book Sales', fontsize=18, pad=20)
scatterplot.set_xlabel('Book Sales (units)', fontsize=14)
scatterplot.set_ylabel('Library Visits (counts)', fontsize=14)

plt.show()