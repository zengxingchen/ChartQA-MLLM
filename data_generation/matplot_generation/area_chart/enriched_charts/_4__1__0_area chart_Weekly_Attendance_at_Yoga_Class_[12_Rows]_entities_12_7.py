
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05', '2024-01-06', 
             '2024-01-07', '2024-01-08', '2024-01-09', '2024-01-10', '2024-01-11', '2024-01-12', 
             '2024-01-13', '2024-01-14', '2024-01-15', '2024-01-16', '2024-01-17', '2024-01-18', 
             '2024-01-19', '2024-01-20', '2024-01-21', '2024-01-22', '2024-01-23', '2024-01-24', 
             '2024-01-25', '2024-01-26', '2024-01-27', '2024-01-28', '2024-01-29', '2024-01-30'],
    'Hours Worked': [8, 7.5, 9, 8, 7, 6, 5, 8, 9.5, 8.5, 
                     7.5, 6.5, 7, 8, 7.5, 6.5, 8, 9, 8.5, 7, 
                     8, 7.5, 8, 6.5, 8, 9, 7.5, 8.5, 7, 9.5]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 7))
plt.fill_between(df['Date'], df['Hours Worked'], color='#ff7f0e', alpha=0.6)
plt.plot(df['Date'], df['Hours Worked'], color='#ff7f0e', alpha=0.8)

max_date = df[df['Hours Worked'] == df['Hours Worked'].max()]['Date'].values[0]
max_value = df['Hours Worked'].max()
plt.annotate(f'Max Hours: {max_value}', xy=(max_date, max_value), xytext=(max_date, max_value + 1),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.title('Daily Working Hours - January 2024', fontsize=16, pad=20)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Hours', fontsize=12)

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()