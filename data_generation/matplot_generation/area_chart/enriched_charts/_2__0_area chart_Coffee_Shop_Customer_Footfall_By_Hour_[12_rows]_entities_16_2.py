
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Date': pd.date_range(start='2023-01-01', periods=31, freq='D'),
    'Temperature': [
        5, 7, 8, 6, 9, 10, 12, 15, 14, 13,
        12, 11, 13, 14, 15, 17, 19, 20, 18, 16,
        14, 15, 17, 18, 20, 21, 23, 24, 25, 27, 28
    ]
}

df = pd.DataFrame(data)

# Visualization
plt.figure(figsize=(14, 8))
area_chart = sns.lineplot(data=df, x='Date', y='Temperature', color="#ff6347")
plt.fill_between(data['Date'], data['Temperature'], color="#ffa07a")

# Annotation
for index in range(0, df.shape[0], 5):
    date = df.iloc[index]['Date']
    temperature = df.iloc[index]['Temperature']
    plt.text(date, temperature + 1, str(temperature), ha='center')

# Customization
plt.title('Daily Temperature in January 2023', pad=20)
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
sns.despine()

# Show the plot
plt.show()