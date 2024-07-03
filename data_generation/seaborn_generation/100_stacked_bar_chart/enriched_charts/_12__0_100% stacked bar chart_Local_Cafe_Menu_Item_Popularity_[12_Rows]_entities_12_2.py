
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Create a DataFrame based on the input data
data = {
    'Category': ['Running', 'Swimming', 'Cycling', 'Yoga', 'Weightlifting'],
    'Cardio': [30, 35, 45, 20, 40],
    'Strength': [20, 40, 30, 35, 25],
    'Flexibility': [50, 25, 25, 45, 35],
}
df = pd.DataFrame(data)

# Compute percentages for the stack
df_percentage = df.set_index('Category')
df_percentage = df_percentage.divide(df_percentage.sum(axis=1), axis=0)

# Create a vertical stacked bar chart
fig, ax = plt.subplots(figsize=(12, 6))
df_percentage.plot(kind='bar', stacked=True, color=['#1E88E5', '#D32F2F', '#388E3C'], ax=ax, width=0.7)

# Customize the plot to reflect percentages
for n in df_percentage:
    for i, (cs, ab, pc) in enumerate(zip(df_percentage.iloc[:, :].cumsum(1)[n], 
                                          df_percentage[n], df_percentage[n])):
        if pc > 0:  # Only show text for non-zero percentages
            plt.text(i, cs - ab / 2, str(round(pc * 100, 1)) + '%', va='center', ha='center')

plt.title('Distribution of Exercise Types in Sports & Fitness')
ax.set_ylabel('Percentage')
ax.set_xlabel('Exercise Types')
plt.legend(title='Exercise Type', bbox_to_anchor=(1.05, 1), loc='upper left')

# Adjust the size and layout
plt.tight_layout()

plt.show()