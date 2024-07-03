
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Genre': ['Science_Fiction', 'Romance', 'Mystery', 'Non_Fiction', 'Fantasy', 'Biography', 'Horror', 
              'Historical_Fiction', 'Self_Help', 'Classics', 'Graphic_Novels', 'Poetry', 'Adventure', 'Drama', 'Thriller'],
    'Average_Book_Sales': [35, 28, 22, 40, 30, 25, 18, 27, 33, 20, 24, 15, 26, 19, 21]
}

df = pd.DataFrame(data)

f, ax = plt.subplots(figsize=(12, 6))

palette = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', 
           '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#aec7e8', '#ffbb78', 
           '#98df8a', '#ff9896', '#c5b0d5']

sns.barplot(y='Average_Book_Sales', x='Genre', data=df,
            palette=palette, orient='v', ax=ax, dodge=False)

ax.set(ylim=(0, 50), xlabel="Genre", ylabel="Average Book Sales (in thousands)")
ax.set_title('Average Book Sales by Genre')

for container in ax.containers:
    ax.bar_label(container, label_type='edge', padding=3)

plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()