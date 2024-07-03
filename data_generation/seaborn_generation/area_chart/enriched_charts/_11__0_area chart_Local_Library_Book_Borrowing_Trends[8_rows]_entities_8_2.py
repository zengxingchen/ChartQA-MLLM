
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a DataFrame from the table data
data = {
    'Date': pd.date_range(start='2023-01-01', periods=31, freq='D'),
    'StockPrices': [100, 105, 102, 108, 112, 115, 118, 120, 125, 130, 128, 135, 138, 140, 142,
                    145, 148, 150, 155, 158, 160, 162, 165, 168, 170, 175, 178, 180, 182, 185, 188]
}

df = pd.DataFrame(data)

# Set the size of the chart
plt.figure(figsize=(14, 7))

# Create an area chart
sns.lineplot(data=df, x='Date', y='StockPrices', color='#4b0082', lw=2)
plt.fill_between(data['Date'], 0, data['StockPrices'], color='#9370db', alpha=0.3)

# Add title and labels
plt.title('Daily Stock Prices for January 2023', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Stock Prices', fontsize=12)

# Assign text label on the chart
plt.text(x=df['Date'][30], y=df['StockPrices'][30], s="Peak", color='#ff4500', va='bottom', ha='right', fontsize=12)

# Enhance the x-axis date format
plt.xticks(rotation=45)

# Display the chart
plt.tight_layout()
plt.show()