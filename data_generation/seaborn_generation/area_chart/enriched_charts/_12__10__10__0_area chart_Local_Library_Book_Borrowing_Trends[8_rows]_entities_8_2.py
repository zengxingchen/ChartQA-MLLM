
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a DataFrame from the provided data
data = {
    'Date': pd.date_range(start='2023-01-01', periods=31, freq='D'),
    'Daily Sales': [150, 160, 170, 180, 175, 190, 200, 210, 220, 230, 240, 245, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430]
}

df = pd.DataFrame(data)

# Set the size of the chart
plt.figure(figsize=(14, 7))

# Create an area chart
sns.lineplot(data=df, x='Date', y='Daily Sales', color='#4682B4', lw=2)
plt.fill_between(df['Date'], 0, df['Daily Sales'], color='#4682B4', alpha=0.3)

# Add title and labels
plt.title('Daily Sales for January 2023', fontsize=16)
plt.xlabel('Date')
plt.ylabel('Sales')

# Assign text label on the chart
plt.text(x=df['Date'][30], y=df['Daily Sales'][30], s="Highest Sales", color='#2E8B57', va='bottom', ha='right')

# Enhance the x-axis date format
plt.xticks(rotation=45)

# Display the chart
plt.tight_layout()
plt.show()