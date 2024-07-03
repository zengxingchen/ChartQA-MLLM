
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'City': ['New York', 'Los Angeles', 'Tokyo', 'London', 'Paris', 'Beijing', 'Sydney', 'Cape Town', 'Mumbai', 'Mexico City'],
    'Goals_2021': [20, 18, 15, 17, 12, 10, 8, 6, 4, 3],
    'Goals_2022': [25, 20, 18, 22, 16, 14, 11, 9, 6, 5],
    'Goals_2023': [30, 22, 21, 25, 19, 17, 13, 12, 8, 7]
}

df = pd.DataFrame(data)

# Melting the dataset to have cities, years, and values in separate columns
df_melted = df.melt(id_vars=['City'], var_name='Year', value_name='GoalsScored')

# Seaborn plot
plt.figure(figsize=(14, 10))

# Vertical bar chart with customized colors and bar width
ax = sns.barplot(
    data=df_melted,
    x='City',
    y='GoalsScored',
    hue='Year',
    palette=['#1f77b4', '#ff7f0e', '#2ca02c'],
    dodge=True
)

ax.bar_label(ax.containers[0], padding=3)
plt.ylabel('Goals Scored')
plt.xlabel('City')
plt.title('Annual Goals Scored by City Teams')
plt.legend(title='Year', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.show()