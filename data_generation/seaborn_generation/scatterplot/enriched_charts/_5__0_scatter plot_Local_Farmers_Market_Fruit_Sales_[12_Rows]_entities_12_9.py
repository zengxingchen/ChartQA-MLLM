
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Day': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
            16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    'BooksRead': [3, 5, 7, 9, 6, 8, 10, 12, 11, 13, 15, 14, 16, 18, 17,
                  19, 20, 21, 22, 24, 23, 25, 26, 27, 28, 29, 30, 31, 32, 33],
    'HoursStudied': [2, 3, 4, 5, 3.5, 4.5, 5.5, 6, 5.8, 6.2, 7, 6.8, 7.2, 8, 7.5,
                     8.2, 8.5, 8.8, 9, 10, 9.5, 10.2, 10.5, 11, 11.2, 11.5, 12, 12.5, 13, 13.5]
}

df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(14, 8))
scatterplot = sns.scatterplot(x='BooksRead', y='HoursStudied',
                              data=df, palette=['#FF5733', '#33FF57'])

scatterplot.set_title('Relationship Between Books Read and Hours Studied', fontsize=16)
scatterplot.set_xlabel('Number of Books Read', fontsize=14)
scatterplot.set_ylabel('Hours Spent Studying', fontsize=14)

plt.show()