
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Cardio Exercise': [3500, 3600, 3800, 4000, 4200, 4500, 4700, 4900, 5100, 5300, 5500, 5800],
    'Strength Training': [2000, 2200, 2400, 2600, 2800, 3000, 3200, 3400, 3600, 3800, 4000, 4200],
    'Yoga': [1500, 1600, 1700, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200, 3400],
    'Meditation': [700, 800, 850, 900, 950, 1000, 1100, 1150, 1200, 1250, 1300, 1400],
}

df = pd.DataFrame(data)

# Define a color palette
palette = ["#8c564b", "#e377c2", "#7f7f7f", "#bcbd22"]

# Melt DataFrame
df_melted = df.melt('Month', var_name='Activity', value_name='Participants')

# Plot
plt.figure(figsize=(14, 8))

# Area plot
sns.set_style("whitegrid")
df.set_index('Month').plot(kind='area', stacked=True, color=palette, alpha=0.6, figsize=(16, 9))

# Customization
plt.title('Monthly Participation in Various Fitness Activities', fontsize=16, pad=20)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Number of Participants', fontsize=12)
plt.xticks(rotation=45)
plt.legend(title='Fitness Activities', bbox_to_anchor=(1.05, 1), loc='upper left')

# Annotations
for i, activity in enumerate(df.columns[1:]):
    y = df[activity].cumsum() - (0.5 * df[activity])
    for x, value in enumerate(y):
        if x == len(df) - 1:
            plt.text(x, value, f'{activity}', fontsize=9, ha='left', va='center')

plt.tight_layout()
plt.show()