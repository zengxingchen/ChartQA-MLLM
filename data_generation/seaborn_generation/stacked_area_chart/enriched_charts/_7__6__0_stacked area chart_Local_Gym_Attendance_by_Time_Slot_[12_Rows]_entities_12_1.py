
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Web Development': [3400, 3500, 3600, 3800, 4000, 4200, 4400, 4600, 4800, 5000, 5200, 5400],
    'Data Science': [2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000, 3100, 3200, 3300],
    'Mobile Development': [1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900],
    'Game Development': [1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600],
}

df = pd.DataFrame(data)

# Define a color palette
palette = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]

# Melt DataFrame
df_melted = df.melt('Month', var_name='Category', value_name='Participants')

# Plot
plt.figure(figsize=(18, 10))

# Area plot
sns.set_style("whitegrid")
df.set_index('Month').plot(kind='area', stacked=True, color=palette, alpha=0.7, figsize=(18, 10))

# Customization
plt.title('Monthly Participation in Various Programming Courses', fontsize=20, pad=20)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Number of Participants', fontsize=14)
plt.xticks(rotation=45)
plt.legend(title='Programming Courses', bbox_to_anchor=(1.05, 1), loc='upper left')

# Annotations
for i, category in enumerate(df.columns[1:]):
    y = df[category].cumsum() - (0.5 * df[category])
    for x, value in enumerate(y):
        if x == len(df) - 1:
            plt.text(x, value, f'{category}', fontsize=10, ha='left', va='center')

plt.tight_layout()
plt.show()