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
    'Fitness Levels': [
        5, 7, 8, 6, 9, 10, 12, 15, 14, 16, 18, 20, 21, 19, 22, 24, 26, 25, 
        27, 30, 32, 31, 33, 35, 34, 37, 38, 40, 39, 42, 45
    ]
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

plt.figure(figsize=(14, 8))
plt.fill_between(df['Date'], df['Fitness Levels'], color='#ADD8E6', alpha=0.7)
plt.plot(df['Date'], df['Fitness Levels'], color='#00008B', linewidth=2)

plt.title('Daily Fitness Levels Over January 2024', fontsize=18)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Fitness Levels', fontsize=14)

peak_fitness = df[df['Fitness Levels'] == df['Fitness Levels'].max()]
plt.annotate('Peak Fitness', xy=(peak_fitness['Date'].values[0], peak_fitness['Fitness Levels'].values[0]),
             xytext=(peak_fitness['Date'].values[0], peak_fitness['Fitness Levels'].values[0]+5),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.grid(True)
plt.show()