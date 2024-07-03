
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Your data
data = [
    {'Age Group': '5-12', 'Monday': 2.0, 'Tuesday': 1.5, 'Wednesday': 2.0, 'Thursday': 2.5, 'Friday': 3.0, 'Saturday': 4.0, 'Sunday': 3.5},
    {'Age Group': '13-18', 'Monday': 3.5, 'Tuesday': 3.0, 'Wednesday': 3.5, 'Thursday': 4.0, 'Friday': 4.5, 'Saturday': 5.0, 'Sunday': 4.5},
    {'Age Group': '19-30', 'Monday': 5.0, 'Tuesday': 4.5, 'Wednesday': 5.0, 'Thursday': 5.5, 'Friday': 6.0, 'Saturday': 7.0, 'Sunday': 6.5},
    {'Age Group': '31-45', 'Monday': 4.0, 'Tuesday': 4.0, 'Wednesday': 4.0, 'Thursday': 4.0, 'Friday': 4.0, 'Saturday': 5.0, 'Sunday': 4.5},
    {'Age Group': '46-60', 'Monday': 3.0, 'Tuesday': 3.0, 'Wednesday': 3.5, 'Thursday': 3.5, 'Friday': 4.0, 'Saturday': 4.5, 'Sunday': 4.0},
    {'Age Group': '61+', 'Monday': 2.5, 'Tuesday': 2.0, 'Wednesday': 2.5, 'Thursday': 3.0, 'Friday': 3.0, 'Saturday': 3.5, 'Sunday': 3.0}
]

# Convert to pandas DataFrame
df = pd.DataFrame(data)

# Melt the DataFrame to long format
df_long = df.melt(id_vars='Age Group', var_name='Day of Week', value_name='Value')

# Create the line chart using Seaborn
sns.set_theme(style='whitegrid')
plt.figure(figsize=(10, 6))

# Lineplot with diverse visual encoding
lineplot = sns.lineplot(data=df_long, x='Day of Week', y='Value', hue='Age Group', style='Age Group',
                        markers=True, dashes=False, palette='tab10', linewidth=2.5)

# Improve the legibility of the plot
plt.title('Weekly Trends by Age Group', fontsize=18)
plt.xlabel('Day of Week', fontsize=14)
plt.ylabel('Value', fontsize=14)
plt.xticks(fontsize=12, rotation=45)
plt.yticks(fontsize=12)
plt.legend(title='Age Group', title_fontsize='13', fontsize='11')

# Show the plot
plt.show()