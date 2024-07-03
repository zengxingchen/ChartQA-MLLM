
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Create a DataFrame based on the input data
data = {
    'Category': ['Vegetables', 'Fruits', 'Grains', 'Dairy', 'Meat'],
    'Carbohydrates': [10, 15, 30, 8, 5],
    'Proteins': [20, 10, 10, 15, 25],
    'Fats': [5, 5, 2, 7, 10],
}
df = pd.DataFrame(data)

# Compute percentages for the stack
df_percentage = df.set_index('Category')
df_percentage = df_percentage.divide(df_percentage.sum(axis=1), axis=0)

# Create a vertical stacked bar chart
fig, ax = plt.subplots(figsize=(12, 6))
df_percentage.plot(kind='bar', stacked=True, color=['#FF5733', '#33FF57', '#3357FF'], width=0.7, ax=ax)

# Customize the plot to reflect percentages
for n in df_percentage:
    for i, (cs, ab, pc) in enumerate(zip(df_percentage.iloc[:, :].cumsum(1)[n], 
                                          df_percentage[n], df_percentage[n])):
        if pc > 0:  # Only show text for non-zero percentages
            plt.text(i, cs - ab / 2, str(round(pc * 100, 1)) + '%', va='center', ha='center', fontsize=10)

plt.title('Nutrient Distribution in Different Food Categories')
ax.set_ylabel('Percentage')
ax.set_xlabel('Food Categories')
plt.legend(title='Nutrients', bbox_to_anchor=(1.05, 1), loc='upper left')

# Adjust the size and layout
plt.tight_layout()

plt.show()