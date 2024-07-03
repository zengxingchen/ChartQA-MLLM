
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Your data converted into a pandas DataFrame
data = [
    {'Week': 'Week 1', ' Apples (kg)': 150, ' Oranges (kg)': 120, ' Bananas (kg)': 130, ' Berries (kg)': 90},
    {'Week': 'Week 2', ' Apples (kg)': 160, ' Oranges (kg)': 130, ' Bananas (kg)': 125, ' Berries (kg)': 100},
    {'Week': 'Week 3', ' Apples (kg)': 170, ' Oranges (kg)': 140, ' Bananas (kg)': 135, ' Berries (kg)': 110},
    {'Week': 'Week 4', ' Apples (kg)': 180, ' Oranges (kg)': 150, ' Bananas (kg)': 140, ' Berries (kg)': 120},
    {'Week': 'Week 5', ' Apples (kg)': 190, ' Oranges (kg)': 160, ' Bananas (kg)': 145, ' Berries (kg)': 130},
    {'Week': 'Week 6', ' Apples (kg)': 200, ' Oranges (kg)': 170, ' Bananas (kg)': 150, ' Berries (kg)': 140},
    {'Week': 'Week 7', ' Apples (kg)': 210, ' Oranges (kg)': 180, ' Bananas (kg)': 155, ' Berries (kg)': 150},
    {'Week': 'Week 8', ' Apples (kg)': 220, ' Oranges (kg)': 190, ' Bananas (kg)': 160, ' Berries (kg)': 160},
    {'Week': 'Week 9', ' Apples (kg)': 230, ' Oranges (kg)': 200, ' Bananas (kg)': 165, ' Berries (kg)': 170},
    {'Week': 'Week 10', ' Apples (kg)': 240, ' Oranges (kg)': 210, ' Bananas (kg)': 170, ' Berries (kg)': 180},
    {'Week': 'Week 11', ' Apples (kg)': 250, ' Oranges (kg)': 220, ' Bananas (kg)': 175, ' Berries (kg)': 190},
    {'Week': 'Week 12', ' Apples (kg)': 260, ' Oranges (kg)': 230, ' Bananas (kg)': 180, ' Berries (kg)': 200}
]
df = pd.DataFrame(data)

# Melting the dataframe to make it suitable for seaborn
df_melted = df.melt(id_vars='Week', var_name='Fruit', value_name='Kilograms')

# Creating the lineplot
sns.set_theme(style="whitegrid")
plt.figure(figsize=(12, 6))
lineplot = sns.lineplot(data=df_melted, x='Week', y='Kilograms', hue='Fruit', style='Fruit', markers=True, dashes=False)

# Customizing the plot
lineplot.set_title('Fruit Sales in Kilograms Over 12 Weeks')
lineplot.set_xlabel('Week')
lineplot.set_ylabel('Kilograms')
lineplot.legend(title='Fruit Type')
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot
plt.show()