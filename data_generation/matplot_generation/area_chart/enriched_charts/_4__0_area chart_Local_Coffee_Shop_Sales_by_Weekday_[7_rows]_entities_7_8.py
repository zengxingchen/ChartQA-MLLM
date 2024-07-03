import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame from the provided data table
data = {
    'Date': pd.date_range(start='2023-01-01', end='2023-01-31'),
    'Subscribers': [
        1000, 1012, 1025, 1050, 1075, 1100, 1130, 1150, 1175, 1200,
        1230, 1260, 1300, 1325, 1350, 1375, 1400, 1430, 1450, 1480,
        1500, 1525, 1550, 1575, 1600, 1625, 1650, 1675, 1700, 1725,
        1750
    ]
}
df = pd.DataFrame(data)

# Resize the plot
plt.figure(figsize=(14, 7))

# Create an area plot
sns.lineplot(data=df, x='Date', y='Subscribers', color="#2ecc71")
plt.fill_between(df['Date'], df['Subscribers'], color="#2ecc71", alpha=0.3)

# Annotating the highest point
max_subscribers = df['Subscribers'].max()
max_date = df.loc[df['Subscribers'].idxmax(), 'Date']
plt.annotate(f'Max: {max_subscribers}', xy=(max_date, max_subscribers),
             xytext=(max_date, max_subscribers + 50), textcoords='data',
             arrowprops=dict(facecolor='#333333', shrink=0.05),
             horizontalalignment='center', verticalalignment='top')

# Change the appearance of the plot
plt.title('Daily New Subscribers in January 2023')
plt.xlabel('Date')
plt.ylabel('Number of Subscribers')
sns.despine()
plt.show()