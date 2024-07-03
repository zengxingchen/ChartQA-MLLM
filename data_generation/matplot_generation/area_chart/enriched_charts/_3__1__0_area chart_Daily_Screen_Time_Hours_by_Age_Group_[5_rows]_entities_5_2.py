
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Date': [
        '2024-01-01', '2024-02-01', '2024-03-01', '2024-04-01', '2024-05-01',
        '2024-06-01', '2024-07-01', '2024-08-01', '2024-09-01', '2024-10-01',
        '2024-11-01', '2024-12-01', '2025-01-01', '2025-02-01', '2025-03-01',
        '2025-04-01', '2025-05-01', '2025-06-01', '2025-07-01', '2025-08-01',
        '2025-09-01', '2025-10-01', '2025-11-01', '2025-12-01'
    ],
    'Value': [
        7, 17, 10, 14, 22, 12, 28, 20, 24, 32, 30, 38, 36, 42, 45, 50, 55, 60, 58, 65, 70, 67, 75, 80
    ]
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

plt.figure(figsize=(14, 8))
plt.fill_between(df['Date'], df['Value'], color='#FFA07A', alpha=0.5)
plt.plot(df['Date'], df['Value'], color='#FF6347', alpha=0.8)

plt.title('Monthly Fitness Progress Over Two Years', fontsize=16)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Workout Hours (in hours)', fontsize=14)

for i in range(len(df)):
    if i % 4 == 0:
        plt.text(df['Date'][i], df['Value'][i] + 1, str(df['Value'][i]), fontsize=10, ha='center')

plt.show()