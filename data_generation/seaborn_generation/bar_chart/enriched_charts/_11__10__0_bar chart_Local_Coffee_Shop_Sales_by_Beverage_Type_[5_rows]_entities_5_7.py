
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Genre': ['Mystery', 'Romance', 'Fantasy', 'Science Fiction', 'Non-fiction', 'Thriller', 'Biography', 'Self-help', 'Historical', "Children's"],
    'Book Sales (in millions)': [150, 200, 180, 140, 170, 160, 130, 120, 110, 190]
}

df = pd.DataFrame(data)
df = df.sort_values('Book Sales (in millions)', ascending=True)

plt.figure(figsize=(8, 10))
sns.barplot(
    x='Book Sales (in millions)',
    y='Genre',
    data=df,
    palette=[
        '#FF6347', '#4682B4', '#7FFF00', '#6A5ACD', '#FFD700',
        '#DA70D6', '#00BFFF', '#32CD32', '#FF4500', '#8A2BE2'
    ],
    linewidth=1.5,
    edgecolor='black'
)

for bar in plt.gca().patches:
    bar.set_height(0.5)

plt.xlabel('Book Sales (in millions)')
plt.ylabel('Genre')
plt.title('Book Sales by Genre')
plt.show()