
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Create a DataFrame based on the input data
data = {
    'Category': ['Category1', 'Category2', 'Category3', 'Category4', 'Category5'],
    'ValueA': [30, 35, 45, 20, 40],
    'ValueB': [20, 45, 30, 35, 25],
    'ValueC': [50, 20, 25, 45, 35],
}
df = pd.DataFrame(data)

# Compute percentages for the stack
df_percentage = df.set_index('Category')
df_percentage = df_percentage.divide(df_percentage.sum(axis=1), axis=0)

# Create a horizontal stacked bar chart
fig, ax = plt.subplots(figsize=(10, 8))
df_percentage.plot(kind='barh', stacked=True, color=['#AD1457', '#6A1B9A', '#283593'], ax=ax)

# Customize the plot to reflect percentages
for n in df_percentage:
    for i, (cs, ab, pc) in enumerate(zip(df_percentage.iloc[:, :].cumsum(1)[n], 
                                          df_percentage[n], df_percentage[n])):
        if pc > 0:  # Only show text for non-zero percentages
            plt.text(cs - ab / 2, i, str(round(pc * 100, 1)) + '%', va='center', ha='center')

plt.title('Diversified Percentage Stacked Bar Chart')
ax.set_xlabel('Percentage')
ax.set_ylabel('Categories')
plt.legend(title='Values', bbox_to_anchor=(1.05, 1), loc='upper left')

# Adjust the size and layout
plt.tight_layout()

plt.show()