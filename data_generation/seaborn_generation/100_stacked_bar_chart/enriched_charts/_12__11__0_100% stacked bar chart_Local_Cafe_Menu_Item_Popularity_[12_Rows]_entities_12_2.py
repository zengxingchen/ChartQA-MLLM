
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = {
    'Category': ['Philosophy', 'Ethics', 'Metaphysics', 'Epistemology', 'Logic', 'Aesthetics'],
    'ValueA': [10, 15, 20, 25, 30, 35],
    'ValueB': [20, 25, 30, 35, 20, 25],
    'ValueC': [30, 35, 25, 20, 25, 30],
    'ValueD': [40, 25, 25, 20, 25, 10],
}

df = pd.DataFrame(data)

df_percentage = df.set_index('Category')
df_percentage = df_percentage.divide(df_percentage.sum(axis=1), axis=0)

fig, ax = plt.subplots(figsize=(10, 7))
df_percentage.plot(kind='bar', stacked=True, color=['#FF4500', '#32CD32', '#1E90FF', '#FFD700'], ax=ax, width=0.7)

for n in df_percentage:
    for i, (cs, ab, pc) in enumerate(zip(df_percentage.iloc[:, :].cumsum(1)[n], 
                                          df_percentage[n], df_percentage[n])):
        if pc > 0:
            plt.text(i, cs - ab / 2, str(round(pc * 100, 1)) + '%', va='center', ha='center', fontsize=10)

plt.title('Branches of Philosophy', pad=20)
ax.set_ylabel('Percentage')
ax.set_xlabel('Categories')
plt.legend(title='Philosophical Aspects', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()