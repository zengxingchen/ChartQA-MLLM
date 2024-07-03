
import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame from the provided data table
data = {
    'Date': pd.date_range(start='2023-01-01', end='2023-01-31'),
    'Daily_Step_Count': [
        5020, 5140, 4980, 5230, 5400, 5450, 5600, 5750, 5800, 5950,
        6100, 6200, 6300, 6150, 6000, 6050, 6150, 6200, 6350, 6450,
        6600, 6700, 6800, 6950, 7100, 7200, 7300, 7450, 7600, 7700,
        7850
    ]
}
df = pd.DataFrame(data)

# Resize the plot
plt.figure(figsize=(14, 8))

# Create an area plot
plt.plot(df['Date'], df['Daily_Step_Count'], color="#1f77b4", label='Daily Steps')
plt.fill_between(df['Date'], df['Daily_Step_Count'], color="#1f77b4", alpha=0.3)

# Annotating the highest point
max_steps = df['Daily_Step_Count'].max()
max_date = df.loc[df['Daily_Step_Count'].idxmax(), 'Date']
plt.annotate(f'Max: {max_steps}', xy=(max_date, max_steps),
             xytext=(max_date, max_steps + 500), textcoords='data',
             arrowprops=dict(facecolor='#333333', shrink=0.05),
             horizontalalignment='center', verticalalignment='top')

# Change the appearance of the plot
plt.title('Daily Step Count in January 2023')
plt.xlabel('Date')
plt.ylabel('Step Count')
plt.legend(loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()