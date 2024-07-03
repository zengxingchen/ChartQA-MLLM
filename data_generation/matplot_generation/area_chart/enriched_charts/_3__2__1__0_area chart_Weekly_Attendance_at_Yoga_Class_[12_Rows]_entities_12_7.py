
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    'Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05', '2024-01-06', 
             '2024-01-07', '2024-01-08', '2024-01-09', '2024-01-10', '2024-01-11', '2024-01-12', 
             '2024-01-13', '2024-01-14', '2024-01-15', '2024-01-16', '2024-01-17', '2024-01-18', 
             '2024-01-19', '2024-01-20', '2024-01-21', '2024-01-22', '2024-01-23', '2024-01-24', 
             '2024-01-25', '2024-01-26', '2024-01-27', '2024-01-28', '2024-01-29', '2024-01-30'],
    'Steps Taken': [3450, 4200, 3800, 4600, 4800, 3500, 5000, 5300, 5500, 4900, 
                    5200, 5700, 6000, 6100, 5800, 5900, 6500, 6200, 6400, 6300, 
                    6100, 6600, 6700, 6800, 6400, 6200, 6500, 6600, 7000, 7100]
}

df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(16, 9))
plt.fill_between(df['Date'], df['Steps Taken'], color='#1f77b4', alpha=0.6)
plt.plot(df['Date'], df['Steps Taken'], color='#1f77b4', alpha=0.8)

# Annotation
max_date = df[df['Steps Taken'] == df['Steps Taken'].max()]['Date'].values[0]
max_value = df['Steps Taken'].max()
plt.annotate(f'Peak Steps: {max_value}', xy=(max_date, max_value), xytext=(max_date, max_value + 500),
             arrowprops=dict(facecolor='black', shrink=0.05))

# Title and labels
plt.title('Daily Steps Taken - January 2024', fontsize=18)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Steps Taken', fontsize=14)

# Rotate x-ticks for better readability
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()