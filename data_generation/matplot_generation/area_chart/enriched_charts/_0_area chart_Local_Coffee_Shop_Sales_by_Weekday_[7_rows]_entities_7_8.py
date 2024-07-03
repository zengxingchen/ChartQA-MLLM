
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame from the provided data table
data = {
    'Date': pd.date_range(start='2023-01-01', end='2023-01-31'),
    'Electricity_Consumption': [
        320, 310, 315, 322, 340, 335, 345, 360, 358, 370,
        360, 375, 380, 370, 360, 350, 355, 362, 340, 330,
        335, 345, 350, 365, 370, 375, 380, 385, 390, 387,
        385
    ]
}
df = pd.DataFrame(data)

# Resize the plot
plt.figure(figsize=(12, 6))

# Create an area plot
sns.lineplot(data=df, x='Date', y='Electricity_Consumption', color="#3498db")
plt.fill_between(df['Date'], df['Electricity_Consumption'], color="#3498db", alpha=0.3)

# Annotating the highest point
max_consumption = df['Electricity_Consumption'].max()
max_date = df.loc[df['Electricity_Consumption'].idxmax(), 'Date']
plt.annotate(f'Max: {max_consumption}', xy=(max_date, max_consumption),
             xytext=(max_date, max_consumption + 10), textcoords='data',
             arrowprops=dict(facecolor='#333333', shrink=0.05),
             horizontalalignment='center', verticalalignment='top')

# Change the appearance of the plot
plt.title('Daily Electricity Consumption in January 2023')
plt.xlabel('Date')
plt.ylabel('Electricity Consumption (MWh)')
sns.despine()
plt.show()