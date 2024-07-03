
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a DataFrame from the provided data
data = {
    'Date': pd.date_range(start='2023-01-01', periods=31, freq='D'),
    'Calories Burned': [2200, 2300, 2500, 2600, 2400, 2700, 2900, 3100, 3300, 3500, 3600, 3700, 3900, 4000,
                        4100, 4200, 4300, 4400, 4500, 4600, 4700, 4800, 4900, 5000, 5100, 5200, 5300, 5400,
                        5500, 5600, 5700]
}

df = pd.DataFrame(data)

# Set the size of the chart
plt.figure(figsize=(14, 7))

# Create an area chart
sns.lineplot(data=df, x='Date', y='Calories Burned', color='#4682B4', lw=2)
plt.fill_between(df['Date'], 0, df['Calories Burned'], color='#4682B4', alpha=0.3)

# Add title and labels
plt.title('Daily Calories Burned for January 2023')
plt.xlabel('Date')
plt.ylabel('Calories Burned')

# Assign text label on the chart
plt.text(x=df['Date'][30], y=df['Calories Burned'][30], s="Peak", color='#8B0000', va='bottom', ha='right')

# Enhance the x-axis date format
plt.xticks(rotation=45)

# Display the chart
plt.tight_layout()
plt.show()