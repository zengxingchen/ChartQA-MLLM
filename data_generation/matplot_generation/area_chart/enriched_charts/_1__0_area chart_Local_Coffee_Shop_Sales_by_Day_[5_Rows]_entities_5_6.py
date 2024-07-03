
import matplotlib.pyplot as plt
import pandas as pd

# Data
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
    'Stress Levels': [
        10, 12, 15, 9, 14, 20, 18, 22, 17, 19, 23, 25, 27, 29, 26, 28, 30, 24, 
        21, 19, 20, 22, 18, 17, 16, 14, 13, 15, 17, 20, 23
    ]
}

# Convert to DataFrame
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

# Plotting
plt.figure(figsize=(12, 6))
plt.fill_between(df['Date'], df['Stress Levels'], color='#FFA07A', alpha=0.7)
plt.plot(df['Date'], df['Stress Levels'], color='#FF6347', linewidth=2)

# Title and labels
plt.title('Daily Stress Levels Over January 2024', fontsize=16)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Stress Levels', fontsize=14)

# Annotations
peak_stress = df[df['Stress Levels'] == df['Stress Levels'].max()]
plt.annotate('Peak Stress', xy=(peak_stress['Date'].values[0], peak_stress['Stress Levels'].values[0]),
             xytext=(peak_stress['Date'].values[0], peak_stress['Stress Levels'].values[0]+5),
             arrowprops=dict(facecolor='black', shrink=0.05))

# Display the plot
plt.grid(True)
plt.show()