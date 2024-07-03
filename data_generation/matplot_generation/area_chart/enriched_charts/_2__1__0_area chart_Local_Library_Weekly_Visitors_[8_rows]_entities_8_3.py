import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = {
    'Date': pd.date_range(start='2024-01-01', periods=24, freq='MS'),
    'Temperature': [10, 12, 15, 18, 22, 25, 28, 27, 23, 18, 13, 10, 
                    11, 14, 16, 20, 23, 26, 29, 28, 24, 19, 14, 11]
}
df = pd.DataFrame(data)

plt.figure(figsize=(14, 8))
plt.fill_between(df['Date'], df['Temperature'], color='#FF6347', alpha=0.6)
plt.plot(df['Date'], df['Temperature'], color='#FF4500', alpha=0.8)

plt.title('Monthly Temperature Over Two Years', fontsize=18, pad=20)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Temperature (°C)', fontsize=14)

max_temp = df['Temperature'].max()
max_date = df['Date'][df['Temperature'].idxmax()]
plt.annotate(f'Max Temp: {max_temp}°C', xy=(max_date, max_temp), xytext=(max_date, max_temp + 3),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.tight_layout()
plt.show()