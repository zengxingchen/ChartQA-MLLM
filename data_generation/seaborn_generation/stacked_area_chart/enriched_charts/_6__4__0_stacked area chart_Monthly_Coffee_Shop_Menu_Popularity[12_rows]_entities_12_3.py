
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data in a Python dictionary
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Exercise': [50, 55, 60, 62, 65, 70, 72, 75, 77, 80, 82, 85],
    'Healthy Eating': [60, 65, 70, 75, 80, 85, 87, 90, 92, 95, 97, 100],
    'Sleep': [70, 75, 78, 80, 82, 85, 88, 90, 92, 94, 96, 98],
    'Stress Management': [40, 42, 45, 47, 50, 52, 54, 55, 56, 58, 60, 62]
}

# Create a DataFrame
df = pd.DataFrame(data)
df.index = df['Month']
df.drop('Month', axis=1, inplace=True)

# Plotting the stacked area chart
plt.figure(figsize=(16, 12))
pal = ['#FF6347', '#4682B4', '#32CD32', '#FFD700']

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
for i, value in enumerate(df_cum['Stress Management']):
    plt.text(i, value + 5, f"{value}", ha='center', va='bottom', fontsize=9)

# Customize the chart
plt.title('Monthly Well-being Activities', fontsize=18, pad=20)
plt.xticks(rotation=45)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Well-being Activities (Hours)', fontsize=14)
plt.legend(title='Activities', labels=df.columns, loc='upper left')
plt.tight_layout()
plt.show()