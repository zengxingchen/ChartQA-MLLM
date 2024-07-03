
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Date': pd.date_range(start='2023-05-01', periods=40, freq='D'),
    'Temperature': [22, 23, 21, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 8))
plt.fill_between(df['Date'], df['Temperature'], color='#ff6347', alpha=0.5)
plt.plot(df['Date'], df['Temperature'], color='#ff6347', alpha=0.8)

plt.title('Daily Temperature Over Time', fontsize=18, pad=20)
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')

plt.annotate('Highest Temperature', xy=(pd.Timestamp('2023-06-09'), 60), xytext=(pd.Timestamp('2023-06-05'), 55),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, ha='center')

plt.tight_layout()
plt.show()