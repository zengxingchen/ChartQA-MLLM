
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a DataFrame from the provided data
data = {
    'Date': pd.date_range(start='2023-06-01', periods=30, freq='D'),
    'Steps Walked': [5000, 5200, 5400, 5600, 5800, 6000, 6200, 6400, 6600, 6800, 7000, 7200, 7400, 7600, 7800, 8000, 8200, 8400, 8600, 8800, 9000, 9200, 9400, 9600, 9800, 10000, 10200, 10400, 10600, 10800]
}

df = pd.DataFrame(data)

# Set the size of the chart
plt.figure(figsize=(16, 8))

# Create an area chart
sns.lineplot(data=df, x='Date', y='Steps Walked', color='#FF4500', lw=2)
plt.fill_between(df['Date'], 0, df['Steps Walked'], color='#FF4500', alpha=0.3)

# Add title and labels
plt.title('Daily Steps Walked for June 2023', pad=20)
plt.xlabel('Date')
plt.ylabel('Steps Walked')

# Assign text label on the chart
plt.text(x=df['Date'][29], y=df['Steps Walked'][29], s="Peak", color='#0000CD', va='bottom', ha='right')

# Enhance the x-axis date format
plt.xticks(rotation=45)

# Display the chart
plt.tight_layout()
plt.show()