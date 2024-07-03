
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    'Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05', '2024-01-06', 
             '2024-01-07', '2024-01-08', '2024-01-09', '2024-01-10', '2024-01-11', '2024-01-12', 
             '2024-01-13', '2024-01-14', '2024-01-15', '2024-01-16', '2024-01-17', '2024-01-18', 
             '2024-01-19', '2024-01-20', '2024-01-21', '2024-01-22', '2024-01-23', '2024-01-24', 
             '2024-01-25', '2024-01-26', '2024-01-27', '2024-01-28', '2024-01-29', '2024-01-30'],
    'Calories Consumed': [2000, 1800, 2200, 2100, 2300, 1900, 2000, 2050, 2150, 2250, 
                          2100, 2200, 2000, 1900, 2050, 1950, 2100, 2300, 2000, 1800, 
                          2200, 2050, 2150, 1950, 2100, 2200, 2000, 1850, 2300, 2000]
}

df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(12, 6))
plt.fill_between(df['Date'], df['Calories Consumed'], color='#1f77b4', alpha=0.6)
plt.plot(df['Date'], df['Calories Consumed'], color='#1f77b4', alpha=0.8)

# Annotation
max_date = df[df['Calories Consumed'] == df['Calories Consumed'].max()]['Date'].values[0]
max_value = df['Calories Consumed'].max()
plt.annotate(f'Peak Consumption: {max_value}', xy=(max_date, max_value), xytext=(max_date, max_value + 200),
             arrowprops=dict(facecolor='black', shrink=0.05))

# Title and labels
plt.title('Daily Calorie Consumption - January 2024', fontsize=14)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Calories', fontsize=12)

# Rotate x-ticks for better readability
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()