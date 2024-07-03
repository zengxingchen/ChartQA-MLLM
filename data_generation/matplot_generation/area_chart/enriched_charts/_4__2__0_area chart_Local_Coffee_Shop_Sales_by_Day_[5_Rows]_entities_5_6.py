
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'AvgTravelExpenditure': [1200, 1500, 1600, 1400, 1800, 1900, 2000, 1950, 1850, 1750, 1650, 1550]
}
df = pd.DataFrame(data)

# Convert 'Month' to categorical type with proper order
df['Month'] = pd.Categorical(df['Month'], categories=data['Month'], ordered=True)

# Create the area chart
plt.figure(figsize=(16, 10))
plt.plot(df['Month'], df['AvgTravelExpenditure'], lw=2, color='#1f77b4')
plt.fill_between(df['Month'], df['AvgTravelExpenditure'], color='#aec7e8', alpha=0.6)

# Annotate the chart with text labels
for i in range(df.shape[0]):
    plt.text(df['Month'][i], df['AvgTravelExpenditure'][i]+20, str(df['AvgTravelExpenditure'][i])+' USD', horizontalalignment='center')

# Customize the axes
plt.xlabel('Month')
plt.ylabel('Average Travel Expenditure (USD)')
plt.title('Average Monthly Travel Expenditure', pad=20)

# Show the final plot
plt.show()