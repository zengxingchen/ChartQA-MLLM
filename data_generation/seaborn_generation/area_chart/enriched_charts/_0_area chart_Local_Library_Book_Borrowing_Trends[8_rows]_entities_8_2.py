
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a DataFrame from the pasted table data
data = {
    'Date': pd.date_range(start='2023-01-01', periods=31, freq='D'),
    'Pageviews': [500, 600, 750, 680, 700, 810, 900, 850, 920, 830, 890, 930, 980, 1050,
                  1100, 1200, 1150, 1170, 1230, 1300, 1350, 1400, 1390, 1420, 1380,
                  1450, 1490, 1550, 1500, 1480, 1600]
}

df = pd.DataFrame(data)

# Set the size of the chart
plt.figure(figsize=(12, 6))

# Create an area chart
sns.lineplot(data=df, x='Date', y='Pageviews', color='#1f77b4', lw=2)
plt.fill_between(data['Date'], 0, data['Pageviews'], color='#1f77b4', alpha=0.3)

# Add title and labels
plt.title('Daily Website Pageviews for January 2023')
plt.xlabel('Date')
plt.ylabel('Pageviews')

# Assign text label on the chart
plt.text(x=df['Date'][30], y=df['Pageviews'][30], s="Peak", color='#ff7f0e', va='bottom', ha='right')

# Enhance the x-axis date format
plt.xticks(rotation=45)

# Display the chart
plt.tight_layout()
plt.show()