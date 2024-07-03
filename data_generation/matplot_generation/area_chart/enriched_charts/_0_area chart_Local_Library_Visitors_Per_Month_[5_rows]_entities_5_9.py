
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a DataFrame from the provided table data
data = {
    'Date': pd.date_range(start='2023-01-01', periods=30, freq='D'),
    'Temperature': [
        5, 8, 6, 7, 9, 10, 8, 7, 4, 5, 6, 9, 8, 10, 11, 12, 10, 9, 11, 13, 14, 12, 13, 15, 14, 12, 13, 15, 16, 14
    ]
}

df = pd.DataFrame(data)

# Set the size of the chart
plt.figure(figsize=(10, 6))

# Create an area plot
sns.lineplot(data=df, x='Date', y='Temperature', color="#FF5733")
plt.fill_between(df.Date, df.Temperature, color="#FF5733", alpha=0.3)

# Assign annotation
for index, value in df.iterrows():
    if index % 5 == 0:  # Annotate every 5 days
        plt.text(value['Date'], value['Temperature'] + 0.5, f"{value['Temperature']}°C", ha='center')

# Set the chart title and labels
plt.title('Daily Average Temperatures in January 2023')
plt.xlabel('Date')
plt.ylabel('Average Temperature (°C)')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()