
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Create a DataFrame based on the input data
data = {
    'Category': ['Q1', 'Q2', 'Q3', 'Q4'],
    'Marketing': [15, 20, 10, 25],
    'Development': [25, 15, 20, 10],
    'Sales': [10, 15, 30, 20],
    'HR': [5, 10, 15, 10],
    'Finance': [15, 10, 5, 10],
}
df = pd.DataFrame(data)

# Compute percentages for the stack
df_percentage = df.set_index('Category')
df_percentage = df_percentage.divide(df_percentage.sum(axis=1), axis=0)

# Create a vertical stacked bar chart
fig, ax = plt.subplots(figsize=(10, 8))
df_percentage.plot(kind='bar', stacked=True, color=['#FFA07A', '#20B2AA', '#778899', '#FFD700', '#FF6347'], width=0.8, ax=ax)

# Customize the plot to reflect percentages
for n in df_percentage:
    for i, (cs, ab, pc) in enumerate(zip(df_percentage.iloc[:, :].cumsum(1)[n], 
                                          df_percentage[n], df_percentage[n])):
        if pc > 0:  # Only show text for non-zero percentages
            plt.text(i, cs - ab / 2, str(round(pc * 100, 1)) + '%', va='center', ha='center', fontsize=10)

plt.title('Departmental Budget Distribution by Quarter')
ax.set_ylabel('Percentage')
ax.set_xlabel('Quarters')
plt.legend(title='Departments', bbox_to_anchor=(1.05, 1), loc='upper left')

# Adjust the size and layout
plt.tight_layout()

plt.show()