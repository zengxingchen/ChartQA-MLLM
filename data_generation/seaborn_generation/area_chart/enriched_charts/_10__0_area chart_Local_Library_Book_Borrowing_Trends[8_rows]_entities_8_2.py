
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a DataFrame from the table data
data = {
    'Date': pd.date_range(start='2023-01-01', periods=31, freq='D'),
    'Temperature': [15.2, 16.0, 14.8, 15.5, 15.1, 14.7, 14.9, 15.3, 15.6, 15.9, 
                    16.2, 16.1, 15.8, 15.5, 15.4, 15.3, 15.6, 15.7, 15.8, 16.0, 
                    16.2, 16.5, 16.8, 16.7, 16.5, 16.2, 16.0, 15.8, 15.7, 15.9, 16.1]
}

df = pd.DataFrame(data)

# Set the size of the chart
plt.figure(figsize=(14, 7))

# Create an area chart
sns.lineplot(data=df, x='Date', y='Temperature', color='#2ca02c', lw=2)
plt.fill_between(df['Date'], 0, df['Temperature'], color='#2ca02c', alpha=0.3)

# Add title and labels
plt.title('Daily Temperature for January 2023', fontsize=16)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Temperature (°C)', fontsize=14)

# Assign text label on the chart
plt.text(x=df['Date'][22], y=df['Temperature'][22], s="Highest Temp", color='#d62728', va='bottom', ha='right')

# Enhance the x-axis date format
plt.xticks(rotation=45)

# Display the chart
plt.tight_layout()
plt.show()