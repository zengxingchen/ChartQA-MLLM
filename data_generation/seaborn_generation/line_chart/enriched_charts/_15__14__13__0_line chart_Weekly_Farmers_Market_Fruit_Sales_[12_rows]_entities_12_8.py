
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Day': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
            21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    'BooksRead': [5, 7, 8, 6, 5, 9, 11, 14, 13, 15, 17, 19, 20, 21, 22, 25, 27, 26, 28, 30, 
                  32, 33, 34, 35, 37, 39, 40, 42, 43, 45]
}

df = pd.DataFrame(data)

sns.set_style("whitegrid")

plt.figure(figsize=(18, 10))
line_plot = sns.lineplot(x='Day', 
                         y='BooksRead', 
                         data=df, 
                         color='#3498db', 
                         linewidth=2.5)

plt.annotate('Reading Marathon', xy=(8, 14), xytext=(10, 25),
             arrowprops=dict(facecolor='#2980b9', shrink=0.05))
plt.annotate('Book Club Meeting', xy=(25, 37), xytext=(20, 40),
             arrowprops=dict(facecolor='#c0392b', shrink=0.05))

plt.title('Monthly Book Reading Trend', pad=20)
plt.xlabel('Day of the Month')
plt.ylabel('Number of Books Read')

plt.show()