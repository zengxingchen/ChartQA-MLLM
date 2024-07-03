
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data in a Python dictionary
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Sector A': [500, 520, 550, 510, 500, 560, 580, 590, 600, 620, 630, 640],
    'Sector B': [700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810],
    'Sector C': [600, 630, 650, 680, 660, 670, 690, 710, 720, 740, 750, 760],
    'Sector D': [300, 310, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420]
}

# Create a DataFrame
df = pd.DataFrame(data)
df.index = df['Month']
df.drop('Month', axis=1, inplace=True)

# Plotting the stacked area chart
plt.figure(figsize=(14, 10))
pal = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1']

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
for i, value in enumerate(df_cum['Sector D']):
    plt.text(i, value + 10, f"{value}", ha='center', va='bottom', fontsize=9)

# Customize the chart
plt.title('Monthly Sales by Sector', fontsize=16, pad=20)
plt.xticks(rotation=45)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Sales (Units)', fontsize=12)
plt.legend(title='Sectors', labels=df.columns)
plt.tight_layout()
plt.show()