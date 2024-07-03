
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Create a DataFrame based on the input data
data = {
    'Food': ['Chicken', 'Rice', 'Avocado', 'Eggs', 'Almonds'],
    'Protein': [35, 7, 4, 30, 21],
    'Carbohydrates': [0, 85, 15, 1, 14],
    'Fat': [65, 8, 81, 69, 65],
}
df = pd.DataFrame(data)

# Compute percentages for the stack
df_percentage = df.set_index('Food')
df_percentage = df_percentage.divide(df_percentage.sum(axis=1), axis=0)

# Create a vertical stacked bar chart
fig, ax = plt.subplots(figsize=(10, 7))
df_percentage.plot(kind='bar', stacked=True, color=['#4CAF50', '#FF9800', '#F44336'], ax=ax, width=0.6)

# Customize the plot to reflect percentages
for n in df_percentage:
    for i, (cs, ab, pc) in enumerate(zip(df_percentage.iloc[:, :].cumsum(1)[n], 
                                          df_percentage[n], df_percentage[n])):
        if pc > 0:  # Only show text for non-zero percentages
            plt.text(i, cs - ab / 2, str(round(pc * 100, 1)) + '%', va='center', ha='center')

plt.title('Macronutrient Distribution in Different Foods')
ax.set_ylabel('Percentage')
ax.set_xlabel('Food Types')
plt.legend(title='Macronutrient', bbox_to_anchor=(1.05, 1), loc='upper left')

# Adjust the size and layout
plt.tight_layout()

plt.show()