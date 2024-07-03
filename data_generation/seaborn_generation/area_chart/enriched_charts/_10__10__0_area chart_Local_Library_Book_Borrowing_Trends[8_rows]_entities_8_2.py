
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a DataFrame from the provided data
data = {
    'Date': pd.date_range(start='2023-01-01', periods=31, freq='D'),
    'Step Counts': [5000, 5200, 5300, 5100, 5500, 5800, 6000, 6200, 6300, 6500, 6700, 6900, 7100, 7200,
                    7300, 7400, 7500, 7600, 7700, 7800, 7900, 8000, 8100, 8200, 8300, 8400, 8500, 8600,
                    8700, 8800, 8900]
}

df = pd.DataFrame(data)

# Set the size of the chart
plt.figure(figsize=(16, 8))

# Create an area chart
sns.lineplot(data=df, x='Date', y='Step Counts', color='#FF6347', lw=2)
plt.fill_between(df['Date'], 0, df['Step Counts'], color='#FF6347', alpha=0.3)

# Add title and labels
plt.title('Daily Step Counts for January 2023')
plt.xlabel('Date')
plt.ylabel('Step Counts')

# Assign text label on the chart
plt.text(x=df['Date'][30], y=df['Step Counts'][30], s="Highest", color='#2E8B57', va='bottom', ha='right')

# Enhance the x-axis date format
plt.xticks(rotation=45)

# Display the chart
plt.tight_layout()
plt.show()