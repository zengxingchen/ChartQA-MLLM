
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Date': pd.date_range(start='2023-01-01', periods=31, freq='D'),
    'Visitors': [
        1200, 1500, 1600, 1650, 1700, 1300, 1400, 1550, 1580, 1620,
        1480, 1450, 1700, 1800, 1850, 1900, 2000, 2050, 1950, 1850,
        1780, 1760, 1800, 1830, 1890, 1910, 1920, 1930, 2000, 2050, 2100
    ]
}

df = pd.DataFrame(data)

# Visualization
plt.figure(figsize=(12, 6))
area_chart = sns.lineplot(data=df, x='Date', y='Visitors', color="#76a5af")
plt.fill_between(data['Date'], data['Visitors'], color="#b0c4de")

# Annotation
for index in range(0, df.shape[0], 5):  # Adding annotations every 5 days for clarity
    date = df.iloc[index]['Date']
    visitors = df.iloc[index]['Visitors']
    plt.text(date, visitors + 50, str(visitors), ha='center')

# Customization
plt.title('Daily Website Visitors in January 2023')
plt.xlabel('Date')
plt.ylabel('Number of Visitors')
sns.despine()  # Removing the top and the right spines for better visual appeal

# Show the plot
plt.show()