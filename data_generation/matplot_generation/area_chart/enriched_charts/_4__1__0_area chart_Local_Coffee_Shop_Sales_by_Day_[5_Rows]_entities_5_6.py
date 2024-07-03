
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
    'Page Views': [
        120, 150, 130, 180, 170, 200, 220, 210, 230, 250, 260, 270, 280, 290, 
        300, 320, 310, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 
        440, 450, 460
    ]
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

plt.figure(figsize=(14, 8))
plt.fill_between(df['Date'], df['Page Views'], color='#87CEFA', alpha=0.6)
plt.plot(df['Date'], df['Page Views'], color='#1E90FF', linewidth=2)

plt.title('Daily Page Views in January 2024', fontsize=18, pad=20)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Page Views', fontsize=14)

max_views = df[df['Page Views'] == df['Page Views'].max()]
plt.annotate('Max Page Views', xy=(max_views['Date'].values[0], max_views['Page Views'].values[0]),
             xytext=(max_views['Date'].values[0], max_views['Page Views'].values[0] + 30),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.grid(True)
plt.show()