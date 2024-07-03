
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data in a Python dictionary
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Primary Education': [100, 150, 200, 250, 110, 160, 210, 260, 120, 170, 220, 270],
    'Secondary Education': [130, 180, 230, 280, 140, 190, 240, 290, 150, 200, 250, 300],
    'Higher Education': [160, 210, 260, 310, 170, 220, 270, 320, 180, 230, 280, 330],
    'Continuing Education': [190, 240, 290, 340, 200, 250, 300, 350, 210, 260, 310, 360]
}

# Create a DataFrame
df = pd.DataFrame(data)
df.index = df['Month']
df.drop('Month', axis=1, inplace=True)

# Plotting the stacked area chart
plt.figure(figsize=(16, 12))
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
for i, value in enumerate(df_cum['Continuing Education']):
    plt.text(i, value + 10, f"{value}", ha='center', va='bottom', fontsize=9)

# Customize the chart
plt.title('Monthly Enrollment by Education Level', fontsize=18)
plt.xticks(rotation=45)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Enrollment (Units)', fontsize=14)
plt.legend(labels=df.columns, loc='upper left', fontsize=12)
plt.tight_layout()
plt.show()