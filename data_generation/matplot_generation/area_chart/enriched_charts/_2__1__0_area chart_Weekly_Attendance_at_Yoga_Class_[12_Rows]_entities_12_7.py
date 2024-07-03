
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    'Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05', '2024-01-06', 
             '2024-01-07', '2024-01-08', '2024-01-09', '2024-01-10', '2024-01-11', '2024-01-12', 
             '2024-01-13', '2024-01-14', '2024-01-15', '2024-01-16', '2024-01-17', '2024-01-18', 
             '2024-01-19', '2024-01-20', '2024-01-21', '2024-01-22', '2024-01-23', '2024-01-24', 
             '2024-01-25', '2024-01-26', '2024-01-27', '2024-01-28', '2024-01-29', '2024-01-30'],
    'Books Sold': [150, 120, 180, 200, 170, 160, 140, 190, 220, 210, 
                   200, 230, 180, 170, 150, 200, 210, 230, 190, 160, 
                   170, 220, 210, 200, 230, 180, 170, 190, 210, 220]
}

df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(14, 8))
plt.fill_between(df['Date'], df['Books Sold'], color='#2ca02c', alpha=0.6)
plt.plot(df['Date'], df['Books Sold'], color='#2ca02c', alpha=0.8)

# Annotation
max_date = df[df['Books Sold'] == df['Books Sold'].max()]['Date'].values[0]
max_value = df['Books Sold'].max()
plt.annotate(f'Peak Sales: {max_value}', xy=(max_date, max_value), xytext=(max_date, max_value + 20),
             arrowprops=dict(facecolor='black', shrink=0.05))

# Title and labels
plt.title('Daily Book Sales - January 2024', fontsize=16)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Books Sold', fontsize=14)

# Rotate x-ticks for better readability
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()