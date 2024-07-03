
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Books': [15, 18, 20, 22, 25, 28, 30, 32, 35, 38, 40, 42],
    'Notes': [10, 12, 15, 18, 20, 22, 25, 27, 30, 32, 35, 37],
    'Assignments': [5, 7, 10, 12, 15, 18, 20, 22, 25, 27, 30, 32],
    'Quizzes': [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
}

df = pd.DataFrame(data)

# Define a color palette
palette = ["#4B0082", "#FF6347", "#4682B4", "#32CD32"]

# Melt DataFrame
df_melted = df.melt('Month', var_name='Study Material', value_name='Amount')

# Plot
plt.figure(figsize=(18, 10))

# Area plot
sns.set_style("whitegrid")
df.set_index('Month').plot(kind='area', stacked=True, color=palette, alpha=0.8, figsize=(18, 10))

# Customization
plt.title('Monthly Study Material Usage', fontsize=20, pad=25)
plt.xlabel('Month', fontsize=16)
plt.ylabel('Amount', fontsize=16)
plt.xticks(rotation=45)
plt.legend(title='Study Material Types', loc='upper left')

# Annotations
for i, material in enumerate(df.columns[1:]):
    y = df[material].cumsum() - (0.5 * df[material])
    for x, value in enumerate(y):
        if x == len(df) - 1:
            plt.text(x, value, f'{material}', fontsize=12, ha='left', va='center')

plt.tight_layout()
plt.show()