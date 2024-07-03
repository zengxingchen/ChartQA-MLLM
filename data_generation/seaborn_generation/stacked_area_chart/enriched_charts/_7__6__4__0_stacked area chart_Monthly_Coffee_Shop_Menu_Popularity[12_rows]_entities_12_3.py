
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data in a Python dictionary
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Urban Exploration': [15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70],
    'Photography': [30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85],
    'Concerts': [45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],
    'Theater': [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32]
}

# Create a DataFrame
df = pd.DataFrame(data)
df.index = df['Month']
df.drop('Month', axis=1, inplace=True)

# Plotting the stacked area chart
plt.figure(figsize=(18, 10))
pal = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

# Cumulate the values
df_cum = df.cumsum(axis=1)

# Plot the categories in reverse order
category_names = df.columns[::-1]
for i, column in enumerate(category_names):
    sns.lineplot(data=df_cum, x=df.index, y=column, color=pal[i])

# Fill the area between the lines
for i, column in enumerate(category_names):
    if i == 0:
        sns.lineplot(data=df_cum, x=df.index, y=column, color=pal[i])
        plt.fill_between(df.index, 0, df_cum[column], facecolor=pal[i], alpha=0.5)
    else:
        sns.lineplot(data=df_cum, x=df.index, y=column, color=pal[i])
        plt.fill_between(df.index, df_cum[category_names[i - 1]], df_cum[column], facecolor=pal[i], alpha=0.5)

# Add annotations
for i, value in enumerate(df_cum['Theater']):
    plt.text(i, value + 5, f"{value}", ha='center', va='bottom', fontsize=9)

# Customize the chart
plt.title('Monthly Engagement in Entertainment & Leisure Activities', fontsize=18, pad=20)
plt.xticks(rotation=45)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Engagement (Hours)', fontsize=14)
plt.legend(title='Activities', labels=df.columns, loc='upper right')
plt.tight_layout()
plt.show()