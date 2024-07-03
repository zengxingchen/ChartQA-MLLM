import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Day': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    'Humidity': [40, 42, 45, 47, 44, 43, 48, 50, 52, 54, 56, 58, 60, 62, 65, 67, 66, 64, 63, 62, 61, 60, 59, 58, 57, 55, 54, 53, 52, 50]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 8))
plt.fill_between(df['Day'], df['Humidity'], color='#1f77b4', alpha=0.6)

plt.title('Humidity Levels Over 30 Days', fontsize=20, loc='center')
plt.xlabel('Day', fontsize=14)
plt.ylabel('Humidity (%)', fontsize=14)

plt.annotate('Highest Humidity', xy=(16, 67), xytext=(10, 70),
             arrowprops=dict(facecolor='red', shrink=0.05),
             fontsize=12, color='red')

plt.xticks(rotation=0)
plt.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()