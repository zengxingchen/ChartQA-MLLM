
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Create a DataFrame based on the input data
data = {
    'Activity': ['Work', 'Leisure', 'Sleep', 'Exercise', 'Other'],
    'Work': [35, 10, 5, 5, 10],
    'Leisure': [15, 50, 5, 10, 20],
    'Sleep': [30, 25, 80, 5, 30],
    'Exercise': [10, 5, 5, 75, 10],
    'Other': [10, 10, 5, 5, 30],
}
df = pd.DataFrame(data)

# Compute percentages for the stack
df_percentage = df.set_index('Activity')
df_percentage = df_percentage.divide(df_percentage.sum(axis=1), axis=0)

# Create a vertical stacked bar chart
fig, ax = plt.subplots(figsize=(10, 8))
df_percentage.plot(kind='bar', stacked=True, color=['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A133FF'], ax=ax, width=0.6)

# Customize the plot to reflect percentages
for n in df_percentage:
    for i, (cs, ab, pc) in enumerate(zip(df_percentage.iloc[:, :].cumsum(1)[n], 
                                          df_percentage[n], df_percentage[n])):
        if pc > 0:  # Only show text for non-zero percentages
            plt.text(i, cs - ab / 2, str(round(pc * 100, 1)) + '%', va='center', ha='center')

plt.title('Daily Activities and Time Spent')
ax.set_ylabel('Percentage')
ax.set_xlabel('Activity')
plt.legend(title='Time Spent', bbox_to_anchor=(1.05, 1), loc='upper left')

# Adjust the size and layout
plt.tight_layout()

plt.show()