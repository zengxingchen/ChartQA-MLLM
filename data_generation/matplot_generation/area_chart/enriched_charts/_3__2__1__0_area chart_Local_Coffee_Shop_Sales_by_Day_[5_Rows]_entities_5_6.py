
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Date': [
        '2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05', 
        '2024-01-06', '2024-01-07', '2024-01-08', '2024-01-09', '2024-01-10',
        '2024-01-11', '2024-01-12', '2024-01-13', '2024-01-14', '2024-01-15', 
        '2024-01-16', '2024-01-17', '2024-01-18', '2024-01-19', '2024-01-20',
        '2024-01-21', '2024-01-22', '2024-01-23', '2024-01-24', '2024-01-25', 
        '2024-01-26', '2024-01-27', '2024-01-28', '2024-01-29', '2024-01-30',
        '2024-01-31'
    ],
    'Daily Visitors': [
        1500, 1800, 2100, 2300, 1900, 2500, 3000, 3200, 2800, 3500, 4000, 4200, 
        4500, 4800, 5000, 5200, 5100, 5300, 5500, 5800, 6000, 6200, 6100, 6300, 
        6500, 6800, 7000, 7200, 7500, 7800, 8000
    ]
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

plt.figure(figsize=(16, 10))
plt.fill_between(df['Date'], df['Daily Visitors'], color='#FF6347', alpha=0.7)
plt.plot(df['Date'], df['Daily Visitors'], color='#8B0000', linewidth=2)

plt.title('Daily Visitors in January 2024 - Entertainment & Leisure', fontsize=20, pad=20)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Daily Visitors', fontsize=14)

peak_visitors = df[df['Daily Visitors'] == df['Daily Visitors'].max()]
plt.annotate('Peak Visitors', xy=(peak_visitors['Date'].values[0], peak_visitors['Daily Visitors'].values[0]),
             xytext=(peak_visitors['Date'].values[0], peak_visitors['Daily Visitors'].values[0]+1000),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.grid(True)
plt.show()