
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    'Date': ['2024-06-01', '2024-06-02', '2024-06-03', '2024-06-04', '2024-06-05', '2024-06-06', 
             '2024-06-07', '2024-06-08', '2024-06-09', '2024-06-10', '2024-06-11', '2024-06-12', 
             '2024-06-13', '2024-06-14', '2024-06-15', '2024-06-16', '2024-06-17', '2024-06-18', 
             '2024-06-19', '2024-06-20', '2024-06-21', '2024-06-22', '2024-06-23', '2024-06-24', 
             '2024-06-25', '2024-06-26', '2024-06-27', '2024-06-28', '2024-06-29', '2024-06-30'],
    'Visitors': [350, 420, 390, 450, 430, 410, 480, 500, 530, 550, 
                 510, 480, 520, 570, 600, 580, 620, 630, 600, 590, 
                 640, 660, 670, 650, 620, 640, 630, 620, 610, 650]
}

df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(16, 10))
plt.fill_between(df['Date'], df['Visitors'], color='#1f77b4', alpha=0.6)
plt.plot(df['Date'], df['Visitors'], color='#1f77b4', alpha=0.8)

# Annotation
max_date = df[df['Visitors'] == df['Visitors'].max()]['Date'].values[0]
max_value = df['Visitors'].max()
plt.annotate(f'Peak Visits: {max_value}', xy=(max_date, max_value), xytext=(max_date, max_value + 50),
             arrowprops=dict(facecolor='black', shrink=0.05))

# Title and labels
plt.title('Daily Tourist Visits - June 2024', fontsize=18, pad=20)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Visitors', fontsize=14)

# Rotate x-ticks for better readability
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()