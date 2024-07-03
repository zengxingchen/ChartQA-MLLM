
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data in a Python dictionary
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Sector A': [450, 480, 520, 510, 530, 550, 560, 570, 590, 600, 620, 640],
    'Sector B': [700, 690, 680, 700, 720, 740, 750, 770, 790, 800, 810, 820],
    'Sector C': [600, 630, 620, 640, 650, 670, 690, 710, 720, 730, 740, 760],
    'Sector D': [320, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440]
}

# Create a DataFrame
df = pd.DataFrame(data)
df.index = df['Month']
df.drop('Month', axis=1, inplace=True)

# Plotting the stacked area chart
plt.figure(figsize=(16, 12))
pal = ['#FFA07A', '#20B2AA', '#778899', '#FF6347']

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
plt.title('Monthly Renewable Energy Generation by Sector', fontsize=20, pad=20)
plt.xticks(rotation=45)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Energy Generation (GWh)', fontsize=14)
plt.legend(title='Sectors', labels=df.columns, loc='upper left')
plt.tight_layout()
plt.show()