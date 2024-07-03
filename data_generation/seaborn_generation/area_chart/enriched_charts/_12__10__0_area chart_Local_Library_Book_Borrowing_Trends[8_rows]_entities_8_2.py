
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a DataFrame from the table data
data = {
    'Date': pd.date_range(start='2023-01-01', periods=31, freq='D'),
    'Distance': [5.2, 6.0, 4.8, 5.5, 6.1, 5.7, 5.9, 6.3, 6.6, 6.9, 
                 7.2, 7.1, 6.8, 6.5, 6.4, 6.3, 6.6, 6.7, 6.8, 7.0, 
                 7.2, 7.5, 7.8, 7.7, 7.5, 7.2, 7.0, 6.8, 6.7, 6.9, 7.1]
}

df = pd.DataFrame(data)

# Set the size of the chart
plt.figure(figsize=(12, 6))

# Create an area chart
sns.lineplot(data=df, x='Date', y='Distance', color='#1f77b4', lw=2)
plt.fill_between(df['Date'], 0, df['Distance'], color='#1f77b4', alpha=0.3)

# Add title and labels
plt.title('Daily Running Distance for January 2023', fontsize=16)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Distance (km)', fontsize=14)

# Assign text label on the chart
plt.text(x=df['Date'][21], y=df['Distance'][21], s="Longest Distance", color='#d62728', va='bottom', ha='right')

# Enhance the x-axis date format
plt.xticks(rotation=45)

# Display the chart
plt.tight_layout()
plt.show()