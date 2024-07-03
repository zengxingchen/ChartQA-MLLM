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
        5, 15, 8, 12, 20, 10, 25, 18, 22, 30, 28, 35, 32, 38, 40, 45, 50, 55, 53, 60, 65, 62, 70, 75
    ]
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

plt.figure(figsize=(12, 6))
plt.fill_between(df['Date'], df['Value'], color='#87CEEB', alpha=0.5)
plt.plot(df['Date'], df['Value'], color='#4682B4', alpha=0.8)

plt.title('Projected Monthly Sales Over Two Years', fontsize=16)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Sales (in thousands)', fontsize=14)

# Adding annotation
for i in range(len(df)):
    if i % 6 == 0:
        plt.text(df['Date'][i], df['Value'][i] + 1, str(df['Value'][i]), fontsize=10, ha='center')

plt.show()