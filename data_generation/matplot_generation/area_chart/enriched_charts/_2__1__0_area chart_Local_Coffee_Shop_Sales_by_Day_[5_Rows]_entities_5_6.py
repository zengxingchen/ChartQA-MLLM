
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
    'Daily Steps': [
        3500, 4200, 4600, 3900, 5200, 6100, 5800, 6700, 6200, 6900, 7200, 7500, 
        8000, 8500, 8700, 9100, 9300, 8900, 8600, 8400, 8200, 7800, 7600, 7400, 
        7000, 6700, 6200, 5900, 5600, 5300, 5000
    ]
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

plt.figure(figsize=(14, 8))
plt.fill_between(df['Date'], df['Daily Steps'], color='#87CEFA', alpha=0.7)
plt.plot(df['Date'], df['Daily Steps'], color='#4682B4', linewidth=2)

plt.title('Daily Steps in January 2024', fontsize=18)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Daily Steps', fontsize=14)

peak_steps = df[df['Daily Steps'] == df['Daily Steps'].max()]
plt.annotate('Peak Steps', xy=(peak_steps['Date'].values[0], peak_steps['Daily Steps'].values[0]),
             xytext=(peak_steps['Date'].values[0], peak_steps['Daily Steps'].values[0]+1000),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.grid(True)
plt.show()