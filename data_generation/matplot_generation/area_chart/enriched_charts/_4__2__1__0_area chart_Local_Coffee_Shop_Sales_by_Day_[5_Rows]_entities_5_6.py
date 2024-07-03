
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
    'Calories Burned': [
        2500, 2700, 2900, 3100, 2800, 3300, 3500, 3700, 3600, 3900, 4000, 4100, 
        4200, 4300, 4500, 4600, 4400, 4300, 4200, 4100, 4000, 3900, 3800, 3700, 
        3600, 3500, 3400, 3300, 3200, 3100, 3000
    ]
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

plt.figure(figsize=(16, 9))
plt.fill_between(df['Date'], df['Calories Burned'], color='#FFA07A', alpha=0.6)
plt.plot(df['Date'], df['Calories Burned'], color='#FF4500', linewidth=2)

plt.title('Calories Burned in January 2024', fontsize=20, pad=20)
plt.xlabel('Date', fontsize=16)
plt.ylabel('Calories Burned', fontsize=16)

peak_calories = df[df['Calories Burned'] == df['Calories Burned'].max()]
plt.annotate('Peak Calories', xy=(peak_calories['Date'].values[0], peak_calories['Calories Burned'].values[0]),
             xytext=(peak_calories['Date'].values[0], peak_calories['Calories Burned'].values[0]+500),
             arrowprops=dict(facecolor='red', shrink=0.05))

plt.grid(True)
plt.show()