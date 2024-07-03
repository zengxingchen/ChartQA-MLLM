
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = {
    'Category': ['Classic', 'Modern', 'Romantic', 'Victorian', 'Contemporary', 'Post-Modern'],
    'Poetry': [25, 20, 30, 35, 20, 25],
    'Fiction': [35, 30, 25, 20, 25, 30],
    'Non-Fiction': [20, 25, 30, 25, 35, 20],
    'Drama': [20, 25, 15, 20, 20, 25],
}

df = pd.DataFrame(data)

df_percentage = df.set_index('Category')
df_percentage = df_percentage.divide(df_percentage.sum(axis=1), axis=0)

fig, ax = plt.subplots(figsize=(12, 8))
df_percentage.plot(kind='bar', stacked=True, color=['#FF6347', '#4682B4', '#8A2BE2', '#3CB371'], ax=ax, width=0.6)

for n in df_percentage:
    for i, (cs, ab, pc) in enumerate(zip(df_percentage.iloc[:, :].cumsum(1)[n], 
                                          df_percentage[n], df_percentage[n])):
        if pc > 0:
            plt.text(i, cs - ab / 2, str(round(pc * 100, 1)) + '%', va='center', ha='center', fontsize=10)

plt.title('Literary Genres Across Different Eras', pad=20)
ax.set_ylabel('Percentage')
ax.set_xlabel('Eras')
plt.legend(title='Genres', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()