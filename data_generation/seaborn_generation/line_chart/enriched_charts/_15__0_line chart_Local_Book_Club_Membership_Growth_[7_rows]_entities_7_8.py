
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'AirQualityIndex': [50, 55, 60, 75, 80, 95, 90, 85, 70, 65, 60, 55]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 10))
sns.lineplot(x='Month', y='AirQualityIndex', data=df, 
             color='#FF5733', linewidth=2.5)

for x, y in zip(df['Month'], df['AirQualityIndex']):
    plt.text(x, y, f"{y} AQI", color='black', fontsize=10, ha='center')

plt.title('Average Monthly Air Quality Index in City Y', fontsize=20, pad=30)
plt.xlabel('Month', fontsize=15)
plt.ylabel('Air Quality Index (AQI)', fontsize=15)
plt.xticks(rotation=45)
plt.grid(True)

plt.tight_layout()
plt.show()