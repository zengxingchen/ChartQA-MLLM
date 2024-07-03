
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data in a Python dictionary
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Product A': [120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230],
    'Product B': [200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310],
    'Product C': [150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260],
    'Product D': [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210]
}

# Create a DataFrame
df = pd.DataFrame(data)
df.index = df['Month']
df.drop('Month', axis=1, inplace=True)

# Plotting the stacked area chart
plt.figure(figsize=(14, 10))
pal = ['#FF5733', '#33FF57', '#3357FF', '#FF33A8']

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
for i, value in enumerate(df_cum['Product D']):
    plt.text(i, value + 10, f"{value}", ha='center', va='bottom', fontsize=9)

# Customize the chart
plt.title('Monthly Sales by Product Category', fontsize=18)
plt.xticks(rotation=45)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Sales (Units)', fontsize=14)
plt.legend(labels=df.columns, loc='upper left', fontsize=12)
plt.tight_layout()
plt.show()