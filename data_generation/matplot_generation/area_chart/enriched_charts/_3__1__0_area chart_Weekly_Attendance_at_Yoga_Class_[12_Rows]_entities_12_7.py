
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05', '2024-01-06', 
             '2024-01-07', '2024-01-08', '2024-01-09', '2024-01-10', '2024-01-11', '2024-01-12', 
             '2024-01-13', '2024-01-14', '2024-01-15', '2024-01-16', '2024-01-17', '2024-01-18', 
             '2024-01-19', '2024-01-20', '2024-01-21', '2024-01-22', '2024-01-23', '2024-01-24', 
             '2024-01-25', '2024-01-26', '2024-01-27', '2024-01-28', '2024-01-29', '2024-01-30'],
    'Steps Count': [7000, 8500, 7900, 8200, 9200, 8800, 9300, 8700, 9100, 7600, 
                    8900, 9400, 8700, 9300, 7800, 8700, 9500, 8400, 9200, 8600, 
                    9000, 8800, 8700, 9100, 8900, 8700, 9400, 9300, 8500, 9000]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 7))
plt.fill_between(df['Date'], df['Steps Count'], color='#FFA07A', alpha=0.6)
plt.plot(df['Date'], df['Steps Count'], color='#FF6347', alpha=0.8)

max_date = df[df['Steps Count'] == df['Steps Count'].max()]['Date'].values[0]
max_value = df['Steps Count'].max()
plt.annotate(f'Peak Steps: {max_value}', xy=(max_date, max_value), xytext=(max_date, max_value + 500),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.title('Daily Steps Count - January 2024', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Steps', fontsize=12)

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()